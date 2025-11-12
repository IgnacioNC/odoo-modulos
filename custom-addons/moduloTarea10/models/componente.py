from odoo import models, fields

class Componente(models.Model):
    _name = 'modulotarea10.componente'
    _description = 'Componentes (Nombres, especificaciones y precios).'

    name = fields.Char(string="Nombre", required=True)
    specs = fields.Text(string="Especificaciones")
    price = fields.Monetary(string="Precio")
