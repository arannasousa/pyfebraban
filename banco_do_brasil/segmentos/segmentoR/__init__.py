# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.base import (TagCaracter, TagInteiro, TXT)
from ....febraban import TIPO_REGISTRO, NIVEIS, gera_text

from ....febraban.segmentos import segmentoR

from .controle import Controle
from .servico import Servico
from .desc2 import Desconto2
from .desc3 import Desconto3
from .multa import Multa
from .dados_debito import DadosDebito

class SegmentoR(segmentoR.SegmentoR):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):

		super(SegmentoR, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.controle					= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico					= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.desconto2					= Desconto2(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.desconto3					= Desconto3(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.multa						= Multa(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dados_debito				= DadosDebito(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.desconto2.txt
		txt += self.desconto3.txt
		txt += self.multa.txt
		txt += self.informacao_ao_sacado.txt
		txt += self.informacao3.txt
		txt += self.informacao4.txt
		txt += self.CNAB203R.txt
		txt += self.codigo_ocorrencia_sacado.txt
		txt += self.dados_debito.txt
		txt += self.identific_emissao_aviso_debito.txt
		txt += self.CNAB293R.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.desconto2.txt = arquivo
			self.desconto3.txt = arquivo
			self.multa.txt = arquivo
			self.informacao_ao_sacado.txt = arquivo
			self.informacao3.txt = arquivo
			self.informacao4.txt = arquivo
			self.CNAB203R.txt = arquivo
			self.codigo_ocorrencia_sacado.txt = arquivo
			self.dados_debito.txt = arquivo
			self.identific_emissao_aviso_debito.txt = arquivo
			self.CNAB293R.txt = arquivo
	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.desconto2.alertas)
		alertas.extend(self.desconto3.alertas)
		alertas.extend(self.multa.alertas)
		alertas.extend(self.informacao_ao_sacado.alertas)
		alertas.extend(self.informacao3.alertas)
		alertas.extend(self.informacao4.alertas)
		alertas.extend(self.CNAB203R.alertas)
		alertas.extend(self.codigo_ocorrencia_sacado.alertas)
		alertas.extend(self.dados_debito.alertas)
		alertas.extend(self.identific_emissao_aviso_debito.alertas)
		alertas.extend(self.CNAB293R.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += self.desconto2.text
		txt += self.desconto3.text
		txt += self.multa.text
		txt += gera_text(NIVEIS.N3, self.informacao_ao_sacado.text)
		txt += gera_text(NIVEIS.N3, self.informacao3.text)
		txt += gera_text(NIVEIS.N3, self.informacao4.text)
		txt += gera_text(NIVEIS.N3, self.CNAB203R.text)
		txt += gera_text(NIVEIS.N3, self.codigo_ocorrencia_sacado.text)
		txt += self.dados_debito.text
		txt += gera_text(NIVEIS.N3, self.identific_emissao_aviso_debito.text)
		txt += gera_text(NIVEIS.N3, self.CNAB293R.text)
		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro