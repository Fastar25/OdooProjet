# -*- coding: utf-8 -*-
{
    'name': "librairie",

    'summary': """ Mini Projet Application Gestion de bibliothèque """,

    'description': """Nous allons créer une nouvelle application Odoo pour gérer une bibliothèque de livres.  """,

    'author': "Papa Sidy Mactar TRAORE",
    'website': "https://linkedin.com/in/traoré",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/librairie_menu.xml',
        'security/librairie_security.xml',
        'views/livre_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
