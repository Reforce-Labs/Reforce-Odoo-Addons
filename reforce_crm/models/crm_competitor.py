from odoo import fields, models

class Competitor(models.Model):
    """Model for defining competitors."""
    _name = 'crm.competitor'
    _description = 'Competitor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Competitor Name', required=True, tracking=True)
    currency_id = fields.Many2one('res.currency', 'Currency', tracking=True)
    revenue = fields.Monetary('Revenue', currency_field='currency_id', tracking=True)
    employees = fields.Integer('Employees', tracking=True)
    users = fields.Integer('Users', tracking=True)
    description = fields.Text('Description', tracking=True)
    website = fields.Char('Website', tracking=True)
    parent_company = fields.Char('Parent Company', tracking=True)
    email = fields.Char('Email', tracking=True)
    phone = fields.Char('Phone', tracking=True)
    street = fields.Char('Street', tracking=True)
    street2 = fields.Char('Street2', tracking=True)
    city = fields.Char('City', tracking=True)
    state_id = fields.Many2one('res.country.state', 'State', tracking=True)
    country_id = fields.Many2one('res.country', 'Country', tracking=True)
    zip = fields.Char('Zip', tracking=True)
    contact_name = fields.Char('Contact Name', tracking=True)
    contact_phone = fields.Char('Contact Phone', tracking=True)
    contact_email = fields.Char('Contact Email', tracking=True)
    contact_job_title = fields.Char('Contact Job Title', tracking=True)
    note = fields.Text('Notes')
    active = fields.Boolean('Active', default=True)
    image = fields.Binary('Image')
    image_medium = fields.Binary('Medium-sized image')
    image_small = fields.Binary('Small-sized image')
    image_url = fields.Char('Image URL')
    sequence = fields.Integer('Sequence', default=10)
    color = fields.Integer('Color Index')
    product_line_ids = fields.One2many('crm.product', 'competitor_id', string='Products')
    strengths = fields.Text('Strengths', tracking=True)
    weaknesses = fields.Text('Weaknesses', tracking=True)    
