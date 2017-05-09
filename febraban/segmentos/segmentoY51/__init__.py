# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagCaracter, TagInteiro, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text, C040

from .controle import Controle
from .servico import Servico
from .notas_fiscais import NotasFiscais

class SegmentoY51(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y', seg_opcional=u'51'):
		super(SegmentoY51, self).__init__()

		self._lote = lote
		self._num_seq = num_seq		# numero sequencial do registro no lote
		self._segmento = segmento

		self._codigo_registro_opcional = seg_opcional
		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		# 	tag CHAVE, com essa informacao, as tags seguintes podem variar
		self.codigo_registro_opcional	= TagInteiro(self._tipo_registro, 	u'08.3Y', u'codigo_registro_opcional',	 18,  19, descricao=u'*G067', comentario=u'Identificação registro opcional', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq, valor=self._codigo_registro_opcional)

		self.notas_fiscais			= NotasFiscais(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB243Y				= TagCaracter(self._tipo_registro, 	u'24.3Y', u'CNAB243Y',						210, 240, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.codigo_registro_opcional.txt
		txt += self.notas_fiscais.txt
		txt += self.CNAB243Y.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.codigo_registro_opcional.txt = arquivo
			self.notas_fiscais.txt = arquivo
			self.CNAB243Y.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.codigo_registro_opcional.alertas)
		alertas.extend(self.notas_fiscais.alertas)
		alertas.extend(self.CNAB243Y.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += gera_text(NIVEIS.N3, self.codigo_registro_opcional.text)
		txt += self.notas_fiscais.text
		txt += gera_text(NIVEIS.N3, self.CNAB243Y.text)

		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro and \
				unicode(self.codigo_registro_opcional.valor).zfill(2) == self._codigo_registro_opcional