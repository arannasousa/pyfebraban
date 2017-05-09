# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....febraban.base import (TagCaracter, TagInteiro, TagData, TagDecimal, TXT)
from ....febraban import TIPO_REGISTRO, NIVEIS, gera_text, CODIGO_MOEDA
from ....febraban import segmentos

from .controle import Controle
from .servico import Servico
from .conta_corrente import ContaCorrente
from .caracteristica_cobranca import CaracteristicaCobranca
from .juros import Juros
from .desc1 import Desc1

class SegmentoP(segmentos.SegmentoP):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'P'):
		super(SegmentoP, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta_corrente			= ContaCorrente(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.caracteristica_cobranca = CaracteristicaCobranca(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.juros 					= Juros(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.desc1					= Desc1(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		self.identificacao_titulo_na_empresa = TagCaracter(self._tipo_registro, u'35.3P', u'identificacao_titulo_na_empresa', 196, 220, descricao=u'G072', comentario=u'Identificação do título na empresa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.conta_corrente.txt
		txt += self.nosso_numero.txt
		txt += self.caracteristica_cobranca.txt
		txt += self.numero_documento.txt
		txt += self.vencimento.txt
		txt += self.valor_titulo.txt
		txt += self.agencia_cobradora.txt
		txt += self.dv.txt
		txt += self.especie_titulo.txt
		txt += self.aceite.txt
		txt += self.data_emissao_titulo.txt
		txt += self.juros.txt
		txt += self.desc1.txt
		txt += self.valor_iof.txt
		txt += self.valor_abatimento.txt
		txt += self.identificacao_titulo_na_empresa.txt
		txt += self.codigo_protesto.txt
		txt += self.prazo_protesto.txt
		txt += self.codigo_baixa_devolucao.txt
		txt += self.prazo_baixa_devolucao.txt
		txt += self.codigo_moeda.txt
		txt += self.numero_contrato.txt
		txt += self.uso_livre.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.conta_corrente.txt = arquivo
			self.nosso_numero.txt = arquivo
			self.caracteristica_cobranca.txt = arquivo
			self.numero_documento.txt = arquivo
			self.vencimento.txt = arquivo
			self.valor_titulo.txt = arquivo
			self.agencia_cobradora.txt = arquivo
			self.dv.txt = arquivo
			self.especie_titulo.txt = arquivo
			self.aceite.txt = arquivo
			self.data_emissao_titulo.txt = arquivo
			self.juros.txt = arquivo
			self.desc1.txt = arquivo
			self.valor_iof.txt = arquivo
			self.valor_abatimento.txt = arquivo
			self.identificacao_titulo_na_empresa.txt = arquivo
			self.codigo_protesto.txt = arquivo
			self.prazo_protesto.txt = arquivo
			self.codigo_baixa_devolucao.txt = arquivo
			self.prazo_baixa_devolucao.txt = arquivo
			self.codigo_moeda.txt = arquivo
			self.numero_contrato.txt = arquivo
			self.uso_livre.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.conta_corrente.alertas)
		alertas.extend(self.nosso_numero.alertas)
		alertas.extend(self.caracteristica_cobranca.alertas)
		alertas.extend(self.numero_documento.alertas)
		alertas.extend(self.vencimento.alertas)
		alertas.extend(self.valor_titulo.alertas)
		alertas.extend(self.agencia_cobradora.alertas)
		alertas.extend(self.dv.alertas)
		alertas.extend(self.especie_titulo.alertas)
		alertas.extend(self.aceite.alertas)
		alertas.extend(self.data_emissao_titulo.alertas)
		alertas.extend(self.juros.alertas)
		alertas.extend(self.desc1.alertas)
		alertas.extend(self.valor_iof.alertas)
		alertas.extend(self.valor_abatimento.alertas)
		alertas.extend(self.identificacao_titulo_na_empresa.alertas)
		alertas.extend(self.codigo_protesto.alertas)
		alertas.extend(self.prazo_protesto.alertas)
		alertas.extend(self.codigo_baixa_devolucao.alertas)
		alertas.extend(self.prazo_baixa_devolucao.alertas)
		alertas.extend(self.codigo_moeda.alertas)
		alertas.extend(self.numero_contrato.alertas)
		alertas.extend(self.uso_livre.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += self.conta_corrente.text
		txt += gera_text(NIVEIS.N3, self.nosso_numero.text)
		txt += self.caracteristica_cobranca.text
		txt += gera_text(NIVEIS.N3, self.numero_documento.text)
		txt += gera_text(NIVEIS.N3, self.vencimento.text)
		txt += gera_text(NIVEIS.N3, self.valor_titulo.text)
		txt += gera_text(NIVEIS.N3, self.agencia_cobradora.text)
		txt += gera_text(NIVEIS.N3, self.dv.text)
		txt += gera_text(NIVEIS.N3, self.especie_titulo.text)
		txt += gera_text(NIVEIS.N3, self.aceite.text)
		txt += gera_text(NIVEIS.N3, self.data_emissao_titulo.text)
		txt += self.juros.text
		txt += self.desc1.text
		txt += gera_text(NIVEIS.N3, self.valor_iof.text)
		txt += gera_text(NIVEIS.N3, self.valor_abatimento.text)
		txt += gera_text(NIVEIS.N3, self.identificacao_titulo_na_empresa.text)
		txt += gera_text(NIVEIS.N3, self.codigo_protesto.text)
		txt += gera_text(NIVEIS.N3, self.prazo_protesto.text)
		txt += gera_text(NIVEIS.N3, self.codigo_baixa_devolucao.text)
		txt += gera_text(NIVEIS.N3, self.prazo_baixa_devolucao.text)
		txt += gera_text(NIVEIS.N3, self.codigo_moeda.text)
		txt += gera_text(NIVEIS.N3, self.numero_contrato.text)
		txt += gera_text(NIVEIS.N3, self.uso_livre.text)
		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro