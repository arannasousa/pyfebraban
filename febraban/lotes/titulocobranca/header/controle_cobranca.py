# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'


from ....base import (TagData, TagInteiro, TXT)

from .... import TIPO_REGISTRO, NIVEIS, gera_text

class ControleCobranca(TXT):
	def __init__(self, lote=u'0001'):
		super(ControleCobranca, self).__init__()

		self._lote = lote
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.LOTE_HEADER

		self.numero_rem_ret		= TagInteiro(self._tipo_registro, u'20.1', 	u'numero_rem_ret',	184, 191, descricao=u'G079', comentario=u'Número remessa/retorno', lote=self._lote)
		self.data_gravacao		= TagData(self._tipo_registro, u'21.1', 	u'data_gravacao', 	192, 199, descricao=u'G068', comentario=u'Data de gravação remessa/retorno', lote=self._lote)

	def get_txt(self):

		txt = u''
		txt += self.numero_rem_ret.txt
		txt += self.data_gravacao.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.numero_rem_ret.txt = arquivo
			self.data_gravacao.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.numero_rem_ret.alertas)
		alertas.extend(self.data_gravacao.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.numero_rem_ret.text)
		txt += gera_text(NIVEIS.N4, self.data_gravacao.text)
		return txt

	text = property(get_text)