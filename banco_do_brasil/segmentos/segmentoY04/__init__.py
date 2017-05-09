# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.segmentos import segmentoY04

from .controle import Controle
from .servico import Servico
from .dados_destinatario import DadosDestinatario

class SegmentoY04(segmentoY04.SegmentoY04):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y', seg_opcional=u'03'):

		super(SegmentoY04, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento, seg_opcional=seg_opcional)

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		self.dados_destinatario		= DadosDestinatario(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
