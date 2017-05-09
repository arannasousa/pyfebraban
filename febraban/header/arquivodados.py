# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ..base import (TagData, TagHora, TagInteiro, TXT)
from .. import TIPO_REGISTRO, NIVEIS, gera_text

class ArquivoHeaderDados(TXT):
	def __init__(self):
		super(ArquivoHeaderDados, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None

		self.codigo			= TagInteiro(self._tipo_registro, u'16.0', u'codigo', 		143, 143, descricao=u'G015', comentario=u'Código do banco na compensação')
		self.data_geracao	= TagData(self._tipo_registro, u'17.0', u'data_geracao', 	144, 151, descricao=u'G016', comentario=u'Data da geração do arquivo')
		self.hora_geracao	= TagHora(self._tipo_registro, u'18.0', u'hora_geracao',	152, 157, descricao=u'G017', comentario=u'Hora da geração do arquivo')
		self.sequencia		= TagInteiro(self._tipo_registro, u'19.0', u'sequencia',	158, 163, descricao=u'*G018', comentario=u'Número sequencial do arquivo')
		self.layout			= TagInteiro(self._tipo_registro, u'20.0', u'layout',		164, 166, descricao=u'*G019', comentario=u'Nº da versão do layout do arquivo', valor=u'090')
		self.densidade		= TagInteiro(self._tipo_registro, u'21.0', u'densidade',	167, 171, descricao=u'G020', comentario=u'Densidade de gravacao do arquivo')

	def get_txt(self):

		txt = u''
		txt += self.codigo.txt
		txt += self.data_geracao.txt
		txt += self.hora_geracao.txt
		txt += self.sequencia.txt
		txt += self.layout.txt
		txt += self.densidade.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.codigo.txt = arquivo
			self.data_geracao.txt = arquivo
			self.hora_geracao.txt = arquivo
			self.sequencia.txt = arquivo
			self.layout.txt = arquivo
			self.densidade.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.codigo.alertas)
		alertas.extend(self.data_geracao.alertas)
		alertas.extend(self.hora_geracao.alertas)
		alertas.extend(self.sequencia.alertas)
		alertas.extend(self.layout.alertas)
		alertas.extend(self.densidade.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'.Arquivo' + u'\n')
		txt += gera_text(NIVEIS.N3, self.codigo.text)
		txt += gera_text(NIVEIS.N3,self.data_geracao.text)
		txt += gera_text(NIVEIS.N3,self.hora_geracao.text)
		txt += gera_text(NIVEIS.N3,self.sequencia.text)
		txt += gera_text(NIVEIS.N3,self.layout.text)
		txt += gera_text(NIVEIS.N3,self.densidade.text)

		return txt

	text = property(get_text)