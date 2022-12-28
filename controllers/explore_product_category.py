from odoo import http


class ExploreProductCategory(http.Controller):
    @http.route('/explore_product_category/', auth="public", type="json", methods=['POST'])
    def all_category(self):
        category = http.request.env['product.category.view'].search_read([], ['category_name', 'description', 'image'])
        return category
