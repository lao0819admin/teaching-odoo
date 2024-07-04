from odoo import models, api, fields

class HospitalPersonalDoctorHistory(models.Model):
    _name = 'hospital.personal.doctor.history'
    _description = 'Personal doctor history'

    name = fields.Char()
    active = fields.Boolean(
        default=True,)
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        required=True,)
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True,)
    appointment_date = fields.Date(
        string='Appointment date',
        required=True,)

    @api.onchange('doctor_id', 'patient_id')
    def onchange_set_name(self):
        for obj in self:
            patient_name = ''
            doctor_name = ''
            if obj.patient_id:
                patient_name = obj.patient_id.name
            if obj.doctor_id:
                doctor_name = obj.doctor_id.name
            obj.name = f'{patient_name} - {doctor_name}'
