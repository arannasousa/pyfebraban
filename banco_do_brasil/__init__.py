# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ..febraban import TIPO_REGISTRO, NIVEIS, gera_text
from ..febraban import Arquivo
from .header import ArquivoHeader
from .trailer import ArquivoTrailer
from . import lotes

class ArquivoBB(Arquivo):
	def __init__(self):
		super(Arquivo, self).__init__()

		self.header = ArquivoHeader()

		self.lotes = []

		self.trailer = ArquivoTrailer()

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.header.txt = arquivo

			# -------------------------------------------------------------------------------------
			# 	busca tudo quanto é lote, nao importanto qual o tipo de lote ou numeracao
			# -------------------------------------------------------------------------------------
			for lote in self._le_nohs(TIPO_REGISTRO.LOTE_HEADER):
				# -----------------------------------------------------------
				# 	carrega cada CLASSE DE LOTE para checar se
				# 	nesse arquivo possui mais de vários lotes
				# -----------------------------------------------------------
				for C in (
						lotes.TituloCobranca,
					):
					# --------------------------------------
					# 	extrai a informacao do lote
					# --------------------------------------
					l = C()
					pos_lote_de = l.header.controle.lote.de - 1
					pos_lote_ate = l.header.controle.lote.ate
					n_lote = lote[pos_lote_de: pos_lote_ate]

					# --------------------------------------
					# 	reeinstancia
					# --------------------------------------
					l = C(lote=n_lote)
					l.txt = lote
					if l.loteCorreto:
						# --------------------------------------
						# 	add o conteudo completo
						# --------------------------------------
						l.txt = arquivo
						# --------------------------------------
						# 	add à lista de lotes
						# --------------------------------------
						self.lotes.append(l)


			self.trailer.txt = arquivo

	def get_txt(self):

		txt = u''
		txt += self.header.txt
		for l in self.lotes:
			txt += l.txt
		txt += self.trailer.txt
		return txt

	txt = property(get_txt, set_txt)