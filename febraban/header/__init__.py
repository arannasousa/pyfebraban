# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ..base import (TagCaracter, TXT)
from .. import TIPO_REGISTRO, NIVEIS, gera_text

from .controle import ArquivoHeaderControle
from .empresa import ArquivoHeaderEmpresa
from .arquivodados import ArquivoHeaderDados

class ArquivoHeader(TXT):
	def __init__(self):
		super(ArquivoHeader, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.controle 	= ArquivoHeaderControle()
		self.CNAB040	= TagCaracter(self._tipo_registro,  u'04.0', u'CNAB040', 	  9, 17, descricao=u'G004', comentario=u'CNAB')
		self.empresa	= ArquivoHeaderEmpresa()
		self.nome_banco	= TagCaracter(self._tipo_registro, u'14.0', u'nome_banco',	103, 132, descricao=u'G014', comentario=u'Nome do banco')
		self.CNAB150	= TagCaracter(self._tipo_registro,  u'15.0', u'CNAB150', 	133, 142, descricao=u'G004', comentario=u'CNAB')
		self.arquivo 	= ArquivoHeaderDados()
		self.reservado_banco = TagCaracter(self._tipo_registro,  u'21.0', u'reservado_banco', 172, 191, descricao=u'G021', comentario=u'Para uso reservado do banco')
		self.reservado_empresa = TagCaracter(self._tipo_registro,  u'22.0', u'reservado_empresa', 192, 211, descricao=u'G022', comentario=u'Para uso reservado da empresa')
		self.CNAB240	= TagCaracter(self._tipo_registro,  u'24.0', u'CNAB240', 	212, 240, descricao=u'G004', comentario=u'CNAB')


	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.CNAB040.txt
		txt += self.empresa.txt
		txt += self.nome_banco.txt
		txt += self.CNAB150.txt
		txt += self.arquivo.txt
		txt += self.reservado_banco.txt
		txt += self.reservado_empresa.txt
		txt += self.CNAB240.txt
		txt += '\n'

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.CNAB040.txt = arquivo
			self.empresa.txt = arquivo
			self.nome_banco.txt = arquivo
			self.CNAB150.txt = arquivo
			self.arquivo.txt = arquivo
			self.reservado_banco.txt = arquivo
			self.reservado_empresa.txt = arquivo
			self.CNAB240.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.CNAB040.alertas)
		alertas.extend(self.empresa.alertas)
		alertas.extend(self.nome_banco.alertas)
		alertas.extend(self.CNAB150.alertas)
		alertas.extend(self.arquivo.alertas)
		alertas.extend(self.reservado_banco.alertas)
		alertas.extend(self.reservado_empresa.alertas)
		alertas.extend(self.CNAB240.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N1, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += gera_text(NIVEIS.N3, self.CNAB040.text)
		txt += self.empresa.text
		txt += gera_text(NIVEIS.N3, self.nome_banco.text)
		txt += gera_text(NIVEIS.N3, self.CNAB150.text)
		txt += self.arquivo.text
		txt += gera_text(NIVEIS.N3, self.reservado_banco.text)
		txt += gera_text(NIVEIS.N3, self.reservado_empresa.text)
		txt += gera_text(NIVEIS.N3, self.CNAB240.text)

		return txt

	text = property(get_text)