# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'


from ....febraban.segmentos import segmentoY05

from .controle import Controle
from .servico import Servico
from .cheque import Cheque

class SegmentoY05(segmentoY05.SegmentoY05):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y', seg_opcional=u'04'):

		super(SegmentoY05, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento, seg_opcional=seg_opcional)

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		self.cheque					= Cheque(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
