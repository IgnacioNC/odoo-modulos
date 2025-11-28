from odoo import models, fields, api

class Camion(models.Model):
    _name = 'paqueteria.camion'
    _description = 'Camión de transporte'
    _rec_name = 'matricula'

    matricula = fields.Char(string='Número de matrícula', required=True)

    conductor_actual_id = fields.Many2one('hr.employee', string='Conductor actual')

    historial_ids = fields.One2many('paqueteria.camion.historial', 'camion_id', string='Historial de Conductores')

    fecha_itv = fields.Date(string='Fecha de la última ITV')
    
    notas_mantenimiento = fields.Text(string='Notas de mantenimiento')

    paquete_ids = fields.One2many('paqueteria.paquete', 'camion_id', string='Paquetes transportados')

    _sql_constraints = [('unique_matricula', 'unique(matricula)', 'La matrícula debe ser única.')]

    def write(self, vals):
        #Cuando cambia el conductor actual guarda el conductor anterior en el historial.
        if 'conductor_actual_id' in vals:
            nuevo = vals['conductor_actual_id']

            for camion in self:
                anterior = camion.conductor_actual_id

                # Si había conductor anterior y es distinto del nuevo se guarda een el historial
                if anterior and anterior.id != nuevo:
                    self.env['paqueteria.camion.historial'].create({
                        'camion_id': camion.id,
                        'conductor_id': anterior.id,
                    })

        return super(Camion, self).write(vals)
