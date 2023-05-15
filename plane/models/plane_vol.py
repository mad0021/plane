from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    codi = fields.Integer('codi', required=True)
    passatgers = fields.Integer('passatgers')
    datasortida = fields.DateTime('data_de_sortida')
    dataarrivada = fields.DateTime('data_d_arrivada')