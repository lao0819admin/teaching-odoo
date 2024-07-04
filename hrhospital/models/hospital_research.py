from odoo import models, fields

class HospitalResearch(models.Model):
    _name = 'hospital.research'
    _description = 'Research'

    active = fields.Boolean(
        default=True,)
    name = fields.Char()
    category_id = fields.Many2one(
        comodel_name='hospital.research.aspect',)
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',)
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',)

