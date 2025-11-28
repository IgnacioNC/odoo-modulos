from odoo import models, fields

class HistorialConductor(models.Model):
    _name = 'paqueteria.camion.historial'
    _description = 'Historial de conductores del camión'
    _order = 'fecha desc'

    camion_id = fields.Many2one('paqueteria.camion', string="Camión", required=True, ondelete='cascade')

    conductor_id = fields.Many2one('hr.employee', string="Conductor", required=True)

    fecha = fields.Date(string="Fecha", required=True, default=fields.Date.today)
