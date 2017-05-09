# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...febraban.base import (TagCaracter, TXT)
from ...febraban.trailer import ArquivoTrailer as ArquivoTrailer_febraban

from .controle import ArquivoTrailerControle

class ArquivoTrailer(ArquivoTrailer_febraban):
	def __init__(self):
		super(ArquivoTrailer, self).__init__()

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.controle 	= ArquivoTrailerControle()