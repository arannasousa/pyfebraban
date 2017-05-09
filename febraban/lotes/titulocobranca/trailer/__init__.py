# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....base import (TagCaracter, TXT, TagInteiro)
from .... import TIPO_REGISTRO, NIVEIS, gera_text

from .controle import Controle
from .totais_cobranca_simples import TotaisCobrancaSimples
from .totais_cobranca_vinculada import TotaisCobrancaVinculada
from .totais_cobranca_caucionada import TotaisCobrancaCaucionada
from .totais_cobranca_descontada import TotaisCobrancaDescontada

class LoteTrailer(TXT):
	def __init__(self, lote=u'0001'):
		super(LoteTrailer, self).__init__()

		self._lote = lote

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_TRAILER

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.controle 				= Controle(lote=self._lote)
		self.CNAB045				= TagCaracter(self._tipo_registro,  u'04.5', u'CNAB045', 	  		  9,  17, descricao=u'G004', comentario=u'CNAB', lote=self._lote)
		self.qtd_registros			= TagInteiro(self._tipo_registro, u'05.5', u'qtd_registros', 		 18,  23, descricao=u'*G057', comentario=u'Quantidade de registros do lote', lote=self._lote)
		self.totais_cobranca_simples 		= TotaisCobrancaSimples(lote=self._lote)
		self.totais_cobranca_vinculada 		= TotaisCobrancaVinculada(lote=self._lote)
		self.totais_cobranca_caucionada 	= TotaisCobrancaCaucionada(lote=self._lote)
		self.totais_cobranca_descontada 	= TotaisCobrancaDescontada(lote=self._lote)
		self.numero_aviso_lancamento= TagInteiro(self._tipo_registro, u'14.5', u'numero_aviso_lancamento',	116, 123, descricao=u'*C072', comentario=u'Número aviso de lançamento', lote=self._lote)
		self.CNAB155				= TagCaracter(self._tipo_registro,  u'15.5', u'CNAB155', 	 		 	124, 240, descricao=u'C004', comentario=u'CNAB', lote=self._lote)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.CNAB045.txt
		txt += self.qtd_registros.txt
		txt += self.totais_cobranca_simples.txt
		txt += self.totais_cobranca_vinculada.txt
		txt += self.totais_cobranca_caucionada.txt
		txt += self.totais_cobranca_descontada.txt
		txt += self.numero_aviso_lancamento.txt
		txt += self.CNAB155.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.CNAB045.txt = arquivo
			self.qtd_registros.txt = arquivo
			self.totais_cobranca_simples.txt = arquivo
			self.totais_cobranca_vinculada.txt = arquivo
			self.totais_cobranca_caucionada.txt = arquivo
			self.totais_cobranca_descontada.txt = arquivo
			self.numero_aviso_lancamento.txt = arquivo
			self.CNAB155.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.CNAB045.alertas)
		alertas.extend(self.qtd_registros.alertas)
		alertas.extend(self.totais_cobranca_simples.alertas)
		alertas.extend(self.totais_cobranca_vinculada.alertas)
		alertas.extend(self.totais_cobranca_caucionada.alertas)
		alertas.extend(self.totais_cobranca_descontada.alertas)
		alertas.extend(self.numero_aviso_lancamento.alertas)
		alertas.extend(self.CNAB155.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += gera_text(NIVEIS.N3, self.CNAB045.text)
		txt += gera_text(NIVEIS.N3, self.qtd_registros.text)
		txt += self.totais_cobranca_simples.text
		txt += self.totais_cobranca_vinculada.text
		txt += self.totais_cobranca_caucionada.text
		txt += self.totais_cobranca_descontada.text
		txt += gera_text(NIVEIS.N3, self.numero_aviso_lancamento.text)
		txt += gera_text(NIVEIS.N3, self.CNAB155.text)
		return txt

	text = property(get_text)