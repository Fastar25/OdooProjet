# -*- coding: utf-8 -*-
# from odoo import http


# class Librairie(http.Controller):
#     @http.route('/librairie/librairie', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/librairie/librairie/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('librairie.listing', {
#             'root': '/librairie/librairie',
#             'objects': http.request.env['librairie.librairie'].search([]),
#         })

#     @http.route('/librairie/librairie/objects/<model("librairie.librairie"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('librairie.object', {
#             'object': obj
#         })
