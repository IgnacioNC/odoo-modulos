from odoo import models, fields, api

class DeclaracionRenta(models.Model):
    _name = "empleado.renta"
    _description = "Declaración anual del empleado"

    empleado_id = fields.Many2one("hr.employee", required=True)
    year = fields.Integer(string="Año", required=True)

    nominas_ids = fields.Many2many("nomina.empleado", string="Nóminas")

    sueldo_bruto_total = fields.Float(
        compute="_compute_totales", store=True
    )
    impuestos_pagados = fields.Float(
        compute="_compute_totales", store=True
    )

    @api.depends("nominas_ids")
    def _compute_totales(self):
        for rec in self:
            rec.sueldo_bruto_total = sum(n.sueldo_base + n.total_bonificaciones for n in rec.nominas_ids)
            rec.impuestos_pagados = sum(n.irpf_pagado for n in rec.nominas_ids)