# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...constantes import CODIGO_BANCO
from ....febraban.base import (TagInteiro)
from ....febraban.segmentos.segmentoS import controle

class Controle(controle.Controle):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'S'):

		super(Controle, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.banco		= TagInteiro(self._tipo_registro, u'01.3S', u'banco', 		1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', segmento=self._segmento, lote=self._lote, num_seq=num_seq, valor=CODIGO_BANCO)
