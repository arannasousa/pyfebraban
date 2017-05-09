# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ..base import (TagCaracter, TagInteiro, TXT)

from .. import TIPO_REGISTRO, NIVEIS, gera_text

class HeaderEmpresaInscricao(TXT):
	def __init__(self):
		super(HeaderEmpresaInscricao, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		self.tipo	= TagInteiro(self._tipo_registro, u'05.0', u'tipo', 	18, 18, descricao=u'*G005', comentario=u'Tipo de inscrição da empresa')
		self.numero	= TagInteiro(self._tipo_registro, u'06.0', u'numero', 	19, 32, descricao=u'*G006', comentario=u'Número de incricao da empresa')

	def get_txt(self):
		txt = u''
		txt += self.tipo.txt
		txt += self.numero.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.tipo.txt = arquivo
			self.numero.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.tipo.alertas)
		alertas.extend(self.numero.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'.Inscricao' + u'\n')
		txt += gera_text(NIVEIS.N4, self.tipo.text)
		txt += gera_text(NIVEIS.N4, self.numero.text)
		return txt

	text = property(get_text)

class HeaderEmpresaContaCorrenteAgencia(TXT):
	def __init__(self):
		super(HeaderEmpresaContaCorrenteAgencia, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		self.codigo	= TagInteiro(self._tipo_registro, u'08.0', u'codigo', 	53, 57, descricao=u'*G008', comentario=u'Agência mantenedora da conta')
		self.dv		= TagCaracter(self._tipo_registro, u'09.0', u'dv', 		58, 58, descricao=u'*G009', comentario=u'Dígito verificador da agência')

	def get_txt(self):
		txt = u''
		txt += self.codigo.txt
		txt += self.dv.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.codigo.txt = arquivo
			self.dv.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.codigo.alertas)
		alertas.extend(self.dv.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N4, unicode(__name__) + u'.ContaCorrente.Agencia' + u'\n')
		txt += gera_text(NIVEIS.N5, self.codigo.text)
		txt += gera_text(NIVEIS.N5, self.dv.text)
		return txt

	text = property(get_text)

class HeaderEmpresaContaCorrenteConta(TXT):
	def __init__(self):
		super(HeaderEmpresaContaCorrenteConta, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		self.numero	= TagInteiro(self._tipo_registro, u'10.0', u'numero', 	59, 70, descricao=u'*G010', comentario=u'Número da conta corrente')
		self.dv		= TagCaracter(self._tipo_registro, u'11.0', u'dv', 		71, 71, descricao=u'*G011', comentario=u'Dígito verificador da conta')

	def get_txt(self):
		txt = u''
		txt += self.numero.txt
		txt += self.dv.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.numero.txt = arquivo
			self.dv.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.numero.alertas)
		alertas.extend(self.dv.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N4, unicode(__name__) + u'.ContaCorrente.Conta' + u'\n')
		txt += gera_text(NIVEIS.N5, self.numero.text)
		txt += gera_text(NIVEIS.N5, self.dv.text)
		return txt

	text = property(get_text)

class HeaderEmpresaContaCorrente(TXT):
	def __init__(self):
		super(HeaderEmpresaContaCorrente, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		self.agencia	= HeaderEmpresaContaCorrenteAgencia()
		self.conta		= HeaderEmpresaContaCorrenteConta()
		self.dv			= TagCaracter(self._tipo_registro, u'12.0', u'dv', 	72, 72, descricao=u'*G012', comentario=u'Dígito verificador da Ag/Conta')

	def get_txt(self):
		txt = u''
		txt += self.agencia.txt
		txt += self.conta.txt
		txt += self.dv.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.agencia.txt = arquivo
			self.conta.txt = arquivo
			self.dv.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.agencia.alertas)
		alertas.extend(self.conta.alertas)
		alertas.extend(self.dv.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'.ContaCorrente' + u'\n')
		txt += self.agencia.text
		txt += self.conta.text
		txt += gera_text(NIVEIS.N4, self.dv.text)
		return txt

	text = property(get_text)

class ArquivoHeaderEmpresa(TXT):
	def __init__(self):
		super(ArquivoHeaderEmpresa, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.ARQUIVO_HEADER

		self.inscricao		= HeaderEmpresaInscricao()
		self.convenio		= TagCaracter(self._tipo_registro, u'07.0', u'convenio', 33, 52, descricao=u'*G007', comentario=u'Código do convênio no banco')
		self.conta_corrente	= HeaderEmpresaContaCorrente()
		self.nome			= TagCaracter(self._tipo_registro, u'13.0', u'nome', 73, 102, descricao=u'G013', comentario=u'Nome da empresa')

	def get_txt(self):
		txt = u''
		txt += self.inscricao.txt
		txt += self.convenio.txt
		txt += self.conta_corrente.txt
		txt += self.nome.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.inscricao.txt = arquivo
			self.convenio.txt = arquivo
			self.conta_corrente.txt = arquivo
			self.nome.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.inscricao.alertas)
		alertas.extend(self.convenio.alertas)
		alertas.extend(self.conta_corrente.alertas)
		alertas.extend(self.nome.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.inscricao.text
		txt += gera_text(NIVEIS.N3, self.convenio.text)
		txt += self.conta_corrente.text
		txt += gera_text(NIVEIS.N3, self.nome.text)

		return txt

	text = property(get_text)