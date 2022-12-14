from odoo import models, fields


class CyCities(models.Model):
    _name = 'cy.cities'
    _description = 'Cy Cities'

    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=?', country_id)]", string='City/State')
    description = fields.Text()
    image = fields.Binary()

