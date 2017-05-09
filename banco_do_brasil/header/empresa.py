# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...febraban.header import ArquivoHeaderEmpresa as ArquivoHeaderEmpresa_febraban

from ...febraban.base import (TagCaracter, TagInteiro, TXT)
# from febraban import TIPO_REGISTRO, NIVEIS, gera_text

class ArquivoHeaderEmpresa(ArquivoHeaderEmpresa_febraban):
	def __init__(self):
		super(ArquivoHeaderEmpresa, self).__init__()

		# --------------------------------------------------------
		# 	valor padrao
		# --------------------------------------------------------
		self.cobranca_cedente = u'0014'

	# ----------------------------------------------------------------
	# 	Campo reservado BB 07.0-BB2		33-41
	# ----------------------------------------------------------------
	def get_numero_convenio(self):
		"""
		:rtype:	int
		"""
		de = 33 - self.convenio.de
		ate = 41 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_numero_convenio(self, valor):
		de = 33 - self.convenio.de
		ate = 41 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]

		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	numero_convenio = property(get_numero_convenio, set_numero_convenio)

	# ----------------------------------------------------------------
	# 	Campo reservado BB 07.0-BB2		42-45
	# ----------------------------------------------------------------
	def get_cobranca_cedente(self):
		"""
		:rtype:	int
		"""
		de = 42 - self.convenio.de
		ate = 45 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_cobranca_cedente(self, valor):
		de = 42 - self.convenio.de
		ate = 45 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	cobranca_cedente = property(get_cobranca_cedente, set_cobranca_cedente)


	# ----------------------------------------------------------------
	# 	Campo reservado BB 07.0-BB3		46-47
	# ----------------------------------------------------------------
	def get_numero_carteira(self):
		"""
		:rtype:	int
		"""
		de = 46 - self.convenio.de
		ate = 47 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_numero_carteira(self, valor):
		de = 46 - self.convenio.de
		ate = 47 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	numero_carteira = property(get_numero_carteira, set_numero_carteira)


	# ----------------------------------------------------------------
	# 	Campo reservado BB 07.0-BB4		48-50
	# ----------------------------------------------------------------
	def get_numero_variacao_carteira(self):
		"""
		:rtype:	int
		"""
		de = 48 - self.convenio.de
		ate = 50 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_numero_variacao_carteira(self, valor):
		de = 48 - self.convenio.de
		ate = 50 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	numero_variacao_carteira = property(get_numero_variacao_carteira, set_numero_variacao_carteira)

	# ----------------------------------------------------------------
	# 	Campo reservado BB 07.0-BB5		51-52
	# ----------------------------------------------------------------
	def get_campo_reservado(self):
		"""
		:rtype:	unicode
		"""
		de = 51 - self.convenio.de
		ate = 52 - self.convenio.de + 1

		return self.convenio.valor[de:ate]

	def set_campo_reservado(self, valor):
		de = 51 - self.convenio.de
		ate = 52 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).ljust(ate-de, u' ') + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	campo_reservado = property(get_campo_reservado, set_campo_reservado)