# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.segmentos.segmentoR import desc3

class Desconto3(desc3.Desconto3):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):

		super(Desconto3, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)