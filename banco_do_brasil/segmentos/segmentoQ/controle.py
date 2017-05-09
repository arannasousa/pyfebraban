# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...constantes import CODIGO_BANCO
from ....febraban.base import (TagInteiro)
from ....febraban import NIVEIS, gera_text

from ....febraban.segmentos.segmentoQ import controle

class Controle(controle.Controle):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Q'):
		super(Controle, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.banco		= TagInteiro(self._tipo_registro, u'01.3Q', u'banco', 		1, 3, descricao=u'G001', comentario=u'Código do banco na compensação', segmento=self._segmento, lote=self._lote, num_seq=num_seq, valor=CODIGO_BANCO)

	def get_txt(self):
		txt = u''
		txt += self.banco.txt
		txt += self.lote.txt
		txt += self.registro.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.banco.txt = arquivo
			self.lote.txt = arquivo
			self.registro.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.banco.alertas)
		alertas.extend(self.lote.alertas)
		alertas.extend(self.registro.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.banco.text)
		txt += gera_text(NIVEIS.N4, self.lote.text)
		txt += gera_text(NIVEIS.N4, self.registro.text)
		return txt

	text = property(get_text)