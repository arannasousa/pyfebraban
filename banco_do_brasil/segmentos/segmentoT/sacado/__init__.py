# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.segmentos.segmentoT import sacado

from .inscricao import Inscricao

class Sacado(sacado.Sacado):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'T'):

		super(Sacado, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.inscricao	= Inscricao(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
