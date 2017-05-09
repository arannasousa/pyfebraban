# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban import NIVEIS, gera_text

from .....febraban.segmentos.segmentoP import conta_corrente

from .agencia import Agencia
from .conta import Conta

class ContaCorrente(conta_corrente.ContaCorrente):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'P'):
		super(ContaCorrente, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.agencia	= Agencia(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta		= Conta(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.agencia.txt
		txt += self.conta.txt
		txt += self.dv.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.agencia.txt = arquivo
			self.conta.txt = arquivo
			self.dv.txt = arquivo

	txt = property(get_txt, set_txt)
