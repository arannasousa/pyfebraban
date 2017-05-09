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
from .conta_corrente_mantenedora import ContaCorrenteMantenedora
from .sacado import Sacado

class SegmentoT(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'T'):
		super(SegmentoT, self).__init__()

		self._lote = lote
		self._num_seq = num_seq		# numero sequencial do registro no lote
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.conta_corrente_mantenedora		= ContaCorrenteMantenedora(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nosso_numero					= TagCaracter(self._tipo_registro, 	u'13.3T', u'nosso_numero',			 38,  57, descricao=u'*G069', comentario=u'Identificação do título no banco', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.carteira						= TagInteiro(self._tipo_registro, 	u'14.3T', u'carteira',		 		 58,  58, descricao=u'*C006', comentario=u'Código da carteira', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.numero_documento				= TagCaracter(self._tipo_registro, 	u'15.3T', u'numero_documento',		 59,  73, descricao=u'*C011', comentario=u'Número do documento de cobrança', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.vencimento						= TagData(self._tipo_registro, 		u'16.3T', u'vencimento',			 74,  81, descricao=u'*C012', comentario=u'Data do vencimento do título', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.valor_titulo					= TagDecimal(self._tipo_registro, 	u'17.3T', u'valor_titulo',			 82,  96, descricao=u'*G070', comentario=u'Valor do título', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.banco_cobrador_recebedor		= TagInteiro(self._tipo_registro, 	u'18.3T', u'banco_cobrador_recebedor', 97,  99, descricao=u'*C045', comentario=u'Número do banco', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.agencia_cobrador_recebedor		= TagInteiro(self._tipo_registro, 	u'19.3T', u'agencia_cobrador_recebedor', 100, 104, descricao=u'*G008', comentario=u'Agência cobradora/recebedora', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dv_cobrador_recebedor			= TagInteiro(self._tipo_registro, 	u'20.3T', u'dv_cobrador_recebedor', 	105, 105, descricao=u'*G009', comentario=u'Dígito verificador cobrador/recebedor', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.uso_da_empresa					= TagCaracter(self._tipo_registro, 	u'21.3T', u'uso_da_empresa',		106, 130, descricao=u'G072', comentario=u'Identificação do título na empresa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_moeda					= TagInteiro(self._tipo_registro, 	u'22.3T', u'codigo_moeda',			131, 132, descricao=u'*G065', comentario=u'Código da moeda', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq, valor=CODIGO_MOEDA.REAL)
		self.sacado							= Sacado(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.numero_contrato				= TagInteiro(self._tipo_registro, 	u'26.3T', u'numero_contrato',		189, 198, descricao=u'C030', comentario=u'Número do contrato da operação de crédito', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq, valor=CODIGO_MOEDA.REAL)
		self.valor_tarifo_custas			= TagDecimal(self._tipo_registro, 	u'27.3T', u'valor_tarifa_custas',	199, 213, descricao=u'G076', comentario=u'Valor da tarifa/custas', casas_decimais=2, lote=self._lote, segmento=self._segmento, num_seq=self._num_seq, valor=CODIGO_MOEDA.REAL)
		self.motivo_ocorrencia				= TagCaracter(self._tipo_registro, 	u'28.3T', u'motivo_ocorrencia',		214, 223, descricao=u'*C047', comentario=u'Motivo da ocorrência', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB293T						= TagCaracter(self._tipo_registro, 	u'29.3T', u'CNAB293T',				224, 240, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.conta_corrente_mantenedora.txt
		txt += self.nosso_numero.txt
		txt += self.carteira.txt
		txt += self.numero_documento.txt
		txt += self.vencimento.txt
		txt += self.valor_titulo.txt
		txt += self.banco_cobrador_recebedor.txt
		txt += self.agencia_cobrador_recebedor.txt
		txt += self.dv_cobrador_recebedor.txt
		txt += self.uso_da_empresa.txt
		txt += self.codigo_moeda.txt
		txt += self.sacado.txt
		txt += self.numero_contrato.txt
		txt += self.valor_tarifo_custas.txt
		txt += self.motivo_ocorrencia.txt
		txt += self.CNAB293T.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.conta_corrente_mantenedora.txt = arquivo
			self.nosso_numero.txt = arquivo
			self.carteira.txt = arquivo
			self.numero_documento.txt = arquivo
			self.vencimento.txt = arquivo
			self.valor_titulo.txt = arquivo
			self.banco_cobrador_recebedor.txt = arquivo
			self.agencia_cobrador_recebedor.txt = arquivo
			self.dv_cobrador_recebedor.txt = arquivo
			self.uso_da_empresa.txt = arquivo
			self.codigo_moeda.txt = arquivo
			self.sacado.txt = arquivo
			self.numero_contrato.txt = arquivo
			self.valor_tarifo_custas.txt = arquivo
			self.motivo_ocorrencia.txt = arquivo
			self.CNAB293T.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.conta_corrente_mantenedora.alertas)
		alertas.extend(self.nosso_numero.alertas)
		alertas.extend(self.carteira.alertas)
		alertas.extend(self.numero_documento.alertas)
		alertas.extend(self.vencimento.alertas)
		alertas.extend(self.valor_titulo.alertas)
		alertas.extend(self.banco_cobrador_recebedor.alertas)
		alertas.extend(self.agencia_cobrador_recebedor.alertas)
		alertas.extend(self.dv_cobrador_recebedor.alertas)
		alertas.extend(self.uso_da_empresa.alertas)
		alertas.extend(self.codigo_moeda.alertas)
		alertas.extend(self.sacado.alertas)
		alertas.extend(self.numero_contrato.alertas)
		alertas.extend(self.valor_tarifo_custas.alertas)
		alertas.extend(self.motivo_ocorrencia.alertas)
		alertas.extend(self.CNAB293T.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += self.conta_corrente_mantenedora.text
		txt += gera_text(NIVEIS.N3, self.nosso_numero.text)
		txt += gera_text(NIVEIS.N3, self.carteira.text)
		txt += gera_text(NIVEIS.N3, self.numero_documento.text)
		txt += gera_text(NIVEIS.N3, self.vencimento.text)
		txt += gera_text(NIVEIS.N3, self.valor_titulo.text)
		txt += gera_text(NIVEIS.N3, self.banco_cobrador_recebedor.text)
		txt += gera_text(NIVEIS.N3, self.agencia_cobrador_recebedor.text)
		txt += gera_text(NIVEIS.N3, self.dv_cobrador_recebedor.text)
		txt += gera_text(NIVEIS.N3, self.uso_da_empresa.text)
		txt += gera_text(NIVEIS.N3, self.codigo_moeda.text)
		txt += self.sacado.text
		txt += gera_text(NIVEIS.N3, self.numero_contrato.text)
		txt += gera_text(NIVEIS.N3, self.valor_tarifo_custas.text)
		txt += gera_text(NIVEIS.N3, self.motivo_ocorrencia.text)
		txt += gera_text(NIVEIS.N3, self.CNAB293T.text)

		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro