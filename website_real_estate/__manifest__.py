# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2017 Acysos S.L. (http://acysos.com) All Rights Reserved.
#                       Daniel Pascal <daniel@acysos.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': "Real Estate Website",
    'category': 'Specific Industry Applications',
    'version': '1.0',
    'depends': ['base',
                'website',
                'website_crm',
                'base_geolocalize',
                'real_estate_base',
                'real_estate_internet_common',
                'base_multi_image',
                ],

    'data': [
        'views/featured_tops.xml',
        'views/top_view.xml',
        'views/tops_template.xml',
        'views/search_list.xml',
        'views/search_map.xml',
        'views/assets.xml',
        'security/ir.model.access.csv',
        'views/company_view.xml'
   ],

    'application':True,
    'author': "Acysos S.L.",
    'website': "www.acysos.com",
}
