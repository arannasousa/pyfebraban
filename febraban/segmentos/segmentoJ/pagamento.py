# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ...base import (TagInteiro, TagDecimal, TagCaracter, TagData, TXT)
from ... import TIPO_REGISTRO, NIVEIS, gera_text

class Pagamento(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'J'):
		super(Pagamento, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.codigo_barras		= TagInteiro(self._tipo_registro, 	u'08.3J', u'codigo_barras', 	 18,  61, descricao=u'*G063', comentario=u'Código de barras',					segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.nome_cedente		= TagCaracter(self._tipo_registro, 	u'09.3J', u'nome_cedente', 		 62,  91, descricao=u'G013', comentario=u'Nome do cedente', 					segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.data_vencimento	= TagData(self._tipo_registro, 		u'10.3J', u'data_vencimento',	 92,  99, descricao=u'G044', comentario=u'Data do vencimento (nominal)', 		segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor_titulo		= TagDecimal(self._tipo_registro, 	u'11.3J', u'valor_titulo', 		100, 114, descricao=u'G042', comentario=u'Valor do título', 					segmento=self._segmento, lote=self._lote, num_seq=num_seq, casas_decimais=2)
		self.desconto			= TagDecimal(self._tipo_registro, 	u'12.3J', u'desconto',  		115, 129, descricao=u'L002', comentario=u'Valor do desconto + abatimento', 		segmento=self._segmento, lote=self._lote, num_seq=num_seq, casas_decimais=2)
		self.acrescimos			= TagDecimal(self._tipo_registro,	u'13.3J', u'acrescimos',  		130, 144, descricao=u'L003', comentario=u'Valor da mora + abatimento', 			segmento=self._segmento, lote=self._lote, num_seq=num_seq, casas_decimais=2)
		self.data_pagamento		= TagData(self._tipo_registro, 		u'14.3J', u'data_pagamento',	145, 152, descricao=u'P009', comentario=u'Data do pagamento', 					segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.valor_pagamento	= TagDecimal(self._tipo_registro,	u'15.3J', u'valor_pagamento', 	153, 167, descricao=u'P010', comentario=u'Valor do pagamento', 					segmento=self._segmento, lote=self._lote, num_seq=num_seq, casas_decimais=2)
		self.quantidade_moeda	= TagDecimal(self._tipo_registro,	u'16.3J', u'quantidade_moeda',	168, 182, descricao=u'G041', comentario=u'Quantidade da moeda', 				segmento=self._segmento, lote=self._lote, num_seq=num_seq, casas_decimais=5)
		self.referencia_sacado	= TagCaracter(self._tipo_registro,	u'17.3J', u'referencia_sacado',	183, 202, descricao=u'G064', comentario=u'Nº do docto atribuído pela empresa', 	segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):

		txt = u''
		txt += self.codigo_barras.txt
		txt += self.nome_cedente.txt
		txt += self.data_vencimento.txt
		txt += self.valor_titulo.txt
		txt += self.desconto.txt
		txt += self.acrescimos.txt
		txt += self.data_pagamento.txt
		txt += self.valor_pagamento.txt
		txt += self.quantidade_moeda.txt
		txt += self.referencia_sacado.txt

		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.codigo_barras.txt = arquivo
			self.nome_cedente.txt = arquivo
			self.data_vencimento.txt = arquivo
			self.valor_titulo.txt = arquivo
			self.desconto.txt = arquivo
			self.acrescimos.txt = arquivo
			self.data_pagamento.txt = arquivo
			self.valor_pagamento.txt = arquivo
			self.quantidade_moeda.txt = arquivo
			self.referencia_sacado.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.codigo_barras.alertas)
		alertas.extend(self.nome_cedente.alertas)
		alertas.extend(self.data_vencimento.alertas)
		alertas.extend(self.valor_titulo.alertas)
		alertas.extend(self.desconto.alertas)
		alertas.extend(self.acrescimos.alertas)
		alertas.extend(self.data_pagamento.alertas)
		alertas.extend(self.valor_pagamento.alertas)
		alertas.extend(self.quantidade_moeda.alertas)
		alertas.extend(self.referencia_sacado.alertas)

		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += gera_text(NIVEIS.N4, self.codigo_barras.text)
		txt += gera_text(NIVEIS.N4, self.nome_cedente.text)
		txt += gera_text(NIVEIS.N4, self.data_vencimento.text)
		txt += gera_text(NIVEIS.N4, self.valor_titulo.text)
		txt += gera_text(NIVEIS.N4, self.desconto.text)
		txt += gera_text(NIVEIS.N4, self.acrescimos.text)
		txt += gera_text(NIVEIS.N4, self.data_pagamento.text)
		txt += gera_text(NIVEIS.N4, self.valor_pagamento.text)
		txt += gera_text(NIVEIS.N4, self.quantidade_moeda.text)
		txt += gera_text(NIVEIS.N4, self.referencia_sacado.text)
		return txt

	text = property(get_text)