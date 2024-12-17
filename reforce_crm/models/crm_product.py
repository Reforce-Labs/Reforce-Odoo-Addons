from odoo import fields, models, api

class CrmProduct(models.Model):
    """Model for tracking products in the competitive landscape."""
    _name = 'crm.product'
    _description = 'Product Intelligence'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Product Name', required=True, tracking=True)
    company_id = fields.Many2one(
        'crm.competitor', 
        'Competitor', 
        tracking=True,
        ondelete='cascade'
    )
    is_competitor_product = fields.Boolean('Competitor Product', default=True, tracking=True)
    
    # Image
    image = fields.Image('Image', max_width=1920, max_height=1920)
    
    # Product Details
    description = fields.Text('Description', tracking=True)
    list_price = fields.Float('List Price', tracking=True)
    currency_id = fields.Many2one(
        'res.currency', 
        'Currency',
        default=lambda self: self.env.company.currency_id.id
    )
    url = fields.Char('Product URL', tracking=True)
    launch_date = fields.Date('Launch Date', tracking=True)
    
    # Market Analysis
    target_market = fields.Text('Target Market', tracking=True)
    key_features = fields.Text('Key Features', tracking=True)
    strengths = fields.Text('Strengths', tracking=True)
    weaknesses = fields.Text('Weaknesses', tracking=True)
    market_share = fields.Float('Market Share %', tracking=True)
    
    # Competitive Analysis
    competing_products_ids = fields.Many2many(
        'crm.product',
        'crm_product_competition_rel',
        'product_id',
        'competing_product_id',
        string='Competing Products',
        domain=[('is_competitor_product', '=', True)],
        tracking=True
    )
    
    competing_with_ids = fields.Many2many(
        'crm.product',
        'crm_product_competition_rel',
        'competing_product_id',
        'product_id',
        string='Competes With',
        domain=[('is_competitor_product', '=', False)],
        tracking=True
    )
    
    # Product Status
    status = fields.Selection([
        ('development', 'In Development'),
        ('beta', 'Beta'),
        ('released', 'Released'),
        ('maintenance', 'Maintenance'),
        ('eol', 'End of Life')
    ], string='Status', default='development', tracking=True)
    
    # Internal
    notes = fields.Text('Internal Notes')
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.company_id:
            self.is_competitor_product = True

    @api.onchange('is_competitor_product')
    def _onchange_is_competitor_product(self):
        if not self.is_competitor_product:
            self.company_id = False