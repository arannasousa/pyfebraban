# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.segmentos.segmentoQ import servico

class Servico(servico.Servico):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Q'):
		super(Servico, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)