from odoo import models, fields, api

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = 'hospital.uni.person'

    name = fields.Char()

    active = fields.Boolean(
        default=True,)

    specialty = fields.Char(
        required=True,)

    is_intern = fields.Boolean(
        default=False,)

    mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        domain="[('is_intern','=',False)]",)

    @api.onchange('mentor_id, is_intern')
    def compute_intern(self):
        for obj in self:
            if obj.is_intern:
                obj.mentor_id.__setattr__(self, 'readonly', False)
                obj.is_intern = obj.mentor_id
            else:
                obj.mentor_id.__setattr__(self.mentor_id, 'readonly', True)
