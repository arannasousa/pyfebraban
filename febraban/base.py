# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime, date, time
from decimal import Decimal
import locale
import unicodedata
import re
import pytz

try:
	locale.setlocale(locale.LC_ALL, b'pt_BR.UTF-8')
	locale.setlocale(locale.LC_COLLATE, b'pt_BR.UTF-8')
except:
	locale.setlocale(locale.LC_ALL, b'')
	locale.setlocale(locale.LC_COLLATE, b'')


def tirar_acentos(texto):
	if not texto:
		return texto or ''

	# ---------------------------------------------------------------------------------
	# como no febrabam não especifica se pode usar essas simbologias, vou retirar tudo
	# ---------------------------------------------------------------------------------
	texto = texto.replace('&', '')
	texto = texto.replace('<', '')
	texto = texto.replace('>', '')
	texto = texto.replace('"', '')
	texto = texto.replace("'", '')
	# texto = texto.replace('&', '&amp;')
	# texto = texto.replace('<', '&lt;')
	# texto = texto.replace('>', '&gt;')
	# texto = texto.replace('"', '&quot;')
	# texto = texto.replace("'", '&apos;')

	#
	# Trocar ENTER e TAB
	#
	texto = texto.replace('\t', ' ')
	texto = texto.replace('\n', '')

	# # Remove espaços seguidos
	# # Nem pergunte...
	# while '  ' in texto:
	# 	texto = texto.replace('  ', ' ')

	return texto


def por_acentos(texto):
	if not texto:
		return texto

	texto = texto.replace('&#39;', "'")
	texto = texto.replace('&apos;', "'")
	texto = texto.replace('&quot;', '"')
	texto = texto.replace('&gt;', '>')
	texto = texto.replace('&lt;', '<')
	texto = texto.replace('&amp;', '&')
	texto = texto.replace('&APOS;', "'")
	texto = texto.replace('&QUOT;', '"')
	texto = texto.replace('&GT;', '>')
	texto = texto.replace('&LT;', '<')
	texto = texto.replace('&AMP;', '&')

	return texto

def _tipo_para_string(valor, tipo, obrigatorio, dec_min):
	if (not obrigatorio) and (not valor):
		return u'', u''

	decimais = u''

	# Cuidado!!!
	# Aqui não dá pra usar a função strftime pois em alguns
	# casos a data retornada é 01/01/0001 00:00:00
	# e a função strftime só aceita data com anos a partir de 1900
	if (tipo in (u'd', u'h', u'dh')) and isinstance(valor, (datetime, date, time,)):
		valor = formata_datahora(valor, tipo)
	elif (tipo == 'n') and isinstance(valor, (int, long, float, Decimal)):
		if isinstance(valor, (int, long, float)):
			valor = Decimal(unicode(valor))

		valor = unicode(valor).strip()

		if u'.' in valor:
			decimais = valor.split(u'.')[1]

		if dec_min:
			decimais = decimais.ljust(dec_min, u'0')

			if u'.' in valor:
				valor = valor.split(u'.')[0]

			valor += u'.' + decimais

	return valor, decimais


def _string_para_tipo(valor, tipo):
	if valor == None:
		return valor

	if tipo == 'd':
		valor = datetime.strptime(valor, b'%Y-%m-%d')
	elif tipo == 'h':
		valor = datetime.strptime(valor, b'%H:%M:%S')
	elif tipo == 'dh':
		valor = datetime.strptime(valor, b'%Y-%m-%dT%H:%M:%S')
	elif tipo == 'n':
		valor = Decimal(valor)

	return valor


def formata_datahora(valor, tipo):
	if (tipo == 'd') and isinstance(valor, (datetime, date,)):
		valor = '%04d-%02d-%02d' % (valor.year, valor.month, valor.day)
	elif (tipo == 'h') and isinstance(valor, (datetime, time,)):
		valor = '%02d:%02d:%02d' % (valor.hour, valor.minute, valor.second)
		valor = valor.strftime('%H:%M:%S')
	elif (tipo == 'dh') and isinstance(valor, datetime):
		valor = '%04d-%02d-%02dT%02d:%02d:%02d' % (valor.year, valor.month, valor.day, valor.hour, valor.minute, valor.second)

	return valor


