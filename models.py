# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Ta(models.Model):

    _name = 'an.ta'  #  Model odoo name

    cve = fields.Boolean(string='Circuito de Verificación de Equipos')
    cve_operario = fields.Many2one('res.partner', string="Operario")