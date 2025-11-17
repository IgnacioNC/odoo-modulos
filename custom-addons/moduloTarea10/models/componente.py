from odoo import models, fields

class Componente(models.Model):
    _name = 'modulotarea10.componente'
    _description = 'Componentes (Nombres, especificaciones y precios).'

    name = fields.Char(string="Nombre", required=True)
    specs = fields.Text(string="Especificaciones")
    price = fields.Monetary(string="Precio")

    currency_id = fields.Many2one(
        'res.currency',
        string='Moneda',
        required=True,
        default=lambda self: self.env.company.currency_id.id
    )
