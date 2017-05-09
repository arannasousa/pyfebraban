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

from .agencia import Agencia
from .conta_corrente import ContaCorrente

class DadosDebito(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):
		super(DadosDebito, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.banco		= TagInteiro(self._tipo_registro,	u'22.3R', u'banco',	208, 210, descricao=u'G001', comentario=u'Código do banco na conta do débito',	segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.agencia	= Agencia(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta		= ContaCorrente(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dv			= TagCaracter(self._tipo_registro,	u'27.3R', u'dv',	230, 230, descricao=u'*G012', comentario=u'Dígito verificador agencia/conta',	segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):
		txt = u''
		txt += self.banco.txt
		txt += self.agencia.txt
		txt += self.conta.txt
		txt += self.dv.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.banco.txt = arquivo
			self.agencia.txt = arquivo
			self.conta.txt = arquivo
			self.dv.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.banco.alertas)
		alertas.extend(self.agencia.alertas)
		alertas.extend(self.conta.alertas)
		alertas.extend(self.dv.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.banco.text)
		txt += self.agencia.text
		txt += self.conta.text
		txt += gera_text(NIVEIS.N4, self.dv.text)
		return txt

	text = property(get_text)