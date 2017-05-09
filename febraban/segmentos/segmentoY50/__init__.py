# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagCaracter, TagInteiro, TagData, TagDecimal, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text, C062

from .controle import Controle
from .servico import Servico
from .conta_corrente_mantenedora import ContaCorrenteMantenedora
from .conta_corrente_beneficiario import ContaCorrenteBeneficiario

class SegmentoY50(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Y', seg_opcional=u'50'):
		super(SegmentoY50, self).__init__()

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
		# -------------------------------------------------------------------------------------
		# 	tag CHAVE, com essa informacao, as tags seguintes podem variar
		# -------------------------------------------------------------------------------------
		self.codigo_registro_opcional		= TagInteiro(self._tipo_registro, 	u'08.3Y', u'codigo_registro_opcional',	 18,  19, descricao=u'*G067', comentario=u'Identificação registro opcional', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq, valor=self._codigo_registro_opcional)
		self.conta_corrente_mantenedora		= ContaCorrenteMantenedora(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nosso_numero					= TagCaracter(self._tipo_registro, 	u'14.3Y', u'nosso_numero',		 40,  59, descricao=u'*G069', comentario=u'Identificação do título no banco', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.calculo_rateio_beneficiario	= TagInteiro(self._tipo_registro, 	u'15.3Y', u'calculo_rateio_beneficiario',	60, 60, descricao=u'C061', comentario=u'Código cálculo raterio para beneficiário', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.tipo_valor_informado			= TagInteiro(self._tipo_registro, 	u'16.3Y', u'tipo_valor_informado',	61, 61, descricao=u'C062', comentario=u'Tipo de valor informado', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		# ------------------------------------------------------------------------
		# 	depende do dado anterior
		# ------------------------------------------------------------------------
		self.valor_quantidade				= TagDecimal(self._tipo_registro, 	u'17.3Y', u'valor_quantidade',		 62,  76, descricao=u'C074', comentario=u'Valor ou quantidade', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.valor_percentual				= TagDecimal(self._tipo_registro, 	u'17.3Y', u'valor_percentual',		 62,  76, descricao=u'C074', comentario=u'Valor em percentual (%)', casas_decimais=3, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		# ------------------------------------------------------------------------
		self.codigo_banco					= TagInteiro(self._tipo_registro, 	u'18.3Y', u'codigo_banco',		 77,  79, descricao=u'G001', comentario=u'Código banco para credito beneficiario', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta_corrente_beneficiario	= ContaCorrenteBeneficiario(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nome_beneficiario				= TagCaracter(self._tipo_registro, 	u'24.3Y', u'nome_beneficiario',	100, 139, descricao=u'G013', comentario=u'Nome do beneficiário', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.parcela						= TagCaracter(self._tipo_registro, 	u'25.3Y', u'parcela',			140, 145, descricao=u'C063', comentario=u'Identificação parcela do rateio', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.floating						= TagInteiro(self._tipo_registro, 	u'26.3Y', u'floating',			146, 148, descricao=u'C064', comentario=u'Qtde dias para crédito beneficiário', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.data_credito					= TagData(self._tipo_registro, 		u'27.3Y', u'data_credito',		149, 156, descricao=u'C065', comentario=u'Data crédito beneficiário', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.motivo_ocorrido				= TagInteiro(self._tipo_registro, 	u'28.3Y', u'motivo_ocorrido',	157, 166, descricao=u'*C066', comentario=u'Identificação das rejeições', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_banco_destinatario_spb	= TagInteiro(self._tipo_registro, 	u'29.3Y', u'codigo_banco_destinatario_spb',	167, 174, descricao=u'*P015', comentario=u'Código do banco destinatário no SPB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB303Y						= TagCaracter(self._tipo_registro, 	u'30.3Y', u'CNAB303Y',			175, 240, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.codigo_registro_opcional.txt
		txt += self.conta_corrente_mantenedora.txt
		txt += self.nosso_numero.txt
		txt += self.calculo_rateio_beneficiario.txt
		txt += self.tipo_valor_informado.txt

		if self.tipo_valor_informado.valor == int(C062.PERCENTUAL):
			txt += self.valor_percentual.txt
		else:
			txt += self.valor_quantidade.txt

		txt += self.codigo_banco.txt
		txt += self.conta_corrente_beneficiario.txt
		txt += self.nome_beneficiario.txt
		txt += self.parcela.txt
		txt += self.floating.txt
		txt += self.data_credito.txt
		txt += self.motivo_ocorrido.txt
		txt += self.codigo_banco_destinatario_spb.txt
		txt += self.CNAB303Y.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.codigo_registro_opcional.txt = arquivo
			self.conta_corrente_mantenedora.txt = arquivo
			self.nosso_numero.txt = arquivo
			self.calculo_rateio_beneficiario.txt = arquivo
			self.tipo_valor_informado.txt = arquivo

			self.valor_percentual.txt = arquivo
			self.valor_quantidade.txt = arquivo

			self.codigo_banco.txt = arquivo
			self.conta_corrente_beneficiario.txt = arquivo
			self.nome_beneficiario.txt = arquivo
			self.parcela.txt = arquivo
			self.floating.txt = arquivo
			self.data_credito.txt = arquivo
			self.motivo_ocorrido.txt = arquivo
			self.codigo_banco_destinatario_spb.txt = arquivo
			self.CNAB303Y.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.codigo_registro_opcional.alertas)
		alertas.extend(self.conta_corrente_mantenedora.alertas)
		alertas.extend(self.nosso_numero.alertas)
		alertas.extend(self.calculo_rateio_beneficiario.alertas)
		alertas.extend(self.tipo_valor_informado.alertas)

		if self.tipo_valor_informado.valor == int(C062.PERCENTUAL):
			alertas.extend(self.valor_percentual.alertas)
		else:
			alertas.extend(self.valor_quantidade.alertas)

		alertas.extend(self.codigo_banco.alertas)
		alertas.extend(self.conta_corrente_beneficiario.alertas)
		alertas.extend(self.nome_beneficiario.alertas)
		alertas.extend(self.parcela.alertas)
		alertas.extend(self.floating.alertas)
		alertas.extend(self.data_credito.alertas)
		alertas.extend(self.motivo_ocorrido.alertas)
		alertas.extend(self.codigo_banco_destinatario_spb.alertas)
		alertas.extend(self.CNAB303Y.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += gera_text(NIVEIS.N3, self.codigo_registro_opcional.text)
		txt += self.conta_corrente_mantenedora.text
		txt += gera_text(NIVEIS.N3, self.nosso_numero.text)
		txt += gera_text(NIVEIS.N3, self.calculo_rateio_beneficiario.text)
		txt += gera_text(NIVEIS.N3, self.tipo_valor_informado.text)

		if self.tipo_valor_informado.valor == int(C062.PERCENTUAL):
			txt += gera_text(NIVEIS.N3, self.valor_percentual.text)
		else:
			txt += gera_text(NIVEIS.N3, self.valor_quantidade.text)

		txt += gera_text(NIVEIS.N3, self.codigo_banco.text)
		txt += self.conta_corrente_beneficiario.text
		txt += gera_text(NIVEIS.N3, self.nome_beneficiario.text)
		txt += gera_text(NIVEIS.N3, self.parcela.text)
		txt += gera_text(NIVEIS.N3, self.floating.text)
		txt += gera_text(NIVEIS.N3, self.data_credito.text)
		txt += gera_text(NIVEIS.N3, self.motivo_ocorrido.text)
		txt += gera_text(NIVEIS.N3, self.codigo_banco_destinatario_spb.text)
		txt += gera_text(NIVEIS.N3, self.CNAB303Y.text)

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