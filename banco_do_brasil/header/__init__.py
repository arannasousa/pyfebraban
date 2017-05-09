# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'


from ...febraban.header import ArquivoHeader as ArquivoHeader_febraban

from ...febraban.base import (TagCaracter, TXT)
from ...febraban import TIPO_REGISTRO, NIVEIS, gera_text

from .controle import ArquivoHeaderControle
from .empresa import ArquivoHeaderEmpresa
from .arquivodados import ArquivoHeaderDados

class ArquivoHeader(ArquivoHeader_febraban):
	def __init__(self):
		super(ArquivoHeader, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.controle 	= ArquivoHeaderControle()
		self.empresa	= ArquivoHeaderEmpresa()
		self.nome_banco	= TagCaracter(self._tipo_registro, u'14.0', u'nome_banco',	103, 132, descricao=u'G014', comentario=u'Nome do banco', valor=u'BANCO DO BRASIL S.A.')
		self.arquivo 	= ArquivoHeaderDados()

