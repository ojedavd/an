# -*- coding: utf-8 -*-
from openerp import http

# class An(http.Controller):
#     @http.route('/an/an/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/an/an/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('an.listing', {
#             'root': '/an/an',
#             'objects': http.request.env['an.an'].search([]),
#         })

#     @http.route('/an/an/objects/<model("an.an"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('an.object', {
#             'object': obj
#         })