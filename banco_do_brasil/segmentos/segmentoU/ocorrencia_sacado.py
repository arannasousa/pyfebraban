# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.base import (TagCaracter)
from ....febraban.segmentos.segmentoU import ocorrencia_sacado

class OcorrenciaSacado(ocorrencia_sacado.OcorrenciaSacado):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'U'):

		super(OcorrenciaSacado, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		# nao informado e passa a ser CHAR
		self.data = TagCaracter(self._tipo_registro, u'19.3U', u'data',	158, 165, descricao=u'C058', comentario=u'Data da ocorrência', 	segmento=self._segmento, lote=self._lote, num_seq=num_seq)
