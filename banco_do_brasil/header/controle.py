# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...febraban.header.controle import ArquivoHeaderControle as ArquivoHeaderControle_febraban

from ...febraban.base import (TagInteiro, TXT)
from ...febraban import TIPO_REGISTRO, NIVEIS, gera_text

class ArquivoHeaderControle(ArquivoHeaderControle_febraban):
	def __init__(self):
		super(ArquivoHeaderControle, self).__init__()

		self.banco		= TagInteiro(self._tipo_registro, u'01.0', u'banco', 	1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', valor=u'001')