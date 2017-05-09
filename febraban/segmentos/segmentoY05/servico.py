# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagCaracter, TagInteiro, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class Servico(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y'):
		super(Servico, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None, lote=None

		self.numero_registro	= TagInteiro(self._tipo_registro, u'04.5Y', u'numero_registro', 	  9,  13, descricao=u'*G038', comentario=u'Número do registro', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq, valor=self._num_seq)
		self.segmento			= TagCaracter(self._tipo_registro, u'05.5Y', u'segmento', 			 14,  14, descricao=u'*G039', comentario=u'Tipo do serviço', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq, valor=self._segmento)
		self.CNAB065Y 			= TagCaracter(self._tipo_registro, u'06.5Y', u'CNAB065Y', 			 15,  15, descricao=u'G034', comentario=u'Uso exclusivo FEBRABAN/CNAB', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.codigo_movimento	= TagInteiro(self._tipo_registro, u'07.5Y', u'codigo_movimento', 	 16,  17, descricao=u'*C004', comentario=u'Código de movimento remessa', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)

	def get_txt(self):

		txt = u''
		txt += self.numero_registro.txt
		txt += self.segmento.txt
		txt += self.CNAB065Y.txt
		txt += self.codigo_movimento.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.numero_registro.txt = arquivo
			self.segmento.txt = arquivo
			self.CNAB065Y.txt = arquivo
			self.codigo_movimento.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.numero_registro.alertas)
		alertas.extend(self.segmento.alertas)
		alertas.extend(self.CNAB065Y.alertas)
		alertas.extend(self.codigo_movimento.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.numero_registro.text)
		txt += gera_text(NIVEIS.N4, self.segmento.text)
		txt += gera_text(NIVEIS.N4, self.CNAB065Y.text)
		txt += gera_text(NIVEIS.N4, self.codigo_movimento.text)
		return txt

	text = property(get_text)