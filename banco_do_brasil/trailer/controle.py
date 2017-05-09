# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...febraban.base import (TagInteiro, TXT)
from ...febraban.trailer.controle import ArquivoTrailerControle as ArquivoTrailerControle_febraban

class ArquivoTrailerControle(ArquivoTrailerControle_febraban):
	def __init__(self):
		super(ArquivoTrailerControle, self).__init__()

		self.banco = TagInteiro(self._tipo_registro, u'01.9', u'banco', 	1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', valor=u'001')
