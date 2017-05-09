# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'


from ....base import (TagCaracter, TagData, TagInteiro, TXT)
from .... import TIPO_REGISTRO, NIVEIS, gera_text

from .controle import Controle
from .servico import Servico
from .empresa import Empresa
from .controle_cobranca import ControleCobranca

class LoteHeader(TXT):
	def __init__(self, lote=u'0001'):
		super(LoteHeader, self).__init__()

		self._lote = lote

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.controle 			= Controle(lote=self._lote)
		self.servico			= Servico(lote=self._lote)
		self.CNAB081			= TagCaracter(self._tipo_registro,  u'08.1', u'CNAB081', 	  17,  17, descricao=u'G004', comentario=u'CNAB', lote=self._lote)
		self.empresa			= Empresa(lote=self._lote)
		self.informacao1		= TagCaracter(self._tipo_registro, u'18.1', u'informacao1',	  104, 143, descricao=u'C073', comentario=u'Mensagem 1', lote=self._lote)
		self.informacao2		= TagCaracter(self._tipo_registro, u'19.1', u'informacao2',	  144, 183, descricao=u'C073', comentario=u'Mensagem 2', lote=self._lote)
		self.controle_cobranca 	= ControleCobranca(lote=self._lote)
		self.data_credito		= TagData(self._tipo_registro,  	u'22.1', u'data_credito', 200, 207, descricao=u'C003', comentario=u'Data do crédito', lote=self._lote)
		self.CNAB231			= TagCaracter(self._tipo_registro,  u'23.1', u'CNAB231', 	  208, 240, descricao=u'G004', comentario=u'CNAB', lote=self._lote)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.CNAB081.txt
		txt += self.empresa.txt
		txt += self.informacao1.txt
		txt += self.informacao2.txt
		txt += self.controle_cobranca.txt
		txt += self.data_credito.txt
		txt += self.CNAB231.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.CNAB081.txt = arquivo
			self.empresa.txt = arquivo
			self.informacao1.txt = arquivo
			self.informacao2.txt = arquivo
			self.controle_cobranca.txt = arquivo
			self.data_credito.txt = arquivo
			self.CNAB231.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.CNAB081.alertas)
		alertas.extend(self.empresa.alertas)
		alertas.extend(self.informacao1.alertas)
		alertas.extend(self.informacao2.alertas)
		alertas.extend(self.controle_cobranca.alertas)
		alertas.extend(self.data_credito.alertas)
		alertas.extend(self.CNAB231.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += gera_text(NIVEIS.N3, self.CNAB081.text)
		txt += self.empresa.text
		txt += gera_text(NIVEIS.N3, self.informacao1.text)
		txt += gera_text(NIVEIS.N3, self.informacao2.text)
		txt += self.controle_cobranca.text
		txt += gera_text(NIVEIS.N3, self.data_credito.text)
		txt += gera_text(NIVEIS.N3, self.CNAB231.text)
		return txt

	text = property(get_text)