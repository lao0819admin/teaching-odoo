import datetime

from odoo import models, fields, _, api
# from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit = 'hospital.uni.person'

    name = fields.Char()

    active = fields.Boolean(
        default=True,)

    birthday_date = fields.Date(
        string='Date of birth', required=True,)

    age = fields.Integer(
        compute='compute_age',)

    passport = fields.Char()

    contact_id = fields.Many2one(
        comodel_name='hospital.contact.person', string='Contact',)

    personal_doctor_id = fields.Many2one(
        comodel_name='hospital.doctor', required=True,)

    @api.constrains('contact_id', 'personal_doctor_id')
    def check_fields(self):
        for patient in self:
            if patient.contact_id is False:
                raise ValueError('Contact')
                # ValidationError(_('You cannot create contact person.'))
                # pass


    @api.model_create_multi
    def create(self, values):
        return super(HospitalPatient, self).create(values)

    def write(self, values):
        for obj in self:
            if 'personal_doctor_id' in values:
                doctor_history_values = {
                    'name': f'{obj.contact_id.name} - '
                            f'{obj.personal_doctor_id.name}',
                    'active': True,
                    'patient_id': obj.id,
                    'doctor_id': values['personal_doctor_id'],
                    'appointment_date': datetime.date.today()
                }
                self.env['hospital.personal.doctor.history'].\
                    create(doctor_history_values)

        return super(HospitalPatient, self).write(values)

    @api.depends('birthday_date')
    def compute_age(self):
        for obj in self:
            if obj.birthday_date:
                date_today = datetime.date.today()
                extra_year = ((date_today.month, date_today.day) <
                              (obj.birthday_date.month, obj.birthday_date.day))
                obj.age = date_today.year - obj.birthday_date.year - extra_year
            else:
                obj.age = 0
