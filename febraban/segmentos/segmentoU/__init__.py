# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagCaracter, TagInteiro, TagDecimal, TagData, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text, CODIGO_MOEDA

from .controle import Controle
from .servico import Servico
from .dados_titulo import DadosTitulo
from .ocorrencia_sacado import OcorrenciaSacado

class SegmentoU(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'U'):
		super(SegmentoU, self).__init__()

		self._lote = lote
		self._num_seq = num_seq		# numero sequencial do registro no lote
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.controle			= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico			= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dados_titulo		= DadosTitulo(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.outras_despesas	= TagDecimal(self._tipo_registro, 	u'14.3U', u'outras_despesas', 108, 122, descricao=u'C054', comentario=u'Valor de outras despesas', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.outros_creditos	= TagDecimal(self._tipo_registro,	u'15.3U', u'outros_creditos', 123, 137, descricao=u'C055', comentario=u'Valor de outros créditos', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.data_ocorrencia	= TagData(self._tipo_registro,		u'16.3U', u'data_ocorrencia', 138, 145, descricao=u'C056', comentario=u'Data da ocorrência', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.data_credito		= TagData(self._tipo_registro,		u'17.3U', u'data_credito',	  146, 153, descricao=u'C057', comentario=u'Data da efetivação do crédito', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.ocorrencia_sacado	= OcorrenciaSacado(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_banco_correpondente			= TagInteiro(self._tipo_registro,	u'22.3U', u'codigo_banco_correpondente', 		211, 213, descricao=u'*C031', comentario=u'Código banco correspondente compensação', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nosso_numero_banco_correspondente	= TagInteiro(self._tipo_registro,	u'23.3U', u'nosso_numero_banco_correspondente', 214, 233, descricao=u'*C032', comentario=u'Nosso número banco correspondente', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB243			= TagCaracter(self._tipo_registro, 	u'24.3U', u'CNAB243', 		  234, 240, descricao=u'G004', comentario=u'Uso Exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):

		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.dados_titulo.txt
		txt += self.outras_despesas.txt
		txt += self.outros_creditos.txt
		txt += self.data_ocorrencia.txt
		txt += self.data_credito.txt
		txt += self.ocorrencia_sacado.txt
		txt += self.codigo_banco_correpondente.txt
		txt += self.nosso_numero_banco_correspondente.txt
		txt += self.CNAB243.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.dados_titulo.txt = arquivo
			self.outras_despesas.txt = arquivo
			self.outros_creditos.txt = arquivo
			self.data_ocorrencia.txt = arquivo
			self.data_credito.txt = arquivo
			self.ocorrencia_sacado.txt = arquivo
			self.codigo_banco_correpondente.txt = arquivo
			self.nosso_numero_banco_correspondente.txt = arquivo
			self.CNAB243.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.dados_titulo.alertas)
		alertas.extend(self.outras_despesas.alertas)
		alertas.extend(self.outros_creditos.alertas)
		alertas.extend(self.data_ocorrencia.alertas)
		alertas.extend(self.data_credito.alertas)
		alertas.extend(self.ocorrencia_sacado.alertas)
		alertas.extend(self.codigo_banco_correpondente.alertas)
		alertas.extend(self.nosso_numero_banco_correspondente.alertas)
		alertas.extend(self.CNAB243.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += self.dados_titulo.text
		txt += gera_text(NIVEIS.N3, self.outras_despesas.text)
		txt += gera_text(NIVEIS.N3, self.outros_creditos.text)
		txt += gera_text(NIVEIS.N3, self.data_ocorrencia.text)
		txt += gera_text(NIVEIS.N3, self.data_credito.text)
		txt += self.ocorrencia_sacado.text
		txt += gera_text(NIVEIS.N3, self.codigo_banco_correpondente.text)
		txt += gera_text(NIVEIS.N3, self.nosso_numero_banco_correspondente.text)
		txt += gera_text(NIVEIS.N3, self.CNAB243.text)
		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro