# -*- coding: utf-8 -*-
# from odoo import http


# class Reportar(http.Controller):
#     @http.route('/reportar/reportar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reportar/reportar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reportar.listing', {
#             'root': '/reportar/reportar',
#             'objects': http.request.env['reportar.reportar'].search([]),
#         })

#     @http.route('/reportar/reportar/objects/<model("reportar.reportar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reportar.object', {
#             'object': obj
#         })

