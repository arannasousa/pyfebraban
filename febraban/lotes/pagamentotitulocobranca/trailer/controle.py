# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....base import (TagCaracter, TagData, TagDecimal, TagHora, TagInteiro, TXT)
from .... import TIPO_REGISTRO, NIVEIS, gera_text

class Controle(TXT):
	def __init__(self, lote=u'0001'):
		super(Controle, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_TRAILER

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None

		self.banco		= TagInteiro(self._tipo_registro, u'01.5', u'banco', 	1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', lote=self._lote)
		self.lote		= TagInteiro(self._tipo_registro, u'02.5', u'lote', 	4, 7, descricao=u'*G002', comentario=u'Lote de serviço', valor=self._lote, lote=self._lote)
		self.registro	= TagInteiro(self._tipo_registro, u'03.5', u'registro',	8, 8, descricao=u'*G003', comentario=u'Tipo de serviço', valor=TIPO_REGISTRO.LOTE_HEADER, lote=self._lote)

	def get_txt(self):

		txt = u''
		txt += self.banco.txt
		txt += self.lote.txt
		txt += self.registro.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.banco.txt = arquivo
			self.lote.txt = arquivo
			self.registro.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.banco.alertas)
		alertas.extend(self.lote.alertas)
		alertas.extend(self.registro.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.banco.text)
		txt += gera_text(NIVEIS.N4, self.lote.text)
		txt += gera_text(NIVEIS.N4, self.registro.text)
		return txt

	text = property(get_text)