# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################

from openerp import models, fields, api, _
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
from datetime import time, datetime
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.osv import osv, fields, expression
from openerp.tools.translate import _


from pyquery import PyQuery as pq


class res_currency(models.Model):
    _name = 'res.currency'
    _inherit ='res.currency'
    _columns = {
        }

    _defaults = {
        }

class insert_currency_act(osv.osv_memory):
    _name = 'insert.currency.act'
    _description = 'Descripcion del Wizard'
    _columns = {
        'currency_default': fields.text('Tasa de Cambio'),
    }
    def _get_currency(self, cr, uid, context=None):
        result =""
        jquery = pq(url="http://www.cambiodolar.mx/") #obtenemos todo el html y lo asignamos a la variable jquery
        currency = jquery('div.valor').text() #imprime el texto del div que tiene la clase "valor" 
        date_act = jquery('p.day').text() # imprime el texto de la etiqueta p que tiene la clase "day"
        result = currency+"\n"+date_act
        return result

    _defaults = {  
        'currency_default': _get_currency,
        }

    def exec_currency(self, cr, uid, ids, context=None):
        jquery = pq(url="http://www.cambiodolar.mx/") #obtenemos todo el html y lo asignamos a la variable jquery
        currency = jquery('div.valor').text()
        active_ids = context['active_ids']
        date_act = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        currency_rep = currency.replace('1 Dolar = $','').replace('Pesos Mexicanos','').replace(' ','').replace(',','.')
        currency_br = self.pool.get('res.currency').browse(cr, uid, active_ids, context=None)[0]
        if currency_br.name.upper() != 'USD':
            raise osv.except_osv('Error!', 
                'Por el momento solo funciona para Dolares (USD).\nDisculpa las Molestias :( ')

        try:
            rate = 1/ float(currency_rep)
        except:
            rate = 0.0
        vals = {
        'name': date_act,
        'rate': rate,
        'currency_id': active_ids[0],
        }
        currency_rate = self.pool.get('res.currency.rate').create(cr, uid, vals, context=None)
        return True

