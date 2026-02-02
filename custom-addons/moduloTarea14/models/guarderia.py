from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Guarderia(models.Model):
    _name = 'modulotarea14.guarderia'
    _description = 'Guardería para empleados'
    _inherits = {'hr.employee': 'employee_id', 'event.event': 'event_id'}

    employee_id = fields.Many2one('hr.employee', required=True, ondelete='cascade', auto_join=True, index=True)
    event_id = fields.Many2one('event.event', required=True, ondelete='cascade', auto_join=True, index=True)

    descripcion = fields.Text(string='Descripción')
    rango_edad = fields.Selection( 
        [
            ('0_2', '0 - 2 años'),
            ('3_5', '3 - 5 años'),
            ('6_8', '6 - 8 años'),
            ('9_11', '9 - 11 años')
        ],
        string='Rango de Edad', required=True)