# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagInteiro, TagCaracter, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class CaracteristicaCobranca(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'P'):
		super(CaracteristicaCobranca, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.carteira				= TagInteiro(self._tipo_registro, 	u'14.3P', u'carteira',				58, 58, descricao=u'*C007', comentario=u'Código da carteira', 					segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.cadastramento			= TagInteiro(self._tipo_registro, 	u'15.3P', u'cadastramento',			59, 59, descricao=u'C008', comentario=u'Forma de cadastro do título no banco', 	segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.documento				= TagCaracter(self._tipo_registro, 	u'16.3P', u'documento',				60, 60, descricao=u'*C009', comentario=u'Tipo de documento', 					segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.emissao_bloqueto		= TagInteiro(self._tipo_registro, 	u'17.3P', u'emissao_bloqueto',		61, 61, descricao=u'C010', comentario=u'Identificação da emissão do bloqueto', 	segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.distribuicao_bloqueto	= TagCaracter(self._tipo_registro, 	u'18.3P', u'distribuicao_bloqueto',	62, 62, descricao=u'*C011', comentario=u'Identificação da distribuição', 		segmento=self._segmento, lote=self._lote, num_seq=num_seq)


	def get_txt(self):
		txt = u''
		txt += self.carteira.txt
		txt += self.cadastramento.txt
		txt += self.documento.txt
		txt += self.emissao_bloqueto.txt
		txt += self.distribuicao_bloqueto.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.carteira.txt = arquivo
			self.cadastramento.txt = arquivo
			self.documento.txt = arquivo
			self.emissao_bloqueto.txt = arquivo
			self.distribuicao_bloqueto.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.carteira.alertas)
		alertas.extend(self.cadastramento.alertas)
		alertas.extend(self.documento.alertas)
		alertas.extend(self.emissao_bloqueto.alertas)
		alertas.extend(self.distribuicao_bloqueto.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.carteira.text)
		txt += gera_text(NIVEIS.N4, self.cadastramento.text)
		txt += gera_text(NIVEIS.N4, self.documento.text)
		txt += gera_text(NIVEIS.N4, self.emissao_bloqueto.text)
		txt += gera_text(NIVEIS.N4, self.distribuicao_bloqueto.text)
		return txt

	text = property(get_text)