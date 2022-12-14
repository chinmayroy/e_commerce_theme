from odoo import http


class CyCities(http.Controller):

    @http.route('/cities/', auth="public", type="json", methods=['POST'])
    def all_cities(self):
        cities = http.request.env['cy.cities'].search_read([], ['country_id', 'state_id', 'image'])
        return cities
