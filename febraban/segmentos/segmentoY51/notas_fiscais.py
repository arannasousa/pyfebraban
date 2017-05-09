# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagCaracter, TagDecimal, TagData, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class NotasFiscais(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y'):
		super(NotasFiscais, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.nf1				= TagCaracter(self._tipo_registro, 	u'09.3Y', u'nf1', 				 20,  34, descricao=u'C067', comentario=u'Número da nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf1_valor			= TagDecimal(self._tipo_registro, 	u'10.3Y', u'nf1_valor',			 35,  49, descricao=u'C068', comentario=u'Valor da nota fiscal', casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf1_data_emissao	= TagData(self._tipo_registro, 		u'11.3Y', u'nf1_data_emissao', 	 50,  57, descricao=u'C069', comentario=u'Data emissão nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf2				= TagCaracter(self._tipo_registro, 	u'12.3Y', u'nf2', 				 58,  72, descricao=u'C067', comentario=u'Número da nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf2_valor			= TagDecimal(self._tipo_registro, 	u'13.3Y', u'nf2_valor',			 73,  87, descricao=u'C068', comentario=u'Valor da nota fiscal', casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf2_data_emissao	= TagData(self._tipo_registro, 		u'14.3Y', u'nf2_data_emissao', 	 88,  95, descricao=u'C069', comentario=u'Data emissão nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf3				= TagCaracter(self._tipo_registro, 	u'15.3Y', u'nf3', 				 96, 110, descricao=u'C067', comentario=u'Número da nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf3_valor			= TagDecimal(self._tipo_registro, 	u'16.3Y', u'nf3_valor',			111, 125, descricao=u'C068', comentario=u'Valor da nota fiscal', casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf3_data_emissao	= TagData(self._tipo_registro, 		u'17.3Y', u'nf3_data_emissao', 	126, 133, descricao=u'C069', comentario=u'Data emissão nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf4				= TagCaracter(self._tipo_registro, 	u'18.3Y', u'nf4', 				134, 148, descricao=u'C067', comentario=u'Número da nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf4_valor			= TagDecimal(self._tipo_registro, 	u'19.3Y', u'nf4_valor',			149, 163, descricao=u'C068', comentario=u'Valor da nota fiscal', casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf4_data_emissao	= TagData(self._tipo_registro, 		u'20.3Y', u'nf4_data_emissao', 	164, 171, descricao=u'C069', comentario=u'Data emissão nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf5				= TagCaracter(self._tipo_registro, 	u'21.3Y', u'nf5', 				172, 186, descricao=u'C067', comentario=u'Número da nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf5_valor			= TagDecimal(self._tipo_registro, 	u'22.3Y', u'nf5_valor',			187, 201, descricao=u'C068', comentario=u'Valor da nota fiscal', casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.nf5_data_emissao	= TagData(self._tipo_registro, 		u'23.3Y', u'nf5_data_emissao', 	202, 209, descricao=u'C069', comentario=u'Data emissão nota fiscal', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.nf1.txt
		txt += self.nf1_valor.txt
		txt += self.nf1_data_emissao.txt
		txt += self.nf2.txt
		txt += self.nf2_valor.txt
		txt += self.nf2_data_emissao.txt
		txt += self.nf3.txt
		txt += self.nf3_valor.txt
		txt += self.nf3_data_emissao.txt
		txt += self.nf4.txt
		txt += self.nf4_valor.txt
		txt += self.nf4_data_emissao.txt
		txt += self.nf5.txt
		txt += self.nf5_valor.txt
		txt += self.nf5_data_emissao.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.nf1.txt = arquivo
			self.nf1_valor.txt = arquivo
			self.nf1_data_emissao.txt = arquivo
			self.nf2.txt = arquivo
			self.nf2_valor.txt = arquivo
			self.nf2_data_emissao.txt = arquivo
			self.nf3.txt = arquivo
			self.nf3_valor.txt = arquivo
			self.nf3_data_emissao.txt = arquivo
			self.nf4.txt = arquivo
			self.nf4_valor.txt = arquivo
			self.nf4_data_emissao.txt = arquivo
			self.nf5.txt = arquivo
			self.nf5_valor.txt = arquivo
			self.nf5_data_emissao.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.nf1.alertas)
		alertas.extend(self.nf1_valor.alertas)
		alertas.extend(self.nf1_data_emissao.alertas)
		alertas.extend(self.nf2.alertas)
		alertas.extend(self.nf2_valor.alertas)
		alertas.extend(self.nf2_data_emissao.alertas)
		alertas.extend(self.nf3.alertas)
		alertas.extend(self.nf3_valor.alertas)
		alertas.extend(self.nf3_data_emissao.alertas)
		alertas.extend(self.nf4.alertas)
		alertas.extend(self.nf4_valor.alertas)
		alertas.extend(self.nf4_data_emissao.alertas)
		alertas.extend(self.nf5.alertas)
		alertas.extend(self.nf5_valor.alertas)
		alertas.extend(self.nf5_data_emissao.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.nf1.text)
		txt += gera_text(NIVEIS.N4, self.nf1_valor.text)
		txt += gera_text(NIVEIS.N4, self.nf1_data_emissao.text)
		txt += gera_text(NIVEIS.N4, self.nf2.text)
		txt += gera_text(NIVEIS.N4, self.nf2_valor.text)
		txt += gera_text(NIVEIS.N4, self.nf2_data_emissao.text)
		txt += gera_text(NIVEIS.N4, self.nf3.text)
		txt += gera_text(NIVEIS.N4, self.nf3_valor.text)
		txt += gera_text(NIVEIS.N4, self.nf3_data_emissao.text)
		txt += gera_text(NIVEIS.N4, self.nf4.text)
		txt += gera_text(NIVEIS.N4, self.nf4_valor.text)
		txt += gera_text(NIVEIS.N4, self.nf4_data_emissao.text)
		txt += gera_text(NIVEIS.N4, self.nf5.text)
		txt += gera_text(NIVEIS.N4, self.nf5_valor.text)
		txt += gera_text(NIVEIS.N4, self.nf5_data_emissao.text)
		return txt

	text = property(get_text)