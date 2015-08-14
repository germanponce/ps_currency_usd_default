# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################

{
    'name': 'Consulta de Tasa de Cambio USD',
    'version': '1',
    "author" : "German Ponce Dominguez",
    "category" : "Facturacion",
    'description': """

Este modulo modifica las tasas de cambio para los Dolares, consultando la pagina oficial http://www.cambiodolar.mx/
y obteniendo automaticamente el valor actual.

Es necesario instalar la libreria:
    - pyquery

En Linux ejecutamos:
    - sudo pip install pyquery


Nota: por el momento solo funciona con Dolares.

    """,
    "website" : "http://poncesoft.blogspot.com",
    "license" : "AGPL-3",
    "depends" : ["base",],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    "view.xml",
                    ],
    "installable" : True,
    "active" : False,
}
