# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...febraban.header.arquivodados import ArquivoHeaderDados as ArquivoHeaderDados_febraban

from ...febraban.base import (TagData, TagHora, TagInteiro, TXT)
# from ...febraban import TIPO_REGISTRO, NIVEIS, gera_text

class ArquivoHeaderDados(ArquivoHeaderDados_febraban):
	def __init__(self):
		super(ArquivoHeaderDados, self).__init__()

		self.layout			= TagInteiro(self._tipo_registro, u'20.0', u'layout',		164, 166, descricao=u'*G019', comentario=u'Nº da versão do layout do arquivo', valor=u'083')
