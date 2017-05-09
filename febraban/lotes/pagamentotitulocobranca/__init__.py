# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagData, TagHora, TagInteiro, TXT, TagCaracter)
from ... import TIPO_REGISTRO, TIPO_OPERACAO, NIVEIS, gera_text, TIPO_SERVICO
from .header import LoteHeader
from .trailer import LoteTrailer

# from .registro_inicial import RegistroInicial
# from .registro_final import RegistroFinal
from ... import segmentos

class PagamentoTituloCobranca(TXT):
	def __init__(self, lote=u'0001'):
		super(PagamentoTituloCobranca, self).__init__()

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._lote = lote

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.header 			= LoteHeader(lote=self._lote)
		self.registros_iniciais = []
		self.segmentos			= []
		self.registros_finais	= []
		self.trailer			= LoteTrailer(lote=self._lote)

	@property
	def loteCorreto(self):
		"""
		Checa se as informacoes passadas são mesmos deste lote

		Essa checagem é devido alguns lotes específicos possuirem campos em diferentes posições, dificultando
		a padronização

		:return:	True or False
		:rtype:		bool
		"""

		# --------------------------------------------------------
		# 	lote nao possui servico especifico
		# --------------------------------------------------------
		# if self.header.controle.tipo_servico == u' ':
		#	pass

		# --------------------------------------------------------
		# 	lote possui tipo de operacao - Remessa / Retorno
		# --------------------------------------------------------
		if self.header.servico.operacao.valor in (TIPO_OPERACAO.ARQUIVO_REMESSA, TIPO_OPERACAO.ARQUIVO_RETORNO)\
				and \
			self.header.servico.servico.valor == int(TIPO_SERVICO.PAGAMENTOS_DIVERSOS):
			# 98 - arquivo de remessa definido no banco do brasil
			return True

		return False

	def get_txt(self):

		txt = u''
		txt += self.header.txt
		txt += u'\n'

		for ri in self.registros_iniciais:
			txt += ri.txt
			txt += u'\n'

		for seg in self.segmentos:
			txt += seg.txt
			txt += u'\n'

		for rf in self.registros_finais:
			txt += rf.txt
			txt += u'\n'

		txt += self.trailer.txt
		txt += u'\n'

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.header.txt = arquivo

			# -------------------------------------------------------------------------------------
			# 	para cada registro encontrado, enumera - "pelo manual só deve ter no maximo 1"
			# -------------------------------------------------------------------------------------
			# for i, l in enumerate(self._le_nohs(TIPO_REGISTRO.LOTE_INICIO), start=1):
			# 	self.registros_iniciais.append(RegistroInicial(lote=i))

			# -------------------------------------------------------------------------------------
			# 	busca os segmentos, nao importando a ordem ou numeracao
			# 	desde que, pertenca a este lote
			# -------------------------------------------------------------------------------------
			for tipo_segmento in self._le_nohs(TIPO_REGISTRO.SEGMENTO, lote=self._lote):
				# -----------------------------------------------------------
				# 	carrega cada CLASSE de SEGMENTO para checar se
				# 	nesse arquivo possui varios segmentos distintos
				# -----------------------------------------------------------
				# 	este tipo de LOTE só possui 1 segmento principal
				# -----------------------------------------------------------
				for C in (segmentos.SegmentoJ, ):
					# -----------------------------------------------------------
					# 	colocar None para nao FILTRAR de mais,
					# pois ele ja comeca em '00001' e nossa intencao é checar apenas o segmento u'J'
					# -----------------------------------------------------------
					s = C(num_seq=None)
					s.txt = tipo_segmento

					if s.segmentoCorreto:
						# ---------------------------------------------------
						# 	extrai o numero sequencial correto - 00001-99999
						# ---------------------------------------------------
						pos_num_seq_de = s.servico.numero_registro.de - 1
						pos_num_seq_ate = s.servico.numero_registro.ate

						n_seq = tipo_segmento[pos_num_seq_de: pos_num_seq_ate]

						# ---------------------------------------------------
						# 	agora sim, especifica o LOTE certo e sua NUM_SEQ
						# ---------------------------------------------------
						s = C(lote=self._lote, num_seq=n_seq)
						# ---------------------------------------------------
						# 	conteudo completo
						# ---------------------------------------------------
						s.txt = arquivo
						self.segmentos.append(s)

			# for i, l in enumerate(self._le_nohs(TIPO_REGISTRO.LOTE_FINAL), start=1):
			# 	self.registros_finais.append(RegistroFinal(lote=i))

			self.trailer.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.header.alertas)

		for ri in self.registros_iniciais:
			alertas.extend(ri.alertas)

		for seg in self.segmentos:
			alertas.extend(seg.alertas)

		for rf in self.registros_finais:
			alertas.extend(rf.alertas)

		alertas.extend(self.trailer.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N1, unicode(__name__) + u'\n')
		txt += self.header.text

		for ri in self.registros_iniciais:
			txt += ri.text

		for seg in self.segmentos:
			txt += seg.text

		for rf in self.registros_finais:
			txt += rf.text

		txt += self.trailer.text

		return txt

	text = property(get_text)