# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban import NIVEIS, gera_text

from .....febraban.segmentos.segmentoQ import sacador_avalista

from .inscricao import Inscricao

class SacadorAvalista(sacador_avalista.SacadorAvalista):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Q'):
		super(SacadorAvalista, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.inscricao	= Inscricao(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.inscricao.txt
		txt += self.nome.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.inscricao.txt = arquivo
			self.nome.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.inscricao.alertas)
		alertas.extend(self.nome.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += self.inscricao.text
		txt += gera_text(NIVEIS.N4, self.nome.text)
		return txt

	text = property(get_text)