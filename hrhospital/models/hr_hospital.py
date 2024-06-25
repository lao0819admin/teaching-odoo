import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class HrHospital(models.Model):
    _name = 'hr.hospital'
    _description = 'Hr Hospital'

    doc_name = fields.Char()
    patient_name = fields.Char()
    types_diseases = fields.Char()
    date_visit = fields.Date()
    # image = fields.Image()
