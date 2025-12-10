from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class DeclaracionRenta(models.Model):
    _name = "empleado.renta"
    _description = "Declaración anual del empleado"

    empleado_id = fields.Many2one("hr.employee", required=True)

    year = fields.Integer(string="Año", required=True)

    nominas_ids = fields.Many2many("nomina.empleado", string="Nóminas")

    max_nominas = 14

    sueldo_bruto_total = fields.Float(compute="_compute_totales", store=True)

    impuestos_pagados = fields.Float(compute="_compute_totales", store=True)

    irpf_teorico = fields.Float(compute="_compute_totales", store=True)
    
    regularizacion = fields.Float(compute="_compute_totales", store=True)

    @api.depends(
    "nominas_ids",
    "nominas_ids.sueldo_base",
    "nominas_ids.total_bonificaciones",
    "nominas_ids.irpf_pagado"
    )
    def _compute_totales(self):
        for record in self:

            # SUMA TOTAL (año)
            bruto = sum(n.sueldo_base + n.total_bonificaciones for n in record.nominas_ids)
            retenido = sum(n.irpf_pagado for n in record.nominas_ids)

            record.sueldo_bruto_total = bruto
            record.impuestos_pagados = retenido

            if bruto <= 0:
                record.irpf_teorico = 0
                record.regularizacion = -retenido
                continue

            base_liquidable = bruto

            tramos = [
                (12450, 0.095),
                (20200, 0.12),
                (35200, 0.15),
                (60000, 0.185),
                (300000, 0.225),
            ]

            pendiente = base_liquidable
            irpf_teorico = 0
            limite_anterior = 0

            for limite, tipo in tramos:
                if pendiente <= 0:
                    break

                tramo_base = min(pendiente, limite - limite_anterior)
                irpf_teorico += tramo_base * tipo
                pendiente -= tramo_base
                limite_anterior = limite

            if pendiente > 0:
                irpf_teorico += pendiente * 0.24

            record.irpf_teorico = irpf_teorico

            # REGULARIZACIÓN FINAL
            record.regularizacion = irpf_teorico - retenido

    @api.constrains("nominas_ids")
    def _check_max_nominas(self):
        for record in self:
            if len(record.nominas_ids) > record.max_nominas:
                raise ValidationError("Solo se permiten un máximo de " + str(record.max_nominas) + " nóminas vinculadas.")

    @api.constrains("nominas_ids","year")
    def _check_nomina_year(self):
        for record in self:
            for nomina in record.nominas_ids:
                if nomina.fecha:
                    nomina_year = nomina.fecha.year
                    if nomina_year != record.year:
                        raise ValidationError("La nómina del " + str(nomina.fecha) + " pertenece al año " + 
                        str(nomina.fecha.year) + ", pero esta declaración es del año " + str(record.year) + ".")
                    
    @api.constrains("nominas_ids", "empleado_id")
    def _check_nominas_empleado(self):
        for record in self:
            for nomina in record.nominas_ids:
                if nomina.empleado_id != record.empleado_id:
                    raise ValidationError("La nómina " + str(nomina.name) + " pertenece a " + str(nomina.empleado_id.name) + 
                    ", pero esta declaración es de " + str(record.empleado_id.name) + ".")
           
