# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modulos(models.Model):
#     _name = 'modulos.modulos'
#     _description = 'modulos.modulos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from . import componente
from . import ordenador
