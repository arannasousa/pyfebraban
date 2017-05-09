# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.base import (TagCaracter, TagData, TagDecimal, TagHora, TagInteiro, TXT)
from .....febraban.lotes.titulocobranca.trailer import controle
from ....constantes import CODIGO_BANCO

class Controle(controle.Controle):
	def __init__(self, lote=u'0001'):
		super(Controle, self).__init__(lote=lote)

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None

		self.banco		= TagInteiro(self._tipo_registro, u'01.5', u'banco', 	1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', lote=self._lote, valor=CODIGO_BANCO)