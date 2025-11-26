# -*- coding: utf-8 -*-
{
    'name': "moduloTarea11",

    'summary': "Módulo tarea 11",

    'description': """
Descripción del módulo de la tarea 11
    """,

    'author': "AllKeysHUB",
    'website': "127.0.0.1:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'scurity/ir.model.access.csv'
        'security/security.xml',
        #'security/access_rights.xml',
        'views/ordenadores_view.xml',
        #'views/componentes_view.xml'
    ],
    'installable': True,
    'application': True
}
