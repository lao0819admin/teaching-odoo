from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalDiseaseAspect(models.Model):
    _name = 'hospital.disease.aspect'
    _description = 'Disease aspect'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(index=True, required=True)

    complete_name = fields.Char(compute='_compute_complete_name',
                                recursive=True,
                                store=True)

    parent_id = fields.Many2one(comodel_name='hospital.disease.aspect',
                                string='Parent Disease',
                                index=True,
                                ondelete='cascade')

    parent_path = fields.Char(index=True)

    child_id = fields.One2many(comodel_name='hospital.disease.aspect',
                               inverse_name='parent_id',
                               string='Child Categories')

    disease_count = fields.Integer(
        '# Disease', compute='_compute_disease_aspect_count',
        help="Disease")

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = \
                    '%s / %s' % \
                    (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_disease_type_count(self):
        for obj in self:
            obj.disease_count = 777

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]
