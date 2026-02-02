# -*- coding: utf-8 -*-
{
    'name': "moduloTarea14",

    'summary': "Módulo tarea 14",

    'description': """
Descripción del módulo de la tarea 14 para la gestión de una guardería para empleados.
    """,

    'author': "AllKeysHUB",
    'website': "127.0.0.1:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr', 'event'],

    # always loaded
    'data': [
        "views/guarderia_views.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
    'application': True
}
