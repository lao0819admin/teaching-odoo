from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class HospitalResearchAspect(models.Model):
    _name = 'hospital.research.aspect'
    _description = 'Research aspect'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(index=True, required=True)
    parent_id = fields.Many2one(comodel_name='hospital.research.aspect',
                                string='Parent research',
                                index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many(comodel_name='hospital.research.aspect',
                               inverse_name='parent_id',
                               string='Child Categories')

    @api.constrains('parent_id')
    def check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]
