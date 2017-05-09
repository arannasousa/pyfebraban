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

from .inscricao import Inscricao

class SacadorAvalista(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Q'):
		super(SacadorAvalista, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.inscricao	= Inscricao(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nome		= TagCaracter(self._tipo_registro,	u'19.3Q', u'nome',	170, 209, descricao=u'G013', comentario=u'Nome do sacador/avalista', segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):
		txt = u''
		txt += self.inscricao.txt
		txt += self.nome.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.inscricao.txt = arquivo
			self.nome.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.inscricao.alertas)
		alertas.extend(self.nome.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += self.inscricao.text
		txt += gera_text(NIVEIS.N4, self.nome.text)
		return txt

	text = property(get_text)