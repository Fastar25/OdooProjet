from odoo import api,fields, models
from odoo.exceptions import Warning

class Livre(models.Model):

    _name = 'librairie.livre'
    _description = 'Livre'
    titre = fields.Char()
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_publication = fields.Date()
    image = fields.Binary()
    maison_edition = fields.Many2one('res.partner')
    auteurs = fields.Many2many('res.partner')

    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 5:
            return True

    def button_check_isbn(self):
        for livre in self:
            if not livre.isbn:
                raise Warning('Veuillez donner un ISBN pour %s' % livre.titre)
            if livre.isbn and not livre._check_isbn():
                raise Warning('%s est un ISBN invalide (donner 5 entiers)' % livre.isbn)
                return True
