from odoo import models, fields

class Camion(models.Model):
    _name = 'paqueteria.camion'
    _description = 'Camión de transporte'
    _rec_name = 'matricula'

    matricula = fields.Char(string='Número de matrícula', required=True)

    conductor_actual_id = fields.Many2one('hr.employee', string='Conductor actual')

    antiguos_conductores_ids = fields.Many2many(
        'hr.employee',
        string='Antiguos conductores'
    )

    fecha_itv = fields.Date(string='Fecha de la última ITV')
    notas_mantenimiento = fields.Text(string='Notas de mantenimiento')

    paquete_ids = fields.One2many(
        'paqueteria.paquete',
        'camion_id',
        string='Paquetes transportados'
    )

    _sql_constraints = [
        ('unique_matricula',
         'unique(matricula)',
         'La matrícula debe ser única.')
    ]