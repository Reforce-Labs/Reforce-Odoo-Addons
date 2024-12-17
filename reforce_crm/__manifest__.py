{
    'name': 'Reforce CRM Extensions',
    'version': '1.0',
    'author': 'Reforce Labs',
    'depends': ['crm', 'mail'],
    'application': False,
    'auto_install': True,
    "data": [
        'security/ir.model.access.csv',
        'views/crm_product_views.xml',
        'views/view_tree_crm_competitors.xml',
        'views/action_reforce_crm_competitors.xml',
        'views/action_crm_product.xml',
        'views/crm.xml',
    ]
}