# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....constantes import CODIGO_BANCO
from .....febraban.base import (TagInteiro)
from .....febraban.lotes.titulocobranca.header.controle import Controle as Controle_febraban

class Controle(Controle_febraban):
	def __init__(self, lote=u'0001'):
		super(Controle, self).__init__(lote=lote)

		self.banco		= TagInteiro(self._tipo_registro, u'01.1', u'banco', 	1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', lote=self._lote, valor=CODIGO_BANCO)
