from odoo import http


class ExploreProductCategory(http.Controller):
    @http.route('/explore_product_category/', auth="public", type="json", methods=['POST'])
    def all_category(self):
        category = http.request.env['product.public.category'].search_read([], ['name', 'image_1920'])
        return category