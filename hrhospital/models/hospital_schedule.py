from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalSchedule(models.Model):
    _name = 'hospital.schedule'
    _description = 'Schedule'

    name = fields.Char()
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor', )
    date_from = fields.Datetime(
        string='Date from', )
    date_to = fields.Datetime(
        string='Date to', )
    finished = fields.Boolean(
        string='finished', )

    @api.constrains('date_from', 'date_to')
    def _check_correct_date(self):
        for current in self:
            date_from_count = current.search_count(
                [('doctor_id', '=', current.doctor_id.id),
                 ('date_from', '>=', current.date_from),
                 ('date_from', '<=', current.date_to),
                 ('id', '!=', current.id)
                 ])

            date_to_count = current.search_count(
                [('doctor_id', '=', current.doctor_id.id),
                 ('date_to', '>=', current.date_from),
                 ('date_to', '<=', current.date_to),
                 ('id', '!=', current.id)
                 ])

            if date_from_count != 0 or date_to_count != 0:
                raise ValidationError(_('date to is not valid'))

    @api.onchange('date_from', 'date_to')
    def check_date(self):
        for obj in self:
            if obj.finished:
                raise ValidationError(_('can`t modified finished schedule'))

    @api.onchange('date_from', 'date_to', 'doctor_id')
    def set_name(self):
        for obj in self:
            obj.name = f'{obj.doctor_id.name} | {obj.date_from} - ' \
                       f'{obj.date_to}'
