# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban.lotes.titulocobranca.header.empresa import Empresa as Empresa_febraban

class Empresa(Empresa_febraban):
	def __init__(self, lote=u'0001'):
		super(Empresa, self).__init__(lote=lote)

		# ----------------------------------------------------------------------
		# 	valor padrao para COBRANCA CEDENTE
		# ----------------------------------------------------------------------
		self.cobranca_cedente = u'0014'

	# --------------------------------------------------------------------------------------------------------------
	# 	facilitar o entendimento, o campo CONVENIO foi dividido em 5 partes
	# --------------------------------------------------------------------------------------------------------------
	def get_numero_convenio_cobranca(self):
		"""
		Número do convênio de cobrança BB

		codigo: 11.1-BB1		de-ate: 34-42

		:rtype:	int
		"""
		de = 34 - self.convenio.de
		ate = 42 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_numero_convenio_cobranca(self, valor):
		"""
		Número do convênio de cobrança BB

		codigo: 11.1-BB1		de-ate: 34-42
		"""
		de = 34 - self.convenio.de
		ate = 42 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= (ate-de):
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	numero_convenio_cobranca = property(get_numero_convenio_cobranca, set_numero_convenio_cobranca)



	def get_cobranca_cedente(self):
		"""
		Cobrança cedente BB

		codigo: 11.1-BB2		de-ate: 43-46

		:rtype:	int
		"""
		de = 43 - self.convenio.de
		ate = 46 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_cobranca_cedente(self, valor):
		"""
		Cobrança cedente BB

		codigo: 11.1-BB2		de-ate: 43-46
		"""
		de = 43 - self.convenio.de
		ate = 46 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= (ate-de):
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	cobranca_cedente = property(get_cobranca_cedente, set_cobranca_cedente)



	def get_numero_carteira_cobranca_cedente(self):
		"""
		Número da carteira de cobrança BB

		codigo: 11.1-BB3		de-ate: 47-48

		:rtype:	int
		"""
		de = 47 - self.convenio.de
		ate = 48 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_numero_carteira_cobranca_cedente(self, valor):
		"""
		Número da carteira de cobrança BB

		codigo: 11.1-BB3		de-ate: 47-48
		"""
		de = 47 - self.convenio.de
		ate = 48 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	numero_carteira_cobranca_cedente = property(get_numero_carteira_cobranca_cedente, set_numero_carteira_cobranca_cedente)



	def get_numero_variacao_carteira_cobranca(self):
		"""
		Informar o número da variação da carteira de cobrança

		codigo: 11.1-BB4		de-ate: 49-51

		:rtype:	int
		"""
		de = 49 - self.convenio.de
		ate = 51 - self.convenio.de + 1

		return int(self.convenio.valor[de:ate].replace(u' ', u'0'))

	def set_numero_variacao_carteira_cobranca(self, valor):
		"""
		Informar o número da variação da carteira de cobrança

		codigo: 11.1-BB4		de-ate: 49-51
		"""
		de = 49 - self.convenio.de
		ate = 51 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).zfill(ate-de) + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	numero_variacao_carteira_cobranca = property(get_numero_variacao_carteira_cobranca, set_numero_variacao_carteira_cobranca)



	def get_identificador_remessa_teste(self):
		"""
		Campo que identifica remessa de testes

		codigo: 11.1-BB5		de-ate: 52-53

		:rtype:	unicode
		"""
		de = 52 - self.convenio.de
		ate = 53 - self.convenio.de + 1

		return self.convenio.valor[de:ate]

	def set_identificador_remessa_teste(self, valor):
		"""
		Campo que identifica remessa de testes

		codigo: 11.1-BB5		de-ate: 52-53

		"""
		de = 52 - self.convenio.de
		ate = 53 - self.convenio.de + 1

		if len(unicode(valor)) and len(unicode(valor)) <= ate-de:
			self.convenio.valor = self.convenio.valor[:de] + unicode(valor).ljust(ate-de, u' ') + self.convenio.valor[ate:]
		else:
			# convenio é char
			self.convenio.valor = self.convenio.valor[:de] + unicode(u'').ljust(ate-de, u' ') + self.convenio.valor[ate:]

	identificador_remessa_teste = property(get_identificador_remessa_teste, set_identificador_remessa_teste)