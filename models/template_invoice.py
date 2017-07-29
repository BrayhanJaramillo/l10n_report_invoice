# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2017  Brayhan Jaramillo                                       #
#                     brayhanjaramillo@hotmail.com        					  #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from openerp import api, fields, models

import pprint
from openerp.exceptions import UserError, ValidationError
from openerp.tools.translate import _
from openerp.tools import float_is_zero, float_compare
from openerp.tools.misc import formatLang
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class Template_invoice(models.Model):

	_description = 'Modelo que permite la creacion de plantillas para mensajes en las facturas de los clientes'
	_name = 'template.invoice'
	_rec_name='name'

	name = fields.Char('Nombre Plantilla', required=True, help="Nombre de la plantilla, la cual es laquese escogera en la factura para la impresion de la misma.")
	description = fields.Text('Descripcón de la Plantilla', required=True, help="Descripción de la plantilla, la cual es la que saldra en la impresion del reporte.")
	
	@api.constrains('name')
	def chequear_hora(self):
		_logger.info(self)
		_logger.info(self.name)