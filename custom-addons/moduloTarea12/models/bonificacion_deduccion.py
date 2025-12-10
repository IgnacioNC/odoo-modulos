from odoo import models, fields

class NominaBonificacion(models.Model):
    _name = "nomina.bonificacion"
    _description = "Bonificación o deducción de nómina"

    nomina_id = fields.Many2one("nomina.empleado", string="Nómina", required=True)

    importe = fields.Float(string="Importe Bruto", help="Positivo = bonificación, negativo = deducción", required=True)

    concepto = fields.Char(string="Concepto", required=True)