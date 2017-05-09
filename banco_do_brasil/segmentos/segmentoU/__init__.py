# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.segmentos import segmentoU

from .controle import Controle
from .servico import Servico
from .dados_titulo import DadosTitulo
from .ocorrencia_sacado import OcorrenciaSacado

class SegmentoU(segmentoU.SegmentoU):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'U'):

		super(SegmentoU, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.controle			= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico			= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dados_titulo		= DadosTitulo(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		self.ocorrencia_sacado	= OcorrenciaSacado(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
