from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DeclaracionRenta(models.Model):
    _name = "empleado.renta"
    _description = "Declaración anual del empleado"

    empleado_id = fields.Many2one("hr.employee", required=True)
    year = fields.Integer(string="Año", required=True)

    nominas_ids = fields.Many2many("nomina.empleado", string="Nóminas")

    max_nominas = 1

    sueldo_bruto_total = fields.Float(
        compute="_compute_totales", store=True
    )
    impuestos_pagados = fields.Float(
        compute="_compute_totales", store=True
    )

    @api.depends("nominas_ids")
    def _compute_totales(self):
        for record in self:
            record.sueldo_bruto_total = sum(n.sueldo_base + n.total_bonificaciones for n in record.nominas_ids)
            record.impuestos_pagados = sum(n.irpf_pagado for n in record.nominas_ids)

    @api.constrains("nominas_ids")
    def _check_max_nominas(self):
        for record in self:
            if len(record.nominas_ids) > record.max_nominas:
                raise ValidationError("Solo se permiten un máximo de 3 nóminas vinculadas.")

