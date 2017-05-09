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

class TotaisCobrancaVinculada(TXT):
	def __init__(self, lote=u'0001'):
		super(TotaisCobrancaVinculada, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_TRAILER

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None

		self.qtd	= TagInteiro(self._tipo_registro, u'08.5', u'qtd', 		47, 52, descricao=u'*C070', comentario=u'Quantidade de títulos em cobrança', lote=self._lote)
		self.valor	= TagDecimal(self._tipo_registro, u'09.5', u'valor', 	53, 69, casas_decimais=2, descricao=u'*C071', comentario=u'Valor total dos títulos em carteiras', lote=self._lote)

	def get_txt(self):
		txt = u''
		txt += self.qtd.txt
		txt += self.valor.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.qtd.txt = arquivo
			self.valor.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.qtd.alertas)
		alertas.extend(self.valor.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.qtd.text)
		txt += gera_text(NIVEIS.N4, self.valor.text)
		return txt

	text = property(get_text)