def somente_ascii(funcao):
	'''
	Usado como decorator para a nota fiscal eletrônica de servicos
	'''

	def converter_para_ascii_puro(*args, **kwargs):
		return unicodedata.normalize(b'NFKD', funcao(*args, **kwargs)).encode('ascii', 'ignore')

	return converter_para_ascii_puro


class RegistroTXT(object):
	def __init__(self, *args, **kwargs):
		self._txt = None
		self._alertas = []

		# 	deve ser um LIST de duas posicoes, subtraindo o primeiro digito, sempre
		# 	de acordo ao manual da FEBRABAN
		self._posicoes_identificador_lote = [4, 7]				# campo FIXO - G002
		self._posicoes_identificador_tipo_registro = [8, 8]		# campo FIXO - G003
		self._posicoes_identificador_tipo_operacao = None		# [9, 9]	# depende do registro
		self._posicoes_identificador_numero_sequencia = [9, 13] # fixo
		self._posicoes_identificador_segmento = [14, 14] 		# fixo

	def _le_txt(self, arquivo):
		if arquivo is None:
			return False

		if isinstance(arquivo, file):
			# --------------------------------------
			# 	le o arquivo em LIST
			# --------------------------------------
			self._txt = arquivo.readlines()
			arquivo.close()

			for i, t in enumerate(self._txt):
				self._txt[i] = unicode(t)

			return True

		elif isinstance(arquivo, basestring):
			if isinstance(arquivo, str):
				arquivo = unicode(arquivo.encode('utf-8'))

			# ------------------------------------
			# le o arquivo
			# ------------------------------------
			arquivo = unicode(arquivo).split(u'\n')

		if isinstance(arquivo, list):
			self._txt = arquivo
			return True

		return False

	def _le_nohs(self, tipo_registro, lote=None, num_seq=None, segmento=None, operacao=None):
		"""
		Busca todos os REGISTROS (linhas) que possuam o "tipo_registro" e "segmento" informados
		"""
		if isinstance(self._txt, list):
			pos_tipo_reg = slice(
				self._posicoes_identificador_tipo_registro[0] - 1,
				self._posicoes_identificador_tipo_registro[1]
			)

			pos_lote = None
			if lote and self._posicoes_identificador_lote:
				pos_lote = slice(
					self._posicoes_identificador_lote[0] - 1,
					self._posicoes_identificador_lote[1]
				)

			# ---------------------------------------------------------
			# 	usado na IDENTIFICACAO DO LOTE
			# ---------------------------------------------------------
			pos_operacao = None
			if operacao and self._posicoes_identificador_tipo_operacao:
				pos_operacao = slice(
					self._posicoes_identificador_tipo_operacao - 1,
					self._posicoes_identificador_tipo_operacao
				)

			# ---------------------------------------------------------
			# 	usado na IDENTIFICACAO DO SEGMENTO do serviço
			# ---------------------------------------------------------
			pos_segmento = None
			if segmento and self._posicoes_identificador_segmento:
				pos_segmento = slice(
					self._posicoes_identificador_segmento[0] - 1,
					self._posicoes_identificador_segmento[1]
				)

			# ---------------------------------------------------------
			# 	usado na IDENTIFICACAO do NUMERO do Registro no Lote
			# ---------------------------------------------------------
			pos_num_seq = None
			if num_seq and self._posicoes_identificador_numero_sequencia:
				pos_num_seq = slice(
					self._posicoes_identificador_numero_sequencia[0] - 1,
					self._posicoes_identificador_numero_sequencia[1]
				)

			nohs = []
			for t in self._txt:
				# --------------------------------------------------------
				# 	é o tipo de registro que estou buscando
				# --------------------------------------------------------
				if t[pos_tipo_reg] == tipo_registro:
					# --------------------------------------------------
					# se NAO for de um lote especifico, PULA
					# --------------------------------------------------
					if pos_lote and (t[pos_lote] != unicode(lote)):
						continue

					# --------------------------------------------------
					# se NAO for o numero sequencial solicitado do registro no lote, pula
					# --------------------------------------------------
					if pos_num_seq and (t[pos_num_seq] != unicode(num_seq)):
						continue

					# --------------------------------------------------------
					# 	se possuir operacao, busca com a operacao
					# --------------------------------------------------------
					if pos_operacao and t[pos_operacao] == operacao:
						nohs.append(t)

					# --------------------------------------------------------
					# se possuir segmento, busca com o segumento solicitado
					# --------------------------------------------------------
					elif pos_segmento and t[pos_segmento] == segmento:
						nohs.append(t)
					else:
						nohs.append(t)

			return nohs

		return None

	def _le_noh(self, tipo_registro, lote=None, num_seq=None, segmento=None, operacao=None, ocorrencia=1):

		nohs = self._le_nohs(tipo_registro, lote=lote, num_seq=num_seq, segmento=segmento, operacao=operacao)

		if (nohs is not None) and (len(nohs) >= ocorrencia):
			return nohs[ocorrencia - 1]
		else:
			return None

	def _le_campo(self, tipo_registro, de, ate, lote=None, num_seq=None, segmento=None, operacao=None, ocorrencia=1):
		# ------------------------------------------------
		# 	le o registro
		# ------------------------------------------------
		noh = self._le_noh(tipo_registro, lote=lote, num_seq=num_seq, segmento=segmento, operacao=operacao,
						   ocorrencia=ocorrencia)

		if noh is None:
			valor = u''
		else:
			if len(noh) > 0:
				valor = noh[de - 1: ate]
			else:
				valor = u''

		return valor


