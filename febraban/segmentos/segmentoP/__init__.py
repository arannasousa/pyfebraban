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
from ... import TIPO_REGISTRO, NIVEIS, gera_text, CODIGO_MOEDA

from .controle import Controle
from .servico import Servico
from .conta_corrente import ContaCorrente
from .caracteristica_cobranca import CaracteristicaCobranca
from .juros import Juros
from .desc1 import Desc1

class SegmentoP(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'P'):
		super(SegmentoP, self).__init__()

		self._lote = lote
		self._num_seq = num_seq		# numero sequencial do registro no lote
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta_corrente			= ContaCorrente(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nosso_numero			= TagCaracter(self._tipo_registro, 	u'13.3P', u'nosso_numero',  		 38,  57, descricao=u'*G069', comentario=u'Identificação do título no banco', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.caracteristica_cobranca = CaracteristicaCobranca(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.numero_documento		= TagCaracter(self._tipo_registro, 	u'19.3P', u'numero_documento',		 63,  77, descricao=u'*C011', comentario=u'Número do documento de cobrança', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.vencimento				= TagData(self._tipo_registro, 		u'20.3P', u'vencimento',			 78,  85, descricao=u'*C012', comentario=u'Data de vencimento do título', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.valor_titulo			= TagDecimal(self._tipo_registro, 	u'21.3P', u'valor_titulo',			 86, 100, descricao=u'*G070', comentario=u'Valor nominal do título', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.agencia_cobradora		= TagInteiro(self._tipo_registro, 	u'22.3P', u'agencia_cobradora',		101, 105, descricao=u'*C014', comentario=u'Agência encarregada da cobrança', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dv						= TagCaracter(self._tipo_registro, 	u'23.3P', u'dv',					106, 106, descricao=u'*G009', comentario=u'Dígito verificador da agência', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.especie_titulo			= TagInteiro(self._tipo_registro, 	u'24.3P', u'especie_titulo',		107, 108, descricao=u'*C015', comentario=u'Espécie de título', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.aceite					= TagCaracter(self._tipo_registro, 	u'25.3P', u'aceite',				109, 109, descricao=u'*C016', comentario=u'Identificação de título aceito/não aceito', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.data_emissao_titulo	= TagData(self._tipo_registro, 		u'26.3P', u'data_emissao_titulo',	110, 117, descricao=u'G071', comentario=u'Data de emissão do título', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.juros 					= Juros(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.desc1					= Desc1(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.valor_iof 				= TagDecimal(self._tipo_registro, 	u'33.3P', u'valor_iof',				166, 180, descricao=u'C024', comentario=u'Valor do IOF a ser recolhido', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.valor_abatimento		= TagDecimal(self._tipo_registro, 	u'34.3P', u'valor_abatimento',		181, 195, descricao=u'G045', comentario=u'Valor do abatimento', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.uso_empresa_cedente	= TagCaracter(self._tipo_registro, 	u'35.3P', u'uso_empresa_cedente',	196, 220, descricao=u'G072', comentario=u'Identificação do título na empresa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_protesto		= TagInteiro(self._tipo_registro, 	u'36.3P', u'codigo_protesto',		221, 221, descricao=u'G026', comentario=u'Código para protesto', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.prazo_protesto			= TagInteiro(self._tipo_registro, 	u'37.3P', u'prazo_protesto',		222, 223, descricao=u'G027', comentario=u'Número de dias para protesto', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_baixa_devolucao	= TagInteiro(self._tipo_registro, 	u'38.3P', u'codigo_baixa_devolucao',224, 224, descricao=u'G028', comentario=u'Código para baixa/devolucao', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.prazo_baixa_devolucao	= TagCaracter(self._tipo_registro, 	u'39.3P', u'prazo_baixa_devolucao',	225, 227, descricao=u'G029', comentario=u'Número de dias para baixa/devolucao', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_moeda			= TagInteiro(self._tipo_registro, 	u'40.3P', u'codigo_moeda',			228, 229, descricao=u'*G065', comentario=u'Código da moeda', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.numero_contrato		= TagInteiro(self._tipo_registro, 	u'41.3P', u'numero_contrato',		230, 239, descricao=u'C030', comentario=u'Número do contrato', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.uso_livre				= TagCaracter(self._tipo_registro, 	u'42.3P', u'uso_livre',				240, 240, descricao=u'C078', comentario=u'Uso livre banco/empresa ou autorização de pagamento parcial', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

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
		txt += self.uso_empresa_cedente.txt
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
			self.uso_empresa_cedente.txt = arquivo
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
		alertas.extend(self.uso_empresa_cedente.alertas)
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
		txt += gera_text(NIVEIS.N3, self.uso_empresa_cedente.text)
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