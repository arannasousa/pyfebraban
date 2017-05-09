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
from .totais import Totais

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
		self.totais					= Totais(lote=self._lote)
		self.numero_aviso_debito	= TagInteiro(self._tipo_registro, u'08.5', u'numero_aviso_debito',	 60,  65, descricao=u'G066', comentario=u'Número aviso débito', lote=self._lote)
		self.CNAB095				= TagCaracter(self._tipo_registro,  u'09.5', u'CNAB095', 	 		 66, 230, descricao=u'G004', comentario=u'CNAB', lote=self._lote)
		self.ocorrencias 			= TagCaracter(self._tipo_registro,  u'10.5', u'ocorrencias',		231, 240, descricao=u'*G059', comentario=u'Ocorrências', lote=self._lote)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.CNAB045.txt
		txt += self.totais.txt
		txt += self.numero_aviso_debito.txt
		txt += self.CNAB095.txt
		txt += self.ocorrencias.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.CNAB045.txt = arquivo
			self.totais.txt = arquivo
			self.numero_aviso_debito.txt = arquivo
			self.CNAB095.txt = arquivo
			self.ocorrencias.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.CNAB045.alertas)
		alertas.extend(self.totais.alertas)
		alertas.extend(self.numero_aviso_debito.alertas)
		alertas.extend(self.CNAB095.alertas)
		alertas.extend(self.ocorrencias.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += gera_text(NIVEIS.N3, self.CNAB045.text)
		txt += self.totais.text
		txt += gera_text(NIVEIS.N3, self.numero_aviso_debito.text)
		txt += gera_text(NIVEIS.N3, self.CNAB095.text)
		txt += gera_text(NIVEIS.N3, self.ocorrencias.text)
		return txt

	text = property(get_text)