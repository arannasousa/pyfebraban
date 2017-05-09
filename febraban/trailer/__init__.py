# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ..base import (TagCaracter, TXT)
from .. import TIPO_REGISTRO, NIVEIS, gera_text

from .controle import ArquivoTrailerControle
from .totais import ArquivoTrailerTotais

class ArquivoTrailer(TXT):
	def __init__(self):
		super(ArquivoTrailer, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_TRAILER

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.controle 	= ArquivoTrailerControle()
		self.CNAB040	= TagCaracter(self._tipo_registro,  u'04.9', u'CNAB040', 	  9, 17, descricao=u'G004', comentario=u'CNAB')
		self.totais		= ArquivoTrailerTotais()
		self.CNAB089	= TagCaracter(self._tipo_registro,  u'08.9', u'CNAB089', 	36, 240, descricao=u'G004', comentario=u'CNAB')


	def get_txt(self):

		txt = u''
		txt += self.controle.txt
		txt += self.CNAB040.txt
		txt += self.totais.txt
		txt += self.CNAB089.txt
		txt += '\n'

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.CNAB040.txt = arquivo
			self.totais.txt = arquivo
			self.CNAB089.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.CNAB040.alertas)
		alertas.extend(self.totais.alertas)
		alertas.extend(self.CNAB089.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N1, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += gera_text(NIVEIS.N2, self.CNAB040.text)
		txt += self.totais.text
		txt += gera_text(NIVEIS.N2, self.CNAB089.text)
		return txt

	text = property(get_text)