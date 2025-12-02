from odoo import models, fields

class Paquete(models.Model):
    _name = 'paqueteria.paquete'
    _description = 'Paquete de Envío'
    _rec_name = 'numero_seguimiento'

    numero_seguimiento = fields.Char(string='N.º de Seguimiento', required=True)

    remitente_id = fields.Many2one('res.partner', string='Remitente', required=True)
    destinatario_id = fields.Many2one('res.partner', string='Destinatario', required=True)

    pais_id = fields.Many2one('res.country', string='País')
    region_id = fields.Many2one('res.country.state', string='Región/Provincia')
    municipio = fields.Char(string='Municipio')
    calle = fields.Char(string='Calle')
    numero = fields.Char(string='Número')
    datos_adicionales = fields.Text(string='Datos adicionales')

    camion_id = fields.Many2one('paqueteria.camion', string='Camión Actual')

    estado_envio_ids = fields.One2many('paqueteria.estado_envio', 'paquete_id', string='Historial del Envío')

    _sql_constraints = [('unique_tracking_number', 'unique(numero_seguimiento)', 
                         'El número de seguimiento debe ser único.')]