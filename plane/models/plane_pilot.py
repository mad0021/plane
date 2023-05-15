from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    codi = fields.Integer('codi', required=True)
    nom = fields.Char('nom')
    cognoms = fields.Char('cognoms')
    nif = fields.Char('nif')
    telf = fields.Char('telefono')
    gmail = fields.Char('gmail')