class ErroObrigatorio(Exception):
	def __init__(self, raiz, codigo, nome, propriedade):
		if propriedade:
			self.value = u'%(raiz)s No campo código %(codigo)s, "%(nome)s", a propriedade "%(propriedade)s" é de envio obrigatório, mas não foi preenchida.' % {
				u'codigo': codigo,
				u'nome': nome,
				u'propriedade': propriedade,
				u'raiz': raiz,
			}
		else:
			self.value = u'%(raiz)s O campo código %(codigo)s, "%(nome)s" é de envio obrigatório, mas não foi preenchido.' % {
				u'codigo': codigo,
				u'nome': nome,
				u'raiz': raiz,
			}

	def __str__(self):
		return repr(self.value)

	def __unicode__(self):
		return self.value


class TamanhoInvalido(Exception):
	def __init__(self, codigo, nome, valor, tam_max=None, dec_min=None, dec_max=None):
		if tam_max:
			self.value = u'O campo código %(codigo)s, "%(nome)s", deve ter o tamanho máximo de %(tam_max)s, mas o tamanho enviado foi %(tam_env)s: %(valor)s' % {
				u'codigo': codigo,
				u'nome': nome,
				u'tam_max': unicode(tam_max),
				u'tam_env': unicode(len(unicode(valor))),
				u'valor': unicode(valor),
			}
		elif dec_min:
			self.value = u'O campo código %(codigo)s, "%(nome)s", deve ter o mínimo de %(dec_min)s casas decimais, mas o enviado foi %(tam_env)s: %(valor)s' % {
				u'codigo': codigo,
				u'nome': nome,
				u'dec_min': unicode(dec_min),
				u'tam_env': unicode(len(unicode(valor))),
				u'valor': unicode(valor),
			}
		elif dec_max:
			self.value = u'O campo código %(codigo)s, "%(nome)s", deve ter o máximo de %(dec_max)s casas decimais, mas o enviado foi %(tam_env)s: %(valor)s' % {
				u'codigo': codigo,
				u'nome': nome,
				u'dec_max': unicode(dec_max),
				u'tam_env': unicode(len(unicode(valor))),
				u'valor': unicode(valor),
			}

	def __str__(self):
		return repr(self.value)

	def __unicode__(self):
		return self.value


class ErroCaracterInvalido(Exception):
	def __init__(self,  codigo, nome, valor, caracter):
		self.value = u'O campo código %(codigo)s, "%(nome)s" possui um caracter inválido: "%(caracter)s".' % {
			u'codigo': codigo,
			u'nome': nome,
			u'caracter': caracter,
		}

	def __str__(self):
		return repr(self.value)

	def __unicode__(self):
		return self.value

class ErroFormatoInvalido(Exception):
	def __init__(self,  codigo, nome, valor, formato):
		self.value = u'O campo código %(codigo)s, "%(nome)s" possui um formato inválido: "%(valor)s" - "%(formato)s".' % {
			u'codigo': codigo,
			u'nome': nome,
			u'valor': unicode(valor),
			u'formato': formato,
		}

	def __str__(self):
		return repr(self.value)

	def __unicode__(self):
		return self.value

