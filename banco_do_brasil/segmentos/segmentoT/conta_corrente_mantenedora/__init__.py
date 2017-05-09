# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.segmentos.segmentoT import conta_corrente_mantenedora

from .agencia import Agencia
from .conta import Conta

class ContaCorrenteMantenedora(conta_corrente_mantenedora.ContaCorrenteMantenedora):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'T'):

		super(ContaCorrenteMantenedora, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.agencia	= Agencia(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta		= Conta(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
