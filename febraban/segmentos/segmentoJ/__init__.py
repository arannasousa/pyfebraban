# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagCaracter, TagInteiro, TagDecimal, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text, CODIGO_MOEDA

from .controle import Controle
from .servico import Servico
from .pagamento import Pagamento

class SegmentoJ(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'J'):
		super(SegmentoJ, self).__init__()

		self._lote = lote
		self._num_seq = num_seq		# numero sequencial do registro no lote
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.controle			= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico			= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.pagamento			= Pagamento(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nosso_numero		= TagCaracter(self._tipo_registro, u'18.3J', u'nosso_numero', 203, 222, descricao=u'*G043', comentario=u'Nº do docto atribuído pelo banco', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_moeda		= TagInteiro(self._tipo_registro, u'19.3J', u'codigo_moeda',  223, 224, descricao=u'*G065', comentario=u'Código de moeda', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq, valor=CODIGO_MOEDA.REAL)
		self.CNAB203			= TagCaracter(self._tipo_registro, u'20.3J', u'CNAB203', 	  225, 230, descricao=u'G004', comentario=u'Uso Exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.ocorrencias		= TagCaracter(self._tipo_registro, u'21.3J', u'ocorrencias',  231, 240, descricao=u'*G059', comentario=u'Códigos das ocorrências p/ retorno', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):

		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.pagamento.txt
		txt += self.nosso_numero.txt
		txt += self.codigo_moeda.txt
		txt += self.CNAB203.txt
		txt += self.ocorrencias.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.pagamento.txt = arquivo
			self.nosso_numero.txt = arquivo
			self.codigo_moeda.txt = arquivo
			self.CNAB203.txt = arquivo
			self.ocorrencias.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.pagamento.alertas)
		alertas.extend(self.nosso_numero.alertas)
		alertas.extend(self.codigo_moeda.alertas)
		alertas.extend(self.CNAB203.alertas)
		alertas.extend(self.ocorrencias.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += self.pagamento.text
		txt += gera_text(NIVEIS.N3, self.nosso_numero.text)
		txt += gera_text(NIVEIS.N3, self.codigo_moeda.text)
		txt += gera_text(NIVEIS.N3, self.CNAB203.text)
		txt += gera_text(NIVEIS.N3, self.ocorrencias.text)
		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro