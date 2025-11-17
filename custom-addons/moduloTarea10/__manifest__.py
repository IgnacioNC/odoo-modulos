# -*- coding: utf-8 -*-
{
    'name': "moduloTarea10",

    'summary': "Módulo tarea 10",

    'description': """
Descripción del módulo de la tarea 10
    """,

    'author': "AllKeysHUB",
    'website': "127.0.0.1:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True
}

