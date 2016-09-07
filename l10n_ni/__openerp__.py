# -*- coding: utf-8 -*-

{
    'name': 'Nicaraguan - Accounting',
    'version': '0.1',
    'category': 'Localization/Account Charts',
    'description': """
Nicaraguan Accounting and Tax Preconfiguration:
=================================================================
""",
    'author': '3Nodus SAS',
    'depends': [
        'account',
        'base_vat',
        'account_chart',
    ],
    'data': [
        'data/account.account.type.csv',
        'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'data/account_chart_template.xml',
        'data/account.tax.template.csv',
        'wizard/account_wizard.xml',
    ],
    'demo': [],
    'installable': True,
}
