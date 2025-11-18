from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Ordenador(models.Model):
    _name = 'modulotarea10.ordenador'
    _description = 'Ordenador (Nº Equipos, Usuarios, Lista De Piezas, Última Modificación, Precio Total e Incidencias).'

    num_pc = fields.Char(string="Nombre", required=True)
    user_id = fields.Many2one("res.users",string="Usuario")
    components_ids = fields.Many2many("modulotarea10.componente", string="Componentes")
    incidences = fields.Text(string="Incidencias")

    @api.constrains('ultima_mod')
    def _comprobar_fecha(self):
        for record in self:
            if record.ultima_mod > date.today():
                raise ValidationError("La fecha no puede ser futura")
            
    ultima_mod = fields.Date(string="Fecha última modificación", compute="_compute_total", store=True)        

    @api.depends('components_ids.price')
    def _compute_total(self):
        for record in self:
            record.total_price = sum(record.components_ids.mapped('price'))

    total_price = fields.Monetary(string="Precio Total", compute="_compute_total", store=True, currency_field='currency_id')

    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id.id,
        required=True
    )