class TagCaracter(RegistroTXT):
	def __init__(self, tipo_registro, codigo, nome, de, ate, valor=None, descricao=None,
				 alertas=[], comentario=None, segmento=None, operacao=None, lote=None, num_seq=None,
				 *args, **kwargs):
		super(TagCaracter, self).__init__(*args, **kwargs)

		assert type(de) == int, u'(%s-%s)[%s] atributo "de" deve ser inteiro' % (codigo, descricao, nome)
		assert type(ate) == int, u'(%s-%s)[%s] atributo "ate" deve ser inteiro' % (codigo, descricao, nome)
		assert de <= ate, u'(%s-%s)[%s] atributo "ate" deve ser maior ou igual que o atributo "de"' % (codigo, descricao, nome)

		self.tipo_registro = tipo_registro
		self.lote = lote				# usado nos lotes e detalhes - numeracao do lote
		self.operacao = operacao		# usado no LOTE
		self.segmento = segmento		# usado nos detalhes - seguimentos
		self.num_seq = num_seq
		self.codigo = codigo
		self.nome = nome
		self.de = de					# posicao do campo inicial
		self.ate = ate					# posicao do campo final
		# o -1 é pq o [x:y], x é o valor -1
		self.tamanho = self.ate - (self.de - 1)
		self._valor_string = u' '.ljust(self.tamanho, u' ')
		self._alertas = alertas
		self.valor = valor
		self.descricao = descricao
		self.comentario = comentario

		# Codigo para dinamizar a criacao de instancias de entidade,
		# aplicando os valores dos atributos na instanciacao
		for k, v in kwargs.items():
			setattr(self, k, v)

		if kwargs.has_key('valor'):
			self.valor = kwargs['valor']

	def _testa_tamanho_maximo(self, valor):

		if len(unicode(valor)) > self.tamanho:
			return TamanhoInvalido(self.codigo, self.nome, valor, tam_max=self.tamanho)

	def _valida(self, valor):
		# rezeta
		self._alertas = []

		if self._testa_tamanho_maximo(valor):
			self._alertas.append(self._testa_tamanho_maximo(valor))

		return self._alertas == []

	def get_alertas(self):
		return self._alertas

	alertas = property(get_alertas)

	def set_valor(self, novo_valor):
		if novo_valor is not None:
			#
			# Remover caratceres inválidos
			#
			for c in novo_valor:
				if c > 'ÿ':
					raise ErroCaracterInvalido(self.codigo, self.nome, novo_valor, c)

		novo_valor = novo_valor or u''
		if self._valida(novo_valor):
			novo_valor = unicode(tirar_acentos(novo_valor))

		# conforme a FEBRABAN, completa à direita do texto, com espaços em branco
		self._valor_string = novo_valor.ljust(self.tamanho, u' ').upper()

	def get_valor(self):
		return unicode(por_acentos(self._valor_string))

	valor = property(get_valor, set_valor)

	def __unicode__(self):
		return unicode(self._valor_string)

	def __repr__(self):
		return self.__unicode__()

	def get_text(self):
		return u'(%s-%s)[%s:%s][%s] %s=%s\n' % (self.codigo, self.descricao, self.de, self.ate, self.tamanho, self.nome, self._valor_string)

	text = property(get_text)

	def get_txt(self):
		return self._valor_string

	def set_txt(self, arquivo, ocorrencia=1):
		if self._le_txt(arquivo):
			self.valor = self._le_campo(self.tipo_registro, self.de, self.ate, ocorrencia=ocorrencia,
							segmento=self.segmento, operacao=self.operacao, lote=self.lote, num_seq=self.num_seq)

	txt = property(get_txt, set_txt)


