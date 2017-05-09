# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.segmentos.segmentoP import desc1

class Desc1(desc1.Desc1):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'P'):
		super(Desc1, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)
