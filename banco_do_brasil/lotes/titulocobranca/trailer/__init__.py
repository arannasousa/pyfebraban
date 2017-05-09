# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.base import (TagCaracter, TXT, TagInteiro)
from .....febraban import TIPO_REGISTRO, NIVEIS, gera_text

from .....febraban.lotes.titulocobranca import trailer

from .controle import Controle
from .totais_cobranca_simples import TotaisCobrancaSimples
from .totais_cobranca_vinculada import TotaisCobrancaVinculada
from .totais_cobranca_caucionada import TotaisCobrancaCaucionada
from .totais_cobranca_descontada import TotaisCobrancaDescontada

class LoteTrailer(trailer.LoteTrailer):
	def __init__(self, lote=u'0001'):
		super(LoteTrailer, self).__init__(lote=lote)

		self.controle 				= Controle(lote=self._lote)

		# ----------------------------------------------------------------------------------------------------------------
		# no manual do BB, informa que o campo 06.5 exclusivo da FEBRABAN começa de 24 até 240 do tipo ALFA NUMERICO,
		# MAS ao passar no validador, mostra que são exatamente os campos do modelo da FEBRABAN original
		#
		# no validador, do campo 024 até o 115 deverá ser preenchido com '0'
		#
		#
		# por isto, o campo NUMERO_AVISO_LANCAMENTO vira CHAR
		# ----------------------------------------------------------------------------------------------------------------
		self.numero_aviso_lancamento = TagCaracter(self._tipo_registro, u'14.5', u'numero_aviso_lancamento',	116, 123, descricao=u'*C072', comentario=u'Número aviso de lançamento', lote=self._lote)
