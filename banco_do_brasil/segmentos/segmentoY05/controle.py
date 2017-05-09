# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.base import (TagInteiro)
from ...constantes import CODIGO_BANCO

from ....febraban.segmentos.segmentoY05 import controle

class Controle(controle.Controle):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y'):

		super(Controle, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.banco		= TagInteiro(self._tipo_registro, u'01.5Y', u'banco', 1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', segmento=self._segmento, lote=self._lote, num_seq=num_seq, valor=CODIGO_BANCO)
