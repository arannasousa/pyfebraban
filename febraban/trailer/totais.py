# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ..base import (TagInteiro, TXT)
from .. import TIPO_REGISTRO, NIVEIS, gera_text

class ArquivoTrailerTotais(TXT):
	def __init__(self):
		super(ArquivoTrailerTotais, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_TRAILER

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None

		self.qtd_lotes				= TagInteiro(self._tipo_registro, u'05.9', u'qtd_lotes', 				 18,  23, descricao=u'G049', comentario=u'Qtd de lotes do arquivo')
		self.qtd_registros			= TagInteiro(self._tipo_registro, u'06.9', u'qtd_registros', 			 24,  29, descricao=u'G056', comentario=u'Qtd de registros do arquivo')
		self.qtd_contas_conciliacao	= TagInteiro(self._tipo_registro, u'07.9', u'qtd_contas_conciliacao',	 30,  35, descricao=u'*G037', comentario=u'Qtd de contas p/ concililiação (lotes)')


	def get_txt(self):

		txt = u''
		txt += self.qtd_lotes.txt
		txt += self.qtd_registros.txt
		txt += self.qtd_contas_conciliacao.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.qtd_lotes.txt = arquivo
			self.qtd_registros.txt = arquivo
			self.qtd_contas_conciliacao.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.qtd_lotes.alertas)
		alertas.extend(self.qtd_registros.alertas)
		alertas.extend(self.qtd_contas_conciliacao.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N3, self.qtd_lotes.text)
		txt += gera_text(NIVEIS.N3, self.qtd_registros.text)
		txt += gera_text(NIVEIS.N3, self.qtd_contas_conciliacao.text)
		return txt

	text = property(get_text)