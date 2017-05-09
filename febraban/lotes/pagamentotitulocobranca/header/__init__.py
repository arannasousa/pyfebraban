# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'


from ....base import (TagCaracter, TXT)
from .... import TIPO_REGISTRO, NIVEIS, gera_text

from .controle import Controle
from .servico import Servico
from .empresa import Empresa
from .endereco import EnderecoEmpresa

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
		self.CNAB081			= TagCaracter(self._tipo_registro,  u'08.1', u'CNAB081', 	17, 17, descricao=u'G004', comentario=u'CNAB', lote=self._lote)
		self.empresa			= Empresa(lote=self._lote)
		self.informacao1		= TagCaracter(self._tipo_registro, u'18.1', u'informacao1',	103, 142, descricao=u'*G031', comentario=u'Mensagem', lote=self._lote)
		self.endereco_empresa 	= EnderecoEmpresa(lote=self._lote)
		self.CNAB261			= TagCaracter(self._tipo_registro,  u'26.1', u'CNAB261', 	223, 230, descricao=u'G004', comentario=u'CNAB', lote=self._lote)
		self.ocorrencias 		= TagCaracter(self._tipo_registro,  u'27.1', u'ocorrencias', 231, 240, descricao=u'*G059', comentario=u'Código das ocorrências p/ retorno', lote=self._lote)

	def get_txt(self):

		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.CNAB081.txt
		txt += self.empresa.txt
		txt += self.informacao1.txt
		txt += self.endereco_empresa.txt
		txt += self.CNAB261.txt
		txt += self.ocorrencias.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.CNAB081.txt = arquivo
			self.empresa.txt = arquivo
			self.informacao1.txt = arquivo
			self.endereco_empresa.txt = arquivo
			self.CNAB261.txt = arquivo
			self.ocorrencias.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.CNAB081.alertas)
		alertas.extend(self.empresa.alertas)
		alertas.extend(self.informacao1.alertas)
		alertas.extend(self.endereco_empresa.alertas)
		alertas.extend(self.CNAB261.alertas)
		alertas.extend(self.ocorrencias.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += gera_text(NIVEIS.N3, self.CNAB081.text)
		txt += self.empresa.text
		txt += gera_text(NIVEIS.N3, self.informacao1.text)
		txt += self.endereco_empresa.text
		txt += gera_text(NIVEIS.N3, self.CNAB261.text)
		txt += gera_text(NIVEIS.N3, self.ocorrencias.text)
		return txt

	text = property(get_text)