class TagBoolean(TagCaracter):
	def __init__(self, **kwargs):
		super(TagBoolean, self).__init__(**kwargs)
		self._valor_boolean = None
		# Codigo para dinamizar a criacao de instancias de entidade,
		# aplicando os valores dos atributos na instanciacao
		for k, v in kwargs.items():
			setattr(self, k, v)

		if kwargs.has_key('valor'):
			self.valor = kwargs['valor']


	def _testa_obrigatorio(self, valor):
		# No caso da tag booleana, False deve ser tratado como preenchido
		if self.obrigatorio and (valor is None):
			return ErroObrigatorio(self.raiz, self.codigo, self.nome, self.propriedade)

	def _valida(self, valor):
		self._alertas = []

		if self._testa_obrigatorio(valor):
			self.alertas.append(self._testa_obrigatorio(valor))

		return self.alertas == []

	def set_valor(self, novo_valor):
		if isinstance(novo_valor, basestring):
			if novo_valor.lower() == 'true':
				novo_valor = True
			elif novo_valor.lower() == 'false':
				novo_valor = False
			else:
				novo_valor = None

		if isinstance(novo_valor, bool) and self._valida(novo_valor):
			self._valor_boolean = novo_valor

			if novo_valor == None:
				self._valor_string = ''
			elif novo_valor:
				self._valor_string = 'true'
			else:
				self._valor_string = 'false'
		else:
			self._valor_boolean = None
			self._valor_string = ''

	def get_valor(self):
		return self._valor_boolean

	valor = property(get_valor, set_valor)

	def __unicode__(self):
		if (not self.obrigatorio) and (self.valor == None):
			texto = ''
		else:
			texto = '<%s' % self.nome

			if self.propriedade:
				texto += ' %s="%s">' % (self.propriedade, self._valor_string)
			elif not self.valor == None:
				texto += '>%s</%s>' % (self._valor_string, self.nome)
			else:
				texto += ' />'

		return texto


class TagData(TagCaracter):
	def __init__(self, *args, **kwargs):
		super(TagData, self).__init__(*args, **kwargs)
		self._valor_data = None

		# Codigo para dinamizar a criacao de instancias de entidade,
		# aplicando os valores dos atributos na instanciacao
		for k, v in kwargs.items():
			setattr(self, k, v)

		if kwargs.has_key('valor'):
			self.valor = kwargs['valor']

	def _valida(self, valor):
		self._alertas = []
		return self._alertas == []

	def set_valor(self, novo_valor):
		if isinstance(novo_valor, basestring) and self._valida(novo_valor):
			# 	exessao, aqui permite ser preenchido com ZEROS
			if novo_valor and novo_valor != u'00000000' and self._valida(novo_valor):
				novo_valor = datetime.strptime(novo_valor, u'%d%m%Y')

			else:
				novo_valor = None

		if isinstance(novo_valor, (datetime, date,)) and self._valida(novo_valor):
			self._valor_data = novo_valor
			# Cuidado!!!
			# Aqui não dá pra usar a função strftime pois em alguns
			# casos a data retornada é 01/01/0001 00:00:00
			# e a função strftime só aceita data com anos a partir de 1900
			self._valor_string = '%02d%02d%04d' % (self._valor_data.day, self._valor_data.month, self._valor_data.year)
		else:
			self._valor_data = None
			self._valor_string = u'0'.rjust(self.tamanho, u'0')

	def get_valor(self):
		return self._valor_data

	valor = property(get_valor, set_valor)

	def get_txt(self):
		return self._valor_string

	def set_txt(self, arquivo, ocorrencia=1):
		if self._le_txt(arquivo):
			valor = self._le_campo(self.tipo_registro, self.de, self.ate, ocorrencia=ocorrencia,
							segmento=self.segmento, operacao=self.operacao, lote=self.lote, num_seq=self.num_seq)
			try:
				self.valor = valor
			except:
				self._alertas.append(ErroFormatoInvalido(self.codigo, self.nome, valor, u'Data: ddmmAAAA'))

	txt = property(get_txt, set_txt)

class TagHora(TagData):
	def set_valor(self, novo_valor):
		if isinstance(novo_valor, basestring) and self._valida(novo_valor):
			if novo_valor:
				novo_valor = datetime.strptime(novo_valor, '%H%M%S')
			else:
				novo_valor = None

		if isinstance(novo_valor, (datetime, time,)) and self._valida(novo_valor):
			self._valor_data = novo_valor
			# Cuidado!!!
			# Aqui não dá pra usar a função strftime pois em alguns
			# casos a data retornada é 01/01/0001 00:00:00
			# e a função strftime só aceita data com anos a partir de 1900
			self._valor_string = '%02d%02d%02d' % (self._valor_data.hour, self._valor_data.minute, self._valor_data.second)
		else:
			self._valor_data = None
			self._valor_string = u'0'.rjust(self.tamanho, u'0')

	def get_valor(self):
		return self._valor_data

	valor = property(get_valor, set_valor)

