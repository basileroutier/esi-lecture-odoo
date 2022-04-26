from odoo import api, fields, models
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class Livre(models.Model):
    _name = 'esi.lecture.livre'
    _inherit = ['esi.lecture.livre']

    rent_id = fields.One2many('esi.lecture.livre.rent', 'book_id', string="Un prêt")

    total_rent = fields.Integer(string="Nombre emprunt total du livre", compute="_get_all_emprunt", store=True,
                                default=0)

    @api.depends('rent_id')
    def _get_all_emprunt(self):
        for book in self:
            total = 0
            for rent in book.rent_id:
                total += 1

            self.total_rent = total

    _logger.info('------------------------------------\nBook inherit %s\n------------------------------------',
                 __name__)
