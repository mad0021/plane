from odoo import models, fields
class plane_avio(models.Model):
    _name = 'plane.avio'
    codi = fields.Integer('codi', required=True)
    imagen = fields.Image('imagen')
    marca = fields.Char('marca')
    model= fields.Char('model')
    maxvel = fields.Float('velocitat_max')