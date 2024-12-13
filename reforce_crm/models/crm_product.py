from odoo import fields, models

class CrmProduct(models.Model):
    """Model for competitor products."""
    _name = 'crm.product'
    _description = 'Competitor Product'

    name = fields.Char('Product Name', required=True)
    competitor_id = fields.Many2one('crm.competitor', 'Competitor', required=True, ondelete='cascade')
    list_price = fields.Float('List Price')
    url = fields.Char('Product URL')
    strengths = fields.Text('Strengths')
    weaknesses = fields.Text('Weaknesses')
    description = fields.Text('Description')
    notes = fields.Text('Internal Notes')
    active = fields.Boolean('Active', default=True) 