# class TagDataHora(TagData):
# 	def set_valor(self, novo_valor):
# 		if isinstance(novo_valor, basestring):
# 			if novo_valor:
# 				novo_valor = datetime.strptime(novo_valor, '%Y-%m-%dT%H:%M:%S')
# 			else:
# 				novo_valor = None
#
# 		if isinstance(novo_valor, datetime) and self._valida(novo_valor):
# 			self._valor_data = novo_valor
# 			self._valor_data = self._valor_data.replace(microsecond=0)
# 			# Cuidado!!!
# 			# Aqui não dá pra usar a função strftime pois em alguns
# 			# casos a data retornada é 01/01/0001 00:00:00
# 			# e a função strftime só aceita data com anos a partir de 1900
# 			self._valor_string = '%04d-%02d-%02dT%02d:%02d:%02d' % (self._valor_data.year, self._valor_data.month, self._valor_data.day,
# 																	self._valor_data.hour, self._valor_data.minute, self._valor_data.second)
# 		else:
# 			self._valor_data = None
# 			self._valor_string = ''
#
# 	def get_valor(self):
# 		return self._valor_data
#
# 	valor = property(get_valor, set_valor)
#
# 	def formato_danfe(self):
# 		if self._valor_data is None:
# 			return ''
# 		else:
# 			return self._valor_data.strftime('%d/%m/%Y %H:%M:%S')
#

# class TagDataHoraUTC(TagData):
# 	def __init__(self, **kwargs):
# 		super(TagDataHoraUTC, self).__init__(**kwargs)
# 		#
# 		# Expressão de validação do formato (vinda do arquivo leiauteSRE_V1.00.xsd
# 		# Alterada para tornar a informação do fuso horário opcional
# 		#
# 		self._validacao = re.compile(r'(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d(-0[1-4]:00)?')
# 		self._valida_fuso = re.compile(r'.*-0[1-4]:00$')
# 		self._brasilia = pytz.timezone('America/Sao_Paulo')
# 		self.fuso_horario = 'America/Sao_Paulo'
#
# 	def set_valor(self, novo_valor):
# 		if isinstance(novo_valor, basestring):
# 			if self._validacao.match(novo_valor):
# 				if self._valida_fuso.match(novo_valor):
# 					#
# 					# Extrai e determina qual o fuso horário informado
# 					#
# 					self.fuso_horario = novo_valor[19:]
# 					novo_valor = novo_valor[:19]
#
# 				#
# 				# Converte a data sem fuso horário para o fuso horário atual
# 				# Isso é necessário pois a função strptime ignora a informação
# 				# do fuso horário na string de entrada
# 				#
# 				novo_valor = self.fuso_horario.localize(datetime.strptime(novo_valor, '%Y-%m-%dT%H:%M:%S'))
# 			else:
# 				novo_valor = None
#
# 		if isinstance(novo_valor, datetime) and self._valida(novo_valor):
# 			self._valor_data = novo_valor
# 			self._valor_data = self._valor_data.replace(microsecond=0)
# 			try:
# 				self._valor_data = self.fuso_horario.localize(self._valor_data)
# 			except:
# 				pass
# 			# Cuidado!!!
# 			# Aqui não dá pra usar a função strftime pois em alguns
# 			# casos a data retornada é 01/01/0001 00:00:00
# 			# e a função strftime só aceita data com anos a partir de 1900
# 			#self._valor_string = '%04d-%02d-%02dT%02d:%02d:%02d' % (self._valor_data.year, self._valor_data.month, self._valor_data.day,
# 			#    self._valor_data.hour, self._valor_data.minute, self._valor_data.second)
#
# 			self._valor_string = self._valor_data.isoformat()
# 		else:
# 			self._valor_data = None
# 			self._valor_string = ''
#
# 	def get_valor(self):
# 		return self._valor_data
#
# 	valor = property(get_valor, set_valor)
#
# 	def set_fuso_horaro(self, novo_valor):
# 		if novo_valor in pytz.country_timezones['br']:
# 			self._fuso_horario = pytz.timezone(novo_valor)
#
# 		#
# 		# Nos valores abaixo, não entendi ainda até agora, mas para o resultado
# 		# correto é preciso usar GMT+ (mais), não (menos) como seria de se
# 		# esperar...
# 		#
# 		elif novo_valor == '-04:00' or novo_valor == '-0400':
# 			self._fuso_horario = pytz.timezone('Etc/GMT+4')
# 		elif novo_valor == '-03:00' or novo_valor == '-0300':
# 			self._fuso_horario = pytz.timezone('Etc/GMT+3')
# 		elif novo_valor == '-02:00' or novo_valor == '-0200':
# 			self._fuso_horario = pytz.timezone('Etc/GMT+2')
# 		elif novo_valor == '-01:00' or novo_valor == '-0100':
# 			self._fuso_horario = pytz.timezone('Etc/GMT+1')
#
# 	def get_fuso_horario(self):
# 		return self._fuso_horario
#
# 	fuso_horario = property(get_fuso_horario, set_fuso_horaro)
#
# 	def formato_danfe(self):
# 		if self._valor_data is None:
# 			return ''
# 		else:
# 			valor = self._brasilia.normalize(self._valor_data).strftime('%d/%m/%Y %H:%M:%S %Z (%z)')
# 			#
# 			# Troca as siglas:
# 			# BRT - Brasília Time -> HOB - Horário Oficial de Brasília
# 			# BRST - Brasília Summer Time -> HVOB - Horário de Verão Oficial de Brasília
# 			# AMT - Amazon Time -> HOA - Horário Oficial da Amazônia
# 			# AMST - Amazon Summer Time -> HVOA - Horário de Verão Oficial da Amazônia
# 			# FNT - Fernando de Noronha Time -> HOFN - Horário Oficial de Fernando de Noronha
# 			#
# 			valor = valor.replace('(-0100)', '(-01:00)')
# 			valor = valor.replace('(-0200)', '(-02:00)')
# 			valor = valor.replace('(-0300)', '(-03:00)')
# 			valor = valor.replace('(-0400)', '(-04:00)')
# 			valor = valor.replace('BRT', 'HOB')
# 			valor = valor.replace('BRST', 'HVOB')
# 			valor = valor.replace('AMT', 'HOA')
# 			valor = valor.replace('AMST', 'HVOA')
# 			valor = valor.replace('FNT', 'HOFN')
# 			return valor


