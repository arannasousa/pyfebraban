# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....base import (TagDecimal, TagHora, TagInteiro, TXT)
from .... import TIPO_REGISTRO, NIVEIS, gera_text

class Totais(TXT):
	def __init__(self, lote=u'0001'):
		super(Totais, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_TRAILER

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None

		self.qtd_registros	= TagInteiro(self._tipo_registro, u'05.5', u'qtd_registros', 	18, 23, descricao=u'*G057', comentario=u'Quantidade de registros do lote', lote=self._lote)
		self.valor			= TagDecimal(self._tipo_registro, u'06.5', u'valor', 			24, 41, casas_decimais=2, descricao=u'L001', comentario=u'Somatória dos valores', lote=self._lote)
		self.qtd_moeda		= TagDecimal(self._tipo_registro, u'07.5', u'qtd_moeda',		42, 59, casas_decimais=5, descricao=u'G058', comentario=u'Somatória de quantidade de moedas', lote=self._lote)

	def get_txt(self):

		txt = u''
		txt += self.qtd_registros.txt
		txt += self.valor.txt
		txt += self.qtd_moeda.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.qtd_registros.txt = arquivo
			self.valor.txt = arquivo
			self.qtd_moeda.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.qtd_registros.alertas)
		alertas.extend(self.valor.alertas)
		alertas.extend(self.qtd_moeda.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.qtd_registros.text)
		txt += gera_text(NIVEIS.N4, self.valor.text)
		txt += gera_text(NIVEIS.N4, self.qtd_moeda.text)
		return txt

	text = property(get_text)