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

class TituloCobranca(TXT):
	def __init__(self, lote=u'0001'):
		super(TituloCobranca, self).__init__()
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._lote = lote

		# --------------------------------------------------------------------------------------
		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segumento=None, operacao=None
		# --------------------------------------------------------------------------------------
		self.header 			= LoteHeader(lote=self._lote)

		self.segmentos			= []

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
		# 	lote possui tipo de operacao - Remessa / Retorno
		# 	lote deve possuir serviço de COBRANÇA == u'01'
		# --------------------------------------------------------
		if self.header.servico.operacao.valor in (TIPO_OPERACAO.ARQUIVO_REMESSA, TIPO_OPERACAO.ARQUIVO_RETORNO)\
				and \
			self.header.servico.servico.valor == int(TIPO_SERVICO.COBRANCA):

			return True

		return False

	def get_txt(self):
		txt = u''
		txt += self.header.txt
		txt += u'\n'

		for seg in self.segmentos:
			txt += seg.txt
			txt += u'\n'

		txt += self.trailer.txt
		txt += u'\n'

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.header.txt = arquivo
			# -------------------------------------------------------------------------------------
			# 	aqui tem uma restricao sobre os segmentos, dependendo se for
			# 		REMESSA ou RETORNO
			# -------------------------------------------------------------------------------------
			if self.header.servico.operacao.valor == TIPO_OPERACAO.ARQUIVO_REMESSA:
				segmentosClasses = (
					segmentos.SegmentoP,
					segmentos.SegmentoQ,
					segmentos.SegmentoR,		# * opcional
					segmentos.SegmentoS,		# * opcional
					segmentos.SegmentoY01,		# * opcional
					segmentos.SegmentoY04,		# * opcional
					segmentos.SegmentoY50,		# * opcional
					segmentos.SegmentoY51,		# * opcional
				)
			elif self.header.servico.operacao.valor == TIPO_OPERACAO.ARQUIVO_RETORNO:
				segmentosClasses = (
					segmentos.SegmentoT,
					segmentos.SegmentoU,
					segmentos.SegmentoY01,		# * opcional
					segmentos.SegmentoY04,		# * opcional
					segmentos.SegmentoY05,		# *** opcional
					segmentos.SegmentoY50,		# * opcional
					segmentos.SegmentoY51,		# * opcional
				)
			else:
				segmentosClasses = ()

			# -------------------------------------------------------------------------------------
			# 	busca os segmentos, nao importando a ordem ou numeracao
			# 	desde que, pertenca a este lote
			# -------------------------------------------------------------------------------------
			for tipo_segmento in self._le_nohs(TIPO_REGISTRO.SEGMENTO, lote=self._lote):
				# -----------------------------------------------------------
				# 	carrega cada CLASSE de SEGMENTO para checar se
				# 	nesse arquivo possui varios segmentos distintos
				# -----------------------------------------------------------
				for C in segmentosClasses:
					# -----------------------------------------------------------
					# 	colocar None para nao FILTRAR de mais,
					# pois ele ja comeca em '00001' e nossa intencao é checar apenas o segmento u'J'
					# -----------------------------------------------------------
					s = C(lote=self._lote, num_seq=None)
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
						self.segmentos.append(C(lote=self._lote, num_seq=n_seq))

						# ---------------------------------------------------
						# 	add o conteudo apenas do segmento mesmo
						# ---------------------------------------------------
						self.segmentos[-1].txt = tipo_segmento
						# ---------------------------------------------------
						# 	add o conteudo completo no novo segmento
						# ---------------------------------------------------
						# self.segmentos[-1].txt = arquivo


			# for i, l in enumerate(self._le_nohs(TIPO_REGISTRO.LOTE_FINAL), start=1):
			# 	self.registros_finais.append(RegistroFinal(lote=i))

			self.trailer.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.header.alertas)

		for seg in self.segmentos:
			alertas.extend(seg.alertas)

		alertas.extend(self.trailer.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N1, unicode(__name__) + u'\n')
		txt += self.header.text

		for seg in self.segmentos:
			txt += seg.text

		txt += self.trailer.text

		return txt

	text = property(get_text)