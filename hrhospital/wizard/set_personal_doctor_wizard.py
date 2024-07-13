from odoo import fields, models, _

class SetPersonalDoctor(models.TransientModel):
    _name = 'set.personal.doctor.wizard'

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='New value of personal doctor',)

    def action_set_doctor(self):
        act_list = self._context.get('active_ids',[])
        patients = self.env['hospital.patient'].search([])
        for act_p in act_list:
            patient = patients[act_p-1]
            patient.write(
                            {'personal_doctor_id': self.doctor_id.id})

    def action_open_wizard(self):
        self.read()
        return {
            'name': _('Create personal doctor wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'set.personal.doctor.wizard',
            'res_id': self.id,
            'target': 'new',
            'context': {'active_ids': self._context.get('active_ids',[])},}
