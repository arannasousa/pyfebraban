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
from .celular import Celular

class DadosDestinatario(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y'):
		super(DadosDestinatario, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.email		= TagCaracter(self._tipo_registro, u'09.4Y', u'email', 		 20,  69, descricao=u'*G032', comentario=u'E-mail para envio da informacao', segmento=self._segmento, lote=self._lote, num_seq=self._num_seq)
		self.celular 	= Celular(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.email.txt
		txt += self.celular.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.email.txt = arquivo
			self.celular.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.email.alertas)
		alertas.extend(self.celular.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.email.text)
		txt += self.celular.text
		return txt

	text = property(get_text)