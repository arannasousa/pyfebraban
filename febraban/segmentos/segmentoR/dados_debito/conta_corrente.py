# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....base import (TagInteiro, TagCaracter, TXT)
from .... import TIPO_REGISTRO, NIVEIS, gera_text

class ContaCorrente(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):
		super(ContaCorrente, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.conta	= TagInteiro(self._tipo_registro,	u'25.3R', u'conta',	217,  228, descricao=u'*G010', comentario=u'Conta corrente para débito',	segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.dv		= TagCaracter(self._tipo_registro,	u'26.3R', u'dv',	229,  229, descricao=u'*G011', comentario=u'Dígito verificador da conta',	segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):
		txt = u''
		txt += self.conta.txt
		txt += self.dv.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.conta.txt = arquivo
			self.dv.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.conta.alertas)
		alertas.extend(self.dv.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N4, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N5, self.conta.text)
		txt += gera_text(NIVEIS.N5, self.dv.text)
		return txt

	text = property(get_text)