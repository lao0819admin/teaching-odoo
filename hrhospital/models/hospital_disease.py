from odoo import models, fields

class DHospitalisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'

    name = fields.Char(
        required=True)

    active = fields.Boolean(
        default=True,)

    category_id = fields.Many2one(
        comodel_name='hospital.disease.aspect',)
