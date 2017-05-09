# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.lotes.titulocobranca.header import LoteHeader as LoteHeader_febraban

from .controle import Controle
from .servico import Servico
from .empresa import Empresa

class LoteHeader(LoteHeader_febraban):
	def __init__(self, lote=u'0001'):
		super(LoteHeader, self).__init__(lote=lote)

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.controle 			= Controle(lote=self._lote)
		self.servico			= Servico(lote=self._lote)
		self.empresa			= Empresa(lote=self._lote)
