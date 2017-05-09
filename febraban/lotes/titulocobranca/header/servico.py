# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....base import (TagCaracter, TagInteiro, TXT)
from .... import TIPO_REGISTRO, NIVEIS, gera_text, TIPO_SERVICO

class Servico(TXT):
	def __init__(self, lote=u'0001'):
		super(Servico, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None, lote=None

		self.operacao			= TagCaracter(self._tipo_registro, u'04.1', u'operacao', 		 9,  9, descricao=u'*G028', comentario=u'Tipo da operação', lote=self._lote)
		self.servico			= TagInteiro(self._tipo_registro, u'05.1', u'servico', 			10, 11, descricao=u'*G025', comentario=u'Tipo do serviço', lote=self._lote, valor=TIPO_SERVICO.COBRANCA)
		self.CNAB061			= TagCaracter(self._tipo_registro, u'06.1', u'CNAB061',			12, 13, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote)
		self.layout_lote		= TagInteiro(self._tipo_registro, u'07.1', u'layout_lote',		14, 16, descricao=u'*G030', comentario=u'Nº da versão do layout do lote', valor=047, lote=self._lote)

	def get_txt(self):

		txt = u''
		txt += self.operacao.txt
		txt += self.servico.txt
		txt += self.CNAB061.txt
		txt += self.layout_lote.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.operacao.txt = arquivo
			self.servico.txt = arquivo
			self.CNAB061.txt = arquivo
			self.layout_lote.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.operacao.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.CNAB061.alertas)
		alertas.extend(self.layout_lote.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.operacao.text)
		txt += gera_text(NIVEIS.N4, self.servico.text)
		txt += gera_text(NIVEIS.N4, self.CNAB061.text)
		txt += gera_text(NIVEIS.N4, self.layout_lote.text)
		return txt

	text = property(get_text)