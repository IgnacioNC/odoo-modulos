from odoo import models, fields, api
from datetime import date

class Nomina(models.Model):
    _name = "nomina.empleado"
    _description = "Nómina de empleado"

    empleado_id = fields.Many2one("hr.employee", string="Empleado", required=True)
    sueldo_base = fields.Float(string="Sueldo Base", required=True)

    bonificacion_ids = fields.One2many(
        "nomina.bonificacion", "nomina_id", string="Bonificaciones/Deducciones"
    )

    irpf = fields.Float(string="IRPF (%)", required=True)

    irpf_pagado = fields.Float(
        string="IRPF Pagado (€)",
        compute="_compute_irpf_pagado",
        store=True
    )

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

    # ---- CÁLCULOS ----

    @api.depends("sueldo_base", "bonificacion_ids", "irpf")
    def _compute_irpf_pagado(self):
        for rec in self:
            bruto = rec.sueldo_base + sum(
                b.importe for b in rec.bonificacion_ids if b.importe > 0
            )
            rec.irpf_pagado = bruto * (rec.irpf / 100)

    @api.depends("bonificacion_ids")
    def _compute_totales(self):
        for rec in self:
            rec.total_bonificaciones = sum(
                b.importe for b in rec.bonificacion_ids if b.importe > 0
            )
            rec.total_deducciones = abs(
                sum(b.importe for b in rec.bonificacion_ids if b.importe < 0)
            )

    @api.depends("sueldo_base", "bonificacion_ids", "total_deducciones", "irpf_pagado")
    def _compute_total_sueldo(self):
        for rec in self:
            rec.total_sueldo = (
                rec.sueldo_base
                + rec.total_bonificaciones
                - rec.total_deducciones
                - rec.irpf_pagado
            )