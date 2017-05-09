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

class Inscricao(TXT):
	def __init__(self, lote=u'0001'):
		super(Inscricao, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		self.tipo	= TagInteiro(self._tipo_registro, u'09.1', u'tipo', 	18, 18, descricao=u'*G005', comentario=u'Tipo de inscrição da empresa', lote=self._lote)
		self.numero	= TagInteiro(self._tipo_registro, u'10.1', u'numero', 	19, 33, descricao=u'*G006', comentario=u'Número de incricao da empresa', lote=self._lote)

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
		txt = gera_text(NIVEIS.N4, unicode(__name__) + u'.Incricao' + u'\n')
		txt += gera_text(NIVEIS.N5, self.tipo.text)
		txt += gera_text(NIVEIS.N5, self.numero.text)
		return txt

	text = property(get_text)

class ContaCorrenteAgencia(TXT):
	def __init__(self, lote=u'0001'):
		super(ContaCorrenteAgencia, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		self.codigo	= TagInteiro(self._tipo_registro, u'12.1', u'codigo', 	54, 58, descricao=u'*G008', comentario=u'Agência mantenedora da conta', lote=self._lote)
		self.dv		= TagCaracter(self._tipo_registro, u'13.1', u'dv', 		59, 59, descricao=u'*G009', comentario=u'Dígito verificador da agência', lote=self._lote)

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
		txt = gera_text(NIVEIS.N5, unicode(__name__) + u'.ContaCorrente.Agencia' + u'\n')
		txt += gera_text(NIVEIS.N6, self.codigo.text)
		txt += gera_text(NIVEIS.N6, self.dv.text)
		return txt

	text = property(get_text)

class ContaCorrenteConta(TXT):
	def __init__(self, lote=u'0001'):
		super(ContaCorrenteConta, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		self.numero	= TagInteiro(self._tipo_registro, u'14.1', u'numero', 	60, 71, descricao=u'*G010', comentario=u'Número da conta corrente', lote=self._lote)
		self.dv		= TagCaracter(self._tipo_registro, u'15.1', u'dv', 		72, 72, descricao=u'*G011', comentario=u'Dígito verificador da conta', lote=self._lote)

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
		txt = gera_text(NIVEIS.N5, unicode(__name__) + u'.ContaCorrente.Conta' + u'\n')
		txt += gera_text(NIVEIS.N6, self.numero.text)
		txt += gera_text(NIVEIS.N6, self.dv.text)
		return txt

	text = property(get_text)

class ContaCorrente(TXT):
	def __init__(self, lote=u'0001'):
		super(ContaCorrente, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		self.agencia	= ContaCorrenteAgencia(lote=self._lote)
		self.conta		= ContaCorrenteConta(lote=self._lote)
		self.dv			= TagCaracter(self._tipo_registro, u'16.1', u'dv', 	73, 73, descricao=u'*G012', comentario=u'Dígito verificador da Ag/Conta', lote=self._lote)

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
		txt = gera_text(NIVEIS.N4, unicode(__name__) + u'.ContaCorrente' + u'\n')
		txt += self.agencia.text
		txt += self.conta.text
		txt += gera_text(NIVEIS.N5, self.dv.text)
		return txt

	text = property(get_text)

class Empresa(TXT):
	def __init__(self, lote=u'0001'):
		super(Empresa, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		self.inscricao		= Inscricao(lote=self._lote)
		self.convenio		= TagCaracter(self._tipo_registro, u'11.1', u'convenio', 34,  53, descricao=u'*G007', comentario=u'Código do convênio no banco', lote=self._lote)
		self.conta_corrente	= ContaCorrente(lote=self._lote)
		self.nome			= TagCaracter(self._tipo_registro, u'17.1', u'nome', 	 74, 103, descricao=u'G013', comentario=u'Nome da empresa', lote=self._lote)

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
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += self.inscricao.text
		txt += gera_text(NIVEIS.N4, self.convenio.text)
		txt += self.conta_corrente.text
		txt += gera_text(NIVEIS.N4, self.nome.text)
		return txt

	text = property(get_text)