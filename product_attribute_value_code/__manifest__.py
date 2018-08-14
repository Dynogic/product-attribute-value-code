# -*- coding: utf-8 -*-
{
    'name': "Product Attribute Value Code",

    'summary': "Adds a code to each product attribute value.",

    'description': "Adds a code to each product attribute value.",

    'author': "Testbench Technologies, Inc.",
    'website': "https://www.testbench.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}