class TagInteiro(TagCaracter):
	def __init__(self, *args, **kwargs):
		super(TagInteiro, self).__init__(* args, **kwargs)

		self._valor_inteiro = 0
		self._valor_string = u'0'.rjust(self.tamanho, u'0')

		# Codigo para dinamizar a criacao de instancias de entidade,
		# aplicando os valores dos atributos na instanciacao
		for k, v in kwargs.items():
			setattr(self, k, v)

		if kwargs.has_key(u'valor'):
			self.valor = kwargs[u'valor']

	def set_valor(self, novo_valor):
		if isinstance(novo_valor, basestring) and self._valida(novo_valor):
			if novo_valor.isdigit():
				novo_valor = int(novo_valor)
			else:
				novo_valor = 0

		if isinstance(novo_valor, (int, long, Decimal)) and self._valida(novo_valor):
			self._valor_inteiro = novo_valor
		else:
			self._valor_inteiro = 0

		# conforme a FEBRABAN, preenche com ZEROS à esquerda
		self._valor_string = unicode(self._valor_inteiro).rjust(self.tamanho, u'0')

	def get_valor(self):
		return self._valor_inteiro

	valor = property(get_valor, set_valor)

	def _valida(self, valor):
		"""
		É separado pois o intero só nao tem valor se for '' ou None
		:param valor:
		:return:
		"""
		self._alertas = []

		# converte para string antes de passar nos validador

		if self._testa_tamanho_maximo(unicode(valor)):
			self._alertas.append(self._testa_tamanho_maximo(valor))

		return self._alertas == []

