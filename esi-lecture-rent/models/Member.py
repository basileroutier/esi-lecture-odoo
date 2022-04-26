from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)


class Member(models.Model):
    _inherit = 'res.partner'
    number = fields.Char(string='matricule étudiant')
    rent_ids = fields.One2many('esi.lecture.livre.rent', 'member_id', string="Pret réalisé")
    _logger.info('------------------------------------\nMember model %s\n------------------------------------',
                 __name__)
