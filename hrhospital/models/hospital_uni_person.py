from odoo import models, fields, api, _

class HospitalUniPerson(models.AbstractModel):
    _name = 'hospital.uni.person'
    _description = 'Person mixin'

    name = fields.Char()

    active = fields.Boolean(
        default=True,)

    last_name = fields.Char(
        required=True,
        string='Last name',)

    phone = fields.Char(
        required=False,)

    photo = fields.Binary(
        required=False,)

    gender = fields.Selection(
        default='male',
        required=True,
        selection=[('male', _('Male')), ('female', _('Female'))],)

    @api.onchange('name')
    def onchange_last_name(self):
        for obj in self:
            obj.last_name = obj.name