class TagDecimal(TagCaracter):
	def __init__(self, *args, **kwargs):
		"""
		Os decimais possui um tamanho maior
			[de-1:ate] 	+	decimais
			TAMANHO 	+	DECIMAIS
		"""

		self._valor_decimal = Decimal(u'0.0')
		self.casas_decimais = kwargs.pop(u'casas_decimais', 2)

		super(TagDecimal, self).__init__(*args, **kwargs)

		self._valor_decimal = Decimal(u'0.0')
		self._valor_string = self._formata(self._valor_decimal)

		# Codigo para dinamizar a criacao de instancias de entidade,
		# aplicando os valores dos atributos na instanciacao
		for k, v in kwargs.items():
			setattr(self, k, v)

	def _parte_inteira(self, valor=None):
		if valor is None:
			valor = self._valor_decimal

		valor = unicode(valor).strip()

		if u'.' in valor:
			valor = valor.split(u'.')[0]

		# -----------------------------------------------
		# 	zeros a esquerda - 'xxx0.'
		# -----------------------------------------------
		return valor.rjust(self.tamanho - self.casas_decimais, u'0')

	def _parte_decimal(self, valor=None):
		if valor is None:
			valor = self._valor_decimal

		valor = unicode(valor).strip()

		if u'.' in valor:
			valor = valor.split(u'.')[1]
		else:
			valor = u'0'

		# -----------------------------------------------
		# zeros para direita - '.0yyy'
		# -----------------------------------------------
		return valor.ljust(self.casas_decimais, u'0')

	def _formata(self, valor):
		texto = self._parte_inteira(valor)
		dec = self._parte_decimal(valor)

		texto += dec
		return texto

	# def _testa_decimais_minimo(self, decimal):
	# 	if self.decimais[0] and (len(decimal) < self.decimais[0]):
	# 		return TamanhoInvalido(self.codigo, self.nome, decimal, dec_min=self.decimais[0])

	def _testa_decimais_maximo(self, decimal):
		if len(decimal) > self.casas_decimais:
			return TamanhoInvalido(self.codigo, self.nome, decimal, dec_max=self.casas_decimais)

	def _valida(self, valor):
		self._alertas = []

		inteiro = self._parte_inteira(valor)
		decimal = self._parte_decimal(valor)

		if self._testa_tamanho_maximo(inteiro):
			self._alertas.append(self._testa_tamanho_maximo(inteiro))

		#
		# Analisando as exp.reg. de validação das tags com decimais,
		# parece haver um número máximo de casas decimais, mas as tags
		# podem ser enviadas sem nenhuma casa decimal, então, não
		# há um mínimo de casas decimais
		#
		#if self._testa_decimais_minimo(decimal):
		#    self.alertas.append(self._testa_decimais_minimo(decimal))

		if self._testa_decimais_maximo(decimal):
			self._alertas.append(self._testa_decimais_maximo(decimal))

		return self._alertas == []

	def set_valor(self, novo_valor):
		if isinstance(novo_valor, basestring) and self._valida(novo_valor):
			if novo_valor:
				# antes, tem que quebrar a string e organizar para gerar o DECIMAL, se for o caso
				# 123456 -> 1234.56
				novo_valor = u'%s.%s' % (
					novo_valor[:-self.casas_decimais],	# parte inteira
					novo_valor[-self.casas_decimais:]	# parte decimal
				)
				novo_valor = Decimal(novo_valor)
			else:
				novo_valor = Decimal('0.0')

		if isinstance(novo_valor, (int, long, Decimal)) and self._valida(novo_valor):
			self._valor_decimal = Decimal(novo_valor)
			self._valor_string = self._formata(self._valor_decimal)
		else:
			self._valor_decimal = Decimal('0.0')
			self._valor_string = self._formata(self._valor_decimal)

	def get_valor(self):
		return self._valor_decimal

	valor = property(get_valor, set_valor)

	def get_txt(self):
		return self._valor_string

	def set_txt(self, arquivo, ocorrencia=1):
		if self._le_txt(arquivo):
			valor = self._le_campo(self.tipo_registro, self.de, self.ate, ocorrencia=ocorrencia,
							segmento=self.segmento, operacao=self.operacao, lote=self.lote, num_seq=self.num_seq)
			try:
				self.valor = valor
			except:
				self._alertas.append(ErroFormatoInvalido(self.codigo, self.nome, valor, u'Decimal'))

	txt = property(get_txt, set_txt)

class TXT(RegistroTXT):
	def __init__(self, *args, **kwargs):
		super(TXT, self).__init__(*args, **kwargs)
		self._txt = None
		self._alertas = []

	def get_txt(self):
		# self.alertas = []
		return self._txt

	def le_grupo(self, tipo_registro, classe_grupo, segmento=None, operacao=None):
		tags = []

		grupos = self._le_nohs(tipo_registro, segmento=segmento, operacao=operacao)

		if grupos is not None:
			tags = [classe_grupo() for g in grupos]
			for i in range(len(grupos)):
				tags[i].txt = grupos[i]

		return tags
