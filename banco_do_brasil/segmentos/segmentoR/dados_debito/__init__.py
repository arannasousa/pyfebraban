# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.segmentos.segmentoR import dados_debito

from .agencia import Agencia
from .conta_corrente import ContaCorrente

class DadosDebito(dados_debito.DadosDebito):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):

		super(DadosDebito, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.agencia	= Agencia(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta		= ContaCorrente(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
