from odoo import fields, models

class Competitor(models.Model):
    """Model for defining competitors."""
    _name = 'crm.competitor'
    _description = 'Competitor'

    name = fields.Char('Competitor Name', required=True)
    description = fields.Text('Description')
    website = fields.Char('Website')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    city = fields.Char('City')
    state_id = fields.Many2one('res.country.state', 'State')
    country_id = fields.Many2one('res.country', 'Country')
    zip = fields.Char('Zip')
    contact_name = fields.Char('Contact Name')
    contact_phone = fields.Char('Contact Phone')
    contact_email = fields.Char('Contact Email')
    contact_job_title = fields.Char('Contact Job Title')
    note = fields.Text('Notes')
    active = fields.Boolean('Active', default=True)
    image = fields.Binary('Image')
    image_medium = fields.Binary('Medium-sized image')
    image_small = fields.Binary('Small-sized image')
    image_url = fields.Char('Image URL')
    sequence = fields.Integer('Sequence', default=10)
    color = fields.Integer('Color Index')
    product_line_ids = fields.One2many('crm.product', 'competitor_id', string='Products')
    strengths = fields.Text('Strengths')
    weaknesses = fields.Text('Weaknesses')    