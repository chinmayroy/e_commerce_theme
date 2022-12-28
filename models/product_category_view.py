from odoo import models, fields


class ProductCategoryView(models.Model):
    _name = 'product.category.view'
    _description = 'Product Category View'

    category_name = fields.Char()
    related_category = fields.Many2one("product.category", string='Related Category')
    description = fields.Text()
    image = fields.Binary()
