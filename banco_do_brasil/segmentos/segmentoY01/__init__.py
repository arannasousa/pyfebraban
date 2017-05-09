# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.segmentos import segmentoY01

from .controle import Controle
from .servico import Servico
from .sacador import Sacador

class SegmentoY01(segmentoY01.SegmentoY01):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y', seg_opcional=u'01'):

		super(SegmentoY01, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento, seg_opcional=seg_opcional)

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		self.sacador				= Sacador(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)


	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro and \
				unicode(self.codigo_registro_opcional.valor).zfill(2) == self._codigo_registro_opcional