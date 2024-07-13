from datetime import date
from odoo import api, fields, models, _


class GetReportDiagnosis(models.TransientModel):  #AbstractModel
    _name = "get.report.diagnosis.wizard"
    _description = "Get Report"

    doctor_ids = fields.Many2many(comodel_name='hospital.doctor',
                                  string="Doctor",
                                  required=True, )

    disease_ids = fields.Many2many(comodel_name='hospital.disease',
                                   required=True, )

    patient_id = fields.Many2one(comodel_name='hospital.patient',
                                 required=False, )

    start_date = fields.Datetime(string='Start Date',
                                 required=True, )

    finish_date = fields.Datetime(string='Finish Date',
                                  required=True, )

    # @api.model
    def action_get_report_diagnosis(self):

        domain = [("date", ">=", str(self.start_date)),
                  ("date", "<=", str(self.finish_date))]

        if self.disease_ids:
            domain.append(("disease_id", "in", self.disease_ids.ids))

        return {
            'name': _('Diagnosis report doctor (Date)'),
            'view_mode': 'tree',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'hospital.diagnosis',
            'type': 'ir.actions.act_window',
            'domain': domain,
            'context': {
                'group_by': 'doctor_id',
            }
        }