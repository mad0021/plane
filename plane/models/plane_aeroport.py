from odoo import models, fields
class plane_aeroport(models.Model):
    _name = 'plane.aeroport'
    codi = fields.Integer('codi', required=True)
    nom = fields.Char('nom')
    imagen = fields.Image('imagen')
    ciutat = fields.Char('ciutat')
    pais = fields.Char('pais')
    lat = fields.Float('latitut')
    long = fields.Float('longitut')