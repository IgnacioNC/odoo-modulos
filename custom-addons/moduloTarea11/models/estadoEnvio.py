from odoo import models, fields

class EstadoEnvio(models.Model):
    _name = 'paqueteria.estado_envio'
    _description = 'Estado del envío'

    paquete_id = fields.Many2one(
        'paqueteria.paquete',
        string='Paquete',
        required=True
    )

    fecha = fields.Datetime(
        string='Fecha de entrada',
        default=fields.Datetime.now,
        required=True
    )

    estado = fields.Selection(
        [
            ('recibido', 'Recibido'),
            ('en_transito', 'En tránsito'),
            ('retrasado', 'Retrasado'),
            ('entregado', 'Entregado'),
        ],
        string='Estado',
        required=True
    )

    notas = fields.Text(string='Notas adicionales')