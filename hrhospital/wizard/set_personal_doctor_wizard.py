from odoo import fields, models, _

class SetPersonalDoctor(models.TransientModel):
    _name = 'set.personal.doctor.wizard'

    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor', string='New value of personal doctor',)

    # action_create
    def action_set_doctor(self):
        patients = self.env['hospital.patient'].search([])
        # print(self.doctor_id.id)
        for patient in patients:
            patient.write(
                {'personal_doctor_id': self.doctor_id.id})
        return True

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
