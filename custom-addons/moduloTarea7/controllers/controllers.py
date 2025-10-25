# -*- coding: utf-8 -*-
# from odoo import http


# class Modulos(http.Controller):
#     @http.route('/modulos/modulos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulos/modulos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulos.listing', {
#             'root': '/modulos/modulos',
#             'objects': http.request.env['modulos.modulos'].search([]),
#         })

#     @http.route('/modulos/modulos/objects/<model("modulos.modulos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulos.object', {
#             'object': obj
#         })

