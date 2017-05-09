# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'


from ....base import (TagCaracter, TagInteiro, TXT)

from .... import TIPO_REGISTRO, NIVEIS, gera_text

class EnderecoEmpresa(TXT):
	def __init__(self, lote=u'0001'):
		super(EnderecoEmpresa, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		self.logradouro			= TagCaracter(self._tipo_registro, u'19.1', u'logradouro',	143, 172, descricao=u'G032', comentario=u'Nome da rua, av, praça, etc', lote=self._lote)
		self.numero				= TagInteiro(self._tipo_registro, u'20.1', u'numero', 		173, 177, descricao=u'G032', comentario=u'Número do local', lote=self._lote)
		self.complemento		= TagCaracter(self._tipo_registro, u'21.1', u'complemento', 178, 192, descricao=u'G032', comentario=u'Casa, apto, sala, etc', lote=self._lote)
		self.cidade				= TagCaracter(self._tipo_registro, u'22.1', u'cidade', 		193, 212, descricao=u'G033', comentario=u'Cidade', lote=self._lote)
		self.cep				= TagInteiro(self._tipo_registro, u'23.1', u'cep', 			213, 217, descricao=u'G034', comentario=u'CEP', lote=self._lote)
		self.complemento_cep	= TagCaracter(self._tipo_registro, u'24.1', u'complemento_cep', 218, 220, descricao=u'G035', comentario=u'Complemento CEP', lote=self._lote)
		self.estado				= TagCaracter(self._tipo_registro, u'25.1', u'estado', 		221, 222, descricao=u'G036', comentario=u'Sigla do estado', lote=self._lote)

	def get_txt(self):

		txt = u''
		txt += self.logradouro.txt
		txt += self.numero.txt
		txt += self.complemento.txt
		txt += self.cidade.txt
		txt += self.cep.txt
		txt += self.complemento_cep.txt
		txt += self.estado.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.logradouro.txt = arquivo
			self.numero.txt = arquivo
			self.complemento.txt = arquivo
			self.cidade.txt = arquivo
			self.cep.txt = arquivo
			self.complemento_cep.txt = arquivo
			self.estado.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.logradouro.alertas)
		alertas.extend(self.numero.alertas)
		alertas.extend(self.complemento.alertas)
		alertas.extend(self.cidade.alertas)
		alertas.extend(self.cep.alertas)
		alertas.extend(self.complemento_cep.alertas)
		alertas.extend(self.estado.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__package__) + unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.logradouro.text)
		txt += gera_text(NIVEIS.N4, self.numero.text)
		txt += gera_text(NIVEIS.N4, self.complemento.text)
		txt += gera_text(NIVEIS.N4, self.cidade.text)
		txt += gera_text(NIVEIS.N4, self.cep.text)
		txt += gera_text(NIVEIS.N4, self.complemento_cep.text)
		txt += gera_text(NIVEIS.N4, self.estado.text)
		return txt

	text = property(get_text)