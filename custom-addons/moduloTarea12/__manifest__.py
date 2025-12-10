# -*- coding: utf-8 -*-
{
    'name': "moduloTarea12",

    'summary': "Módulo tarea 12",

    'description': """
Descripción del módulo de la tarea 12
    """,

    'author': "AllKeysHUB",
    'website': "127.0.0.1:8069",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/nomina_views.xml",
        "views/bonificacion_deduccion_views.xml",
        "views/declaracion_renta_views.xml",
        "views/menus.xml",
    ],
    'installable': True,
    'application': True
}
