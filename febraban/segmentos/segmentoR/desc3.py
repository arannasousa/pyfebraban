# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagData, TagDecimal, TagInteiro, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class Desconto3(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):
		super(Desconto3, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.codigo		= TagInteiro(self._tipo_registro,	u'11.3R', u'codigo',	 42,  42, descricao=u'*C021', comentario=u'Código do desconto 3', segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.data		= TagData(self._tipo_registro,		u'12.3R', u'data',		 43,  50, descricao=u'C022', comentario=u'Data do desconto 3', segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.desconto	= TagDecimal(self._tipo_registro,	u'13.3R', u'desconto',	 51,  65, descricao=u'C023', comentario=u'Valor/percentual a ser concedido', casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):
		txt = u''
		txt += self.codigo.txt
		txt += self.data.txt
		txt += self.desconto.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.codigo.txt = arquivo
			self.data.txt = arquivo
			self.desconto.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.codigo.alertas)
		alertas.extend(self.data.alertas)
		alertas.extend(self.desconto.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.codigo.text)
		txt += gera_text(NIVEIS.N4, self.data.text)
		txt += gera_text(NIVEIS.N4, self.desconto.text)
		return txt

	text = property(get_text)