from odoo import http

class ExploreNewProductsView(http.Controller):
    @http.route('/explore_new_products_template/', auth="public", type="json", methods=['POST'])
    def all_new_products(self):
        new_product = http.request.env['product.template'].search_read([],
                                                                             ['name', 'list_price', 'image_1920'])
        return new_product
