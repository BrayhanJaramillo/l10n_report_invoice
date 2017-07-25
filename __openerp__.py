# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 MARLON FALCON HDEZ (<http://www.marlonfalcon.cl>).
# contact: contacto@marlonfalcon.cl

######################################################################

{
    'name': 'Report odoo 9',
    'version': '1.0',
    'author': 'Brayhan Jaramillo',
    'category': 'Accounting & Finance',
    'summary': 'Personalizacion de facturas',
    'sequence': 30,
    'website': 'brayhanjaramillo@hotmail.com',
    'description': """
Modulo basico reporte cliente
======================
Con este modulo se podra personalizar la factura del cliente.
 * Imagenes
 * Tablas
    """,
    'license' : 'AGPL-3',
    'depends': ['sale','base_setup', 'product', 'analytic', 'report'],
    'data': [
        'cubareport_view.xml',
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
}	