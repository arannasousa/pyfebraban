# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.base import (TagInteiro)

from .....febraban.lotes.titulocobranca.header.servico import Servico as Servico_febraban

class Servico(Servico_febraban):
	def __init__(self, lote=u'0001'):
		super(Servico, self).__init__(lote=lote)

		self.layout_lote		= TagInteiro(self._tipo_registro, u'07.1', u'layout_lote',		14, 16, descricao=u'*G030', comentario=u'Nº da versão do layout do lote', valor=042, lote=self._lote)
