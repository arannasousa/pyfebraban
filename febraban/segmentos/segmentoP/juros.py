# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagInteiro, TagData, TagDecimal, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class Juros(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'P'):
		super(Juros, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.codigo_juros_mora		= TagInteiro(self._tipo_registro, 	u'27.3P', u'codigo_juros_mora',	118, 118, descricao=u'*C018', comentario=u'Código do juros de mora', 	segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.data_juros_mora		= TagData(self._tipo_registro, 		u'28.3P', u'data_juros_mora',	119, 126, descricao=u'*C019', comentario=u'Data do juros de mora', 		segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.juros_mora				= TagDecimal(self._tipo_registro, 	u'29.3P', u'juros_mora',		127, 141, descricao=u'C020', comentario=u'Juros de mora por dia/taxa', 	segmento=self._segmento, lote=self._lote, num_seq=num_seq, casas_decimais=2)

	def get_txt(self):
		txt = u''
		txt += self.codigo_juros_mora.txt
		txt += self.data_juros_mora.txt
		txt += self.juros_mora.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.codigo_juros_mora.txt = arquivo
			self.data_juros_mora.txt = arquivo
			self.juros_mora.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.codigo_juros_mora.alertas)
		alertas.extend(self.data_juros_mora.alertas)
		alertas.extend(self.juros_mora.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.codigo_juros_mora.text)
		txt += gera_text(NIVEIS.N4, self.data_juros_mora.text)
		txt += gera_text(NIVEIS.N4, self.juros_mora.text)
		return txt

	text = property(get_text)