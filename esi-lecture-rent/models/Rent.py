from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)


class Rent(models.Model):
    _name = 'esi.lecture.livre.rent'
    _description = 'Prêt livre'
    book_id = fields.Many2one('esi.lecture.livre', string="Livre prêté", required=True)
    member_id = fields.Many2one('res.partner', string='Membre qui a emprunté', required=True)
    state = fields.Selection(
        [('pret', 'Exemplaire prêté'), ('return', 'Exemplaire retourné'), ('lost', 'Exemplaire perdu')], default='pret')
    rent_date = fields.Date(string='Date emprunt livre', default=datetime.today())
    return_data = fields.Date(string='Date retour livre')
    _logger.info('------------------------------------\nRent Model %s\n------------------------------------',
                 __name__)

    @api.constrains('book_id')
    def _check_book_not_return(self):
        for rent in self:
            for book in rent.book_id:
                for livre in book.rent_id:
                    if book != self.book_id:
                        if livre.state == 'pret':
                            raise ValidationError('Le livre a pas encore été retourné')

    @api.depends('book_id')
    def _get_name_book(self):
        self.name_book = self.book_id.name

    @api.depends('member_id')
    def _get_matricule_member(self):
        self.name_member = self.member_id.number

    name_member = fields.Char(string="Matricule du membre", compute="_get_matricule_member", store=True)
    name_book = fields.Char(string="Nom du livre", compute="_get_name_book", store=True)
