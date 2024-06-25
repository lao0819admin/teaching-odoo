import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class MyTo(models.Model):
    _name = 'my.to'
    _description = 'MyTo'

    name = fields.Char()
    active = fields.Boolean(default=True, )

    date = fields.Date()
    yesterday = fields.Date()
    qty = fields.Integer()

    partner_id = fields.Many2one(comodel_name='res.partner')

    image = fields.Image()
