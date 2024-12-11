from odoo import models, fields

class ProjectTask(models.Model):

    _inherit = 'project.task'

    #----------------------------------------------------------
    # Fields
    #----------------------------------------------------------

    work_link = fields.Char(
        string='Work Link',
        help='Link to relevant commit, design, or other work',
        size=256,
        placeholder='Link...'
    )