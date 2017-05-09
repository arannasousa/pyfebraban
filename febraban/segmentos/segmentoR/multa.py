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

class Multa(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):
		super(Multa, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.codigo	= TagInteiro(self._tipo_registro,	u'14.3R', u'codigo', 66,  66, descricao=u'G073', comentario=u'Código da multa', segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.data	= TagData(self._tipo_registro,		u'15.3R', u'data',	 67,  74, descricao=u'G074', comentario=u'Data da multa', segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.multa	= TagDecimal(self._tipo_registro,	u'16.3R', u'multa',	 75,  89, descricao=u'G075', comentario=u'Valor/percentual a ser aplicado', casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):
		txt = u''
		txt += self.codigo.txt
		txt += self.data.txt
		txt += self.multa.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.codigo.txt = arquivo
			self.data.txt = arquivo
			self.multa.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.codigo.alertas)
		alertas.extend(self.data.alertas)
		alertas.extend(self.multa.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.codigo.text)
		txt += gera_text(NIVEIS.N4, self.data.text)
		txt += gera_text(NIVEIS.N4, self.multa.text)
		return txt

	text = property(get_text)