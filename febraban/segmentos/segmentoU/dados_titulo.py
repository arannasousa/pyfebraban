# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagDecimal, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class DadosTitulo(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'U'):
		super(DadosTitulo, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.acrescimos			= TagDecimal(self._tipo_registro, 	u'08.3U', u'acrescimos',  		 18,  32, descricao=u'C048', comentario=u'Juros/Multa/Encargos',				 	casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor_desconto		= TagDecimal(self._tipo_registro, 	u'09.3U', u'valor_desconto', 	 33,  47, descricao=u'C049', comentario=u'Valor do desconto', 						casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor_abatimento	= TagDecimal(self._tipo_registro,	u'10.3U', u'valor_abatimento',	 48,  62, descricao=u'C050', comentario=u'Valor do abatimento concedido/cancelado',	casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor_iof			= TagDecimal(self._tipo_registro,	u'11.3U', u'valor_iof',  		 63,  77, descricao=u'G077', comentario=u'Valor do IOF recolhido',	 				casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor_pago			= TagDecimal(self._tipo_registro,	u'12.3U', u'valor_pago',  		 78,  92, descricao=u'C052', comentario=u'Valor pago pelo sacado', 					casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor_liquido		= TagDecimal(self._tipo_registro,	u'13.3U', u'valor_liquido',		 93, 107, descricao=u'G078', comentario=u'Valor líquido a ser creditado', 			casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)


	def get_txt(self):

		txt = u''
		txt += self.acrescimos.txt
		txt += self.valor_desconto.txt
		txt += self.valor_abatimento.txt
		txt += self.valor_iof.txt
		txt += self.valor_pago.txt
		txt += self.valor_liquido.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.acrescimos.txt = arquivo
			self.valor_desconto.txt = arquivo
			self.valor_abatimento.txt = arquivo
			self.valor_iof.txt = arquivo
			self.valor_pago.txt = arquivo
			self.valor_liquido.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.acrescimos.alertas)
		alertas.extend(self.valor_desconto.alertas)
		alertas.extend(self.valor_abatimento.alertas)
		alertas.extend(self.valor_iof.alertas)
		alertas.extend(self.valor_pago.alertas)
		alertas.extend(self.valor_liquido.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.acrescimos.text)
		txt += gera_text(NIVEIS.N4, self.valor_desconto.text)
		txt += gera_text(NIVEIS.N4, self.valor_abatimento.text)
		txt += gera_text(NIVEIS.N4, self.valor_iof.text)
		txt += gera_text(NIVEIS.N4, self.valor_pago.text)
		txt += gera_text(NIVEIS.N4, self.valor_liquido.text)
		return txt

	text = property(get_text)