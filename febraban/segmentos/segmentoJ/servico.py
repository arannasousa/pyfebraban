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

class Movimento(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'J'):
		super(Movimento, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None, lote=None

		self.tipo	= TagInteiro(self._tipo_registro, u'06.3J', u'tipo', 	15, 15, descricao=u'*G060', comentario=u'Tipo de movimento', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.codigo	= TagInteiro(self._tipo_registro, u'07.3J', u'codigo', 	16, 17, descricao=u'G061', comentario=u'Código da instrução p/ movimento', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)

	def get_txt(self):

		txt = u''
		txt += self.tipo.txt
		txt += self.codigo.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.tipo.txt = arquivo
			self.codigo.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.tipo.alertas)
		alertas.extend(self.codigo.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N4, unicode(__name__) + u'.Movimento' + u'\n')
		txt += gera_text(NIVEIS.N5, self.tipo.text)
		txt += gera_text(NIVEIS.N5, self.codigo.text)
		return txt

	text = property(get_text)


class Servico(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'J'):
		super(Servico, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None, lote=None

		self.numero_registro	= TagInteiro(self._tipo_registro, u'04.3J', u'numero_registro', 		 9, 13, descricao=u'*G038', comentario=u'Tipo da operação', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.segmento			= TagCaracter(self._tipo_registro, u'05.3J', u'segmento', 			14, 14, descricao=u'*G039', comentario=u'Tipo do serviço', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq, valor=self._segmento)
		self.movimento 			= Movimento(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):

		txt = u''
		txt += self.numero_registro.txt
		txt += self.segmento.txt
		txt += self.movimento.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.numero_registro.txt = arquivo
			self.segmento.txt = arquivo
			self.movimento.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.numero_registro.alertas)
		alertas.extend(self.segmento.alertas)
		alertas.extend(self.movimento.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.numero_registro.text)
		txt += gera_text(NIVEIS.N4, self.segmento.text)
		txt += self.movimento.text
		return txt

	text = property(get_text)