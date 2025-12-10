from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class Nomina(models.Model):
    _name = "nomina.empleado"
    _description = "Nómina de empleado"
    _record_name = "name"

    empleado_id = fields.Many2one("hr.employee", string="Empleado", required=True)
    
    sueldo_base = fields.Float(string="Sueldo Base", required=True)

    name = fields.Char(compute="_compute_name", store=True)

    renta_id = fields.Many2one("empleado.renta", string="Declaración de la Renta", ondelete="set null")

    bonificacion_ids = fields.One2many("nomina.bonificacion", "nomina_id", string="Bonificaciones/Deducciones")

    irpf = fields.Float(string="IRPF (%)", default=0, required=True)

    irpf_pagado = fields.Float(string="IRPF Pagado (€)", compute="_compute_irpf_pagado", store=True)

    fecha = fields.Date(string="Fecha", default=fields.Date.today)

    documento_pdf = fields.Binary(string="Justificante PDF")

    documento_pdf_name = fields.Char()

    estado = fields.Selection(
        [
            ("redactada", "Redactada"),
            ("confirmada", "Confirmada"),
            ("pagada", "Pagada")
        ],

        default="redactada",
        string="Estado",
        required=True
    )

    total_bonificaciones = fields.Float(
        string="Total Bonificaciones",
        compute="_compute_totales"
    )
    total_deducciones = fields.Float(
        string="Total Deducciones",
        compute="_compute_totales"
    )

    total_sueldo = fields.Float(
        string="Total Neto",
        compute="_compute_total_sueldo"
    )

    @api.depends("sueldo_base", "bonificacion_ids", "irpf")
    def _compute_irpf_pagado(self):
        for record in self:
            bruto = record.sueldo_base + sum(
                b.importe for b in record.bonificacion_ids if b.importe > 0
            )
            record.irpf_pagado = bruto * (record.irpf / 100)

    @api.depends("bonificacion_ids")
    def _compute_totales(self):
        for record in self:
            record.total_bonificaciones = sum(
                b.importe for b in record.bonificacion_ids if b.importe > 0
            )
            record.total_deducciones = abs(
                sum(b.importe for b in record.bonificacion_ids if b.importe < 0)
            )

    @api.depends("sueldo_base", "bonificacion_ids", "total_deducciones", "irpf_pagado")
    def _compute_total_sueldo(self):
        for record in self:
            record.total_sueldo = (
                record.sueldo_base
                + record.total_bonificaciones
                - record.total_deducciones
                - record.irpf_pagado
            )
        
    @api.depends("empleado_id", "fecha")
    def _compute_name(self):
        for record in self:
            if record.empleado_id and record.fecha:
                record.name = f"{record.empleado_id.name} – {record.fecha.strftime('%B %Y')}"
            elif record.empleado_id:
                record.name = record.empleado_id.name
            else:
                record.name = "Nómina"

    @api.constrains("irpf")
    def _check_irpf_range(self):
        for r in self:
            if r.irpf < 0 or r.irpf > 100:
                raise ValidationError("El IRPF debe estar entre 0 y 100.")            

    @api.constrains("sueldo_base")
    def _check_sueldo_base(self):
        for r in self:
            if r.sueldo_base < 0:
                raise ValidationError("El sueldo base no puede ser negativo. El salario mínimo permitido es 0.")
            