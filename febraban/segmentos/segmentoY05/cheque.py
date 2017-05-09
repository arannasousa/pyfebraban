# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagCaracter, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class Cheque(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y'):
		super(Cheque, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.cmc7_cheque1 = TagCaracter(self._tipo_registro, u'09.5Y', u'cmc7_cheque1',  20,  53, descricao=u'C076', comentario=u'Identificação do cheque 1', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.cmc7_cheque2 = TagCaracter(self._tipo_registro, u'10.5Y', u'cmc7_cheque2',  54,  87, descricao=u'C076', comentario=u'Identificação do cheque 2', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.cmc7_cheque3 = TagCaracter(self._tipo_registro, u'11.5Y', u'cmc7_cheque3',  88, 121, descricao=u'C076', comentario=u'Identificação do cheque 3', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.cmc7_cheque4 = TagCaracter(self._tipo_registro, u'12.5Y', u'cmc7_cheque4', 122, 155, descricao=u'C076', comentario=u'Identificação do cheque 4', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.cmc7_cheque5 = TagCaracter(self._tipo_registro, u'13.5Y', u'cmc7_cheque5', 156, 189, descricao=u'C076', comentario=u'Identificação do cheque 5', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.cmc7_cheque6 = TagCaracter(self._tipo_registro, u'14.5Y', u'cmc7_cheque6', 190, 223, descricao=u'C076', comentario=u'Identificação do cheque 6', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)


	def get_txt(self):
		txt = u''
		txt += self.cmc7_cheque1.txt
		txt += self.cmc7_cheque2.txt
		txt += self.cmc7_cheque3.txt
		txt += self.cmc7_cheque4.txt
		txt += self.cmc7_cheque5.txt
		txt += self.cmc7_cheque6.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.cmc7_cheque1.txt = arquivo
			self.cmc7_cheque2.txt = arquivo
			self.cmc7_cheque3.txt = arquivo
			self.cmc7_cheque4.txt = arquivo
			self.cmc7_cheque5.txt = arquivo
			self.cmc7_cheque6.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.cmc7_cheque1.alertas)
		alertas.extend(self.cmc7_cheque2.alertas)
		alertas.extend(self.cmc7_cheque3.alertas)
		alertas.extend(self.cmc7_cheque4.alertas)
		alertas.extend(self.cmc7_cheque5.alertas)
		alertas.extend(self.cmc7_cheque6.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.cmc7_cheque1.text)
		txt += gera_text(NIVEIS.N4, self.cmc7_cheque2.text)
		txt += gera_text(NIVEIS.N4, self.cmc7_cheque3.text)
		txt += gera_text(NIVEIS.N4, self.cmc7_cheque4.text)
		txt += gera_text(NIVEIS.N4, self.cmc7_cheque5.text)
		txt += gera_text(NIVEIS.N4, self.cmc7_cheque6.text)
		return txt

	text = property(get_text)