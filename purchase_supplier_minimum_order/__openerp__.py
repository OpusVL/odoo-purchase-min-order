# -*- coding: utf-8 -*-

##############################################################################
#
# Set minimum order on suppliers
# Copyright (C) 2016 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Set minimum order on suppliers',
    'version': '0.1',
    'author': 'OpusVL',
    'website': 'http://opusvl.com/',
    'summary': 'Disallow confirmation of PO with minimum purchase order smaller than defined value for supplier',
    
    'category': 'Purchasing',
    
    'description': """Disallow confirmation of PO with minimum purchase order smaller than defined value for supplier.

    You can switch this into advisory mode for your company from the Configuration tab of
    Settings -> Your Company
""",
    'images': [
    ],
    'depends': [
        'base',
        'purchase',
    ],
    'data': [
        'views/res_company.xml',
        'views/res_partner.xml',
        'views/purchase.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
