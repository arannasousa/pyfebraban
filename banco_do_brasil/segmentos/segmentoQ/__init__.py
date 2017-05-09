# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.base import (TagCaracter, TagInteiro)
from ....febraban import NIVEIS, gera_text

from ....febraban import segmentos

from .controle import Controle
from .servico import Servico
from .dados_sacado import DadosSacado
from .sacador_avalista import SacadorAvalista

class SegmentoQ(segmentos.SegmentoQ):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Q'):
		super(SegmentoQ, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dados_sacado 			= DadosSacado(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.sacador_avalista		= SacadorAvalista(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.banco_correspondente				= TagInteiro(self._tipo_registro, 	u'20.3Q', u'banco_correspondente',  			210, 212, descricao=u'*G069', comentario=u'Código do banco correspondente na compensação', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nosso_numero_banco_correspondente	= TagCaracter(self._tipo_registro, 	u'21.3Q', u'nosso_numero_banco_correspondente', 213, 232, descricao=u'*G069', comentario=u'Nosso número no banco correspondente', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB223Q							= TagCaracter(self._tipo_registro, 	u'22.3Q', u'CNAB223Q',							233, 240, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.dados_sacado.txt
		txt += self.sacador_avalista.txt
		txt += self.banco_correspondente.txt
		txt += self.nosso_numero_banco_correspondente.txt
		txt += self.CNAB223Q.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.dados_sacado.txt = arquivo
			self.sacador_avalista.txt = arquivo
			self.banco_correspondente.txt = arquivo
			self.nosso_numero_banco_correspondente.txt = arquivo
			self.CNAB223Q.txt = arquivo
	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.dados_sacado.alertas)
		alertas.extend(self.sacador_avalista.alertas)
		alertas.extend(self.banco_correspondente.alertas)
		alertas.extend(self.nosso_numero_banco_correspondente.alertas)
		alertas.extend(self.CNAB223Q.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += self.dados_sacado.text
		txt += self.sacador_avalista.text
		txt += gera_text(NIVEIS.N3, self.banco_correspondente.text)
		txt += gera_text(NIVEIS.N3, self.nosso_numero_banco_correspondente.text)
		txt += gera_text(NIVEIS.N3, self.CNAB223Q.text)
		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro