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
from .... import TIPO_REGISTRO, NIVEIS, gera_text

class Celular(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y'):
		super(Celular, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None, lote=None
		self.ddd	= TagInteiro(self._tipo_registro, u'10.4Y', u'ddd',	 	 70,  71, descricao=u'*G032', comentario=u'Código DDD', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.numero	= TagInteiro(self._tipo_registro, u'11.4Y', u'numero',	 72,  79, descricao=u'*G032', comentario=u'Número do celular (envio de SMS)', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.ddd.txt
		txt += self.numero.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.ddd.txt = arquivo
			self.numero.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.ddd.alertas)
		alertas.extend(self.numero.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N4, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N5, self.ddd.text)
		txt += gera_text(NIVEIS.N5, self.numero.text)
		return txt

	text = property(get_text)