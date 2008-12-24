# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
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
    "name" : "MRP Sub Product",
    "version" : "1.0",
    "author" : "Tiny",
    "website" : "http://www.openerp.com",
    "depends" : ["base","mrp"],
    "category" : "Generic Modules/Production",
    "init_xml" : [],
    "description": """
This module allows you to produce several products from one production order.
You can configure sub-products in the bill of material.
Without this module:
    A + B + C -> D
With this module:
    A + B + C -> D + E
    """,
    "demo_xml" : [],
    "update_xml" : [
        "mrp_subproduct_view.xml",
    ],
    "active": False,
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

