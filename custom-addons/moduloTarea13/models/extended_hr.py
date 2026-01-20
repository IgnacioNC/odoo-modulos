from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class ExtendedHR(models.Model):
    _inherit = "hr.employee"

    dni = fields.Char(string="DNI", size=9)
    nss = fields.Char(string="Número de la Seguridad Social", size=12)

    @api.constrains("dni", "nss")
    def _check_dni_nss(self):
        letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"

        for record in self:
            if record.dni:
                if not re.match(r"^[0-9]{8}[A-Z]$", record.dni):
                    raise ValidationError("El DNI debe tener 8 números y una letra mayúscula.")

                numero = int(record.dni[:8])
                letra_correcta = letras_dni[numero % 23]
                if record.dni[8] != letra_correcta:
                    raise ValidationError("La letra del DNI no es correcta.")

            if record.nss:
                if not re.match(r"^[0-9]{12}$", record.nss):
                    raise ValidationError("El NSS debe tener exactamente 12 dígitos.")

                provincia = int(record.nss[:2])
                cuerpo = record.nss[:10]
                control = int(record.nss[10:])

                if provincia < 1 or provincia > 52:
                    raise ValidationError("Los dos primeros dígitos del NSS deben corresponder a una provincia válida.")

                if int(cuerpo) % 97 != control:
                    raise ValidationError("Los dígitos de control del NSS no son correctos.")

