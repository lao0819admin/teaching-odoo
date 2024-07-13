from odoo import models, fields, api

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = 'hospital.uni.person'

    name = fields.Char()

    active = fields.Boolean(
        default=True,)

    specialty = fields.Char(
        required=True)

    is_intern = fields.Boolean(
        default=False)

    mentor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        domain="[('is_intern','=', False)]",
        string='mentor_id',
        change_default=True,
        readonly=True if not is_intern else False)

    @api.onchange('is_intern', 'mentor_id')
    def compute_intern(self):
        if not self.is_intern:
            self.mentor_id = True
    # def compute_mentor(self):
    #    if not self.is_intern and self.mentor_id:

