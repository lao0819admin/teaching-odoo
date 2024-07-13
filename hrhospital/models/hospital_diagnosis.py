from odoo import models, fields


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(
        required=True,)

    active = fields.Boolean(
        default=True,)

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True,)

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        required=True,)

    disease_id = fields.Many2one(
        comodel_name='hospital.disease',)

    date = fields.Datetime()

    diagnosis_correct = fields.Boolean(
        default=True, )

    research_id = fields.Many2one(
        comodel_name='hospital.research',)
