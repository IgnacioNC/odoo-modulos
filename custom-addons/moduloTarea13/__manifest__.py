# -*- coding: utf-8 -*-
{
    'name': "moduloTarea13",

    'summary': "Módulo tarea 13",

    'description': """
Descripción del módulo de la tarea 13 para extender el módulo hr.employee
    """,

    'author': "AllKeysHUB",
    'website': "127.0.0.1:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        "views/extended_hr_views.xml",
    ],
    'installable': True,
    'application': False
}
