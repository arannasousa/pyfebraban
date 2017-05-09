# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagInteiro, TagDecimal, TagCaracter, TagData, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class OcorrenciaSacado(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'U'):
		super(OcorrenciaSacado, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.codigo			= TagCaracter(self._tipo_registro, 	u'18.3U', u'codigo', 		154, 157, descricao=u'*A001', comentario=u'Código da ocorrência',				 segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.data			= TagData(self._tipo_registro, 		u'19.3U', u'data',			158, 165, descricao=u'C058', comentario=u'Data da ocorrência', 					 segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor 			= TagDecimal(self._tipo_registro, 	u'20.3U', u'valor', 		166, 180, descricao=u'C059', comentario=u'Valor da ocorrência',	casas_decimais=2, segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.complemento 	= TagCaracter(self._tipo_registro,	u'21.3U', u'complemento',	181, 210, descricao=u'*A002', comentario=u'Complemento da ocorrência', 			 segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):

		txt = u''
		txt += self.codigo.txt
		txt += self.data.txt
		txt += self.valor.txt
		txt += self.complemento.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.codigo.txt = arquivo
			self.data.txt = arquivo
			self.valor.txt = arquivo
			self.complemento.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.codigo.alertas)
		alertas.extend(self.data.alertas)
		alertas.extend(self.valor.alertas)
		alertas.extend(self.complemento.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.codigo.text)
		txt += gera_text(NIVEIS.N4, self.data.text)
		txt += gera_text(NIVEIS.N4, self.valor.text)
		txt += gera_text(NIVEIS.N4, self.complemento.text)
		return txt

	text = property(get_text)