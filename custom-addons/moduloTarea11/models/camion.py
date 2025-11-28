from odoo import models, fields, api

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

    @api.onchange('conductor_actual_id')
    def _onchange_conductor_actual_id(self):
        """
        Actualización temporal del historial de conductores.
        """
        if not self._origin:
            return

        anterior = self._origin.conductor_actual_id
        nuevo = self.conductor_actual_id

        if anterior and anterior != nuevo:
            if anterior not in self.antiguos_conductores_ids:
                self.antiguos_conductores_ids += anterior

    def write(self, vals):
        """
        Guardamos el nuevo historial de conductores.
        """
        if 'conductor_actual_id' in vals:
            nuevo = self.env['hr.employee'].browse(vals['conductor_actual_id'])

            for camion in self:
                anterior = camion.conductor_actual_id

                if anterior and anterior != nuevo:
                    camion.antiguos_conductores_ids |= anterior

        return super(Camion, self).write(vals)
