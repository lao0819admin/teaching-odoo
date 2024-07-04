from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalDoctorVisitor(models.Model):
    _name = 'hospital.doctor.visitor'
    _description = 'Doctor visitor'

    name = fields.Char()

    active = fields.Boolean(
        default=True,)

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        required=True,)

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        required=True,)

    visit_date_planed = fields.Datetime(
        string='Date visit planed',)

    visit_date_reception = fields.Datetime(
        string='Date of reception',)

    diagnosis_id = fields.Many2one(
        comodel_name='hospital.diagnosis',)

    research_id = fields.Many2one(
        comodel_name='hospital.research',)

    visit_state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')],
        default='scheduled',
        string="State",
        required=True,)

    @api.onchange('doctor_id', 'patient_id')
    def onchange_set_name(self):
        for obj in self:
            obj.name = f'{obj.patient_id.name} - {obj.doctor_id.name}'

    @api.constrains('active')
    def constrains_active(self):
        for obj in self:
            if not obj.active and obj.diagnosis_id:
                raise ValidationError(_('removal of the diagnosis is not possible'))

    @api.ondelete(at_uninstall=False)
    def unlink_only_if_open(self):
        for obj in self:
            if obj.diagnosis_id:
                raise ValidationError(_('removal of the diagnosis is not possible'))
