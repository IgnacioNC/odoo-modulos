from odoo import models, fields

class Ejemplo(models.Model):
    _name = 'modulotarea7.ejemplo'
    _description = 'Modulo de ejemplo para la Tarea 7'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha = fields.Date(string="Fecha de creación")
