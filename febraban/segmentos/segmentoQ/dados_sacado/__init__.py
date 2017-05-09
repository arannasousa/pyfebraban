# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from ....base import (TagCaracter, TagInteiro, TXT)
from .... import TIPO_REGISTRO, NIVEIS, gera_text

from .inscricao import Inscricao

class DadosSacado(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Q'):
		super(DadosSacado, self).__init__()

		self._lote = lote
		self._num_seq = num_seq
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		# tipo_registro, codigo, nome, de, ate, valor=None, descricao=None, alertas=[], comentario=None, segmento=None, operacao=None

		self.inscricao	= Inscricao(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.nome		= TagCaracter(self._tipo_registro,	u'10.3Q', u'nome',		 34,  73, descricao=u'G013', comentario=u'Nome',	 		segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.endereco	= TagCaracter(self._tipo_registro,	u'11.3Q', u'endereco',	 74, 113, descricao=u'G032', comentario=u'Endereço',		segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.bairro		= TagCaracter(self._tipo_registro,	u'12.3Q', u'bairro',	114, 128, descricao=u'G032', comentario=u'Bairro',			segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.cep		= TagInteiro(self._tipo_registro,	u'13.3Q', u'cep',		129, 133, descricao=u'G034', comentario=u'CEP',				segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.sufixo_cep	= TagInteiro(self._tipo_registro,	u'14.3Q', u'sufixo_cep',134, 136, descricao=u'G035', comentario=u'Sufixo do CEP',	segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.cidade		= TagCaracter(self._tipo_registro,	u'15.3Q', u'cidade',	137, 151, descricao=u'G033', comentario=u'Cidade',			segmento=self._segmento, lote=self._lote, num_seq=num_seq)
		self.uf			= TagCaracter(self._tipo_registro,	u'16.3Q', u'uf',		152, 153, descricao=u'G036', comentario=u'UF',				segmento=self._segmento, lote=self._lote, num_seq=num_seq)

	def get_txt(self):
		txt = u''
		txt += self.inscricao.txt
		txt += self.nome.txt
		txt += self.endereco.txt
		txt += self.bairro.txt
		txt += self.cep.txt
		txt += self.sufixo_cep.txt
		txt += self.cidade.txt
		txt += self.uf.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.inscricao.txt = arquivo
			self.nome.txt = arquivo
			self.endereco.txt = arquivo
			self.bairro.txt = arquivo
			self.cep.txt = arquivo
			self.sufixo_cep.txt = arquivo
			self.cidade.txt = arquivo
			self.uf.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = self._alertas or []
		alertas.extend(self.inscricao.alertas)
		alertas.extend(self.nome.alertas)
		alertas.extend(self.endereco.alertas)
		alertas.extend(self.bairro.alertas)
		alertas.extend(self.cep.alertas)
		alertas.extend(self.sufixo_cep.alertas)
		alertas.extend(self.cidade.alertas)
		alertas.extend(self.uf.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N3, unicode(__name__) + u'\n')
		txt += self.inscricao.text
		txt += gera_text(NIVEIS.N4, self.nome.text)
		txt += gera_text(NIVEIS.N4, self.endereco.text)
		txt += gera_text(NIVEIS.N4, self.bairro.text)
		txt += gera_text(NIVEIS.N4, self.cep.text)
		txt += gera_text(NIVEIS.N4, self.sufixo_cep.text)
		txt += gera_text(NIVEIS.N4, self.cidade.text)
		txt += gera_text(NIVEIS.N4, self.uf.text)
		return txt

	text = property(get_text)