from odoo import models, fields

class HospitalContact(models.Model):
    _name = 'hospital.contact.person'
    _description = 'Contact person'
    _inherit = 'hospital.uni.person'

    name = fields.Char()

    active = fields.Boolean(
        default=True,)
