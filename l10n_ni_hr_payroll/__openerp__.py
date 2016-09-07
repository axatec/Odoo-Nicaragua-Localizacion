# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Nómina Nicaragua',
    'version' : '1.0',
    'summary': 'Liquidación de nómina - Nicaragua',
    'description': """
Este modulo permite:
=================================================================
Modifica la liquidación de nómina en Odoo para adaptarla a la
legislación vigente en Nicaragua. 
""",
    'category' : 'Localization',
    'author' : '3Nodus SAS',
    'website': 'http://www.3nodus.com/',
    'license': 'AGPL-3',
    'depends' : ['hr_payroll_account'],
    'data' : [              
				'views/hr_payroll_account_view.xml',
              ],
    "js": [
        "static/src/js/search.js",
    ],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
