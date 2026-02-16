# -*- coding: utf-8 -*-
{
    'name': "Reportes",

    'summary': "Impresora de reportes en PDF",


    'author': "My Company",
    'depends': ['base', 'sale'],

    'data': [
        'reports/sale_report.xml',
        'reports/sale_report_action.xml',
        'reports/sale_report_inherit.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}

