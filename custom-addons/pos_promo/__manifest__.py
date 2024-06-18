# -*- coding: utf-8 -*-
{
    'name': "POS Promos",

    'summary': """pos product promotions""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Eric Waweru",
    'website': "https://www.yourcompany.com",
    'license': 'LGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '16.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_promo/static/src/js/*',
            'pos_promo/static/src/xml/*',
        ],
    }
}
