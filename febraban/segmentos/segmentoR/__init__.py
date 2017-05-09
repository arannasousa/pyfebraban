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
from ... import TIPO_REGISTRO, NIVEIS, gera_text

from .controle import Controle
from .servico import Servico
from .desc2 import Desconto2
from .desc3 import Desconto3
from .multa import Multa
from .dados_debito import DadosDebito

class SegmentoR(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'R'):
		super(SegmentoR, self).__init__()

		self._lote = lote
		self._num_seq = num_seq		# numero sequencial do registro no lote
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.controle					= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico					= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.desconto2					= Desconto2(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.desconto3					= Desconto3(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.multa						= Multa(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.informacao_ao_sacado		= TagCaracter(self._tipo_registro, 	u'17.3R', u'informacao_ao_sacado',	 90,  99, descricao=u'*C036', comentario=u'Informação ao sacado', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.informacao3				= TagCaracter(self._tipo_registro, 	u'18.3R', u'informacao3',			100, 139, descricao=u'*C037', comentario=u'Mensagem 3', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.informacao4				= TagCaracter(self._tipo_registro, 	u'19.3R', u'informacao4',			140, 179, descricao=u'*C037', comentario=u'Mensagem 4', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB203R					= TagCaracter(self._tipo_registro, 	u'20.3R', u'CNAB203R',				180, 199, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.codigo_ocorrencia_sacado	= TagInteiro(self._tipo_registro,	u'21.3R', u'codigo_ocorrencia_sacado',200, 207, descricao=u'*C038', comentario=u'Código ocorrência do sacado', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.dados_debito				= DadosDebito(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.identific_emissao_aviso_debito	= TagInteiro(self._tipo_registro, u'28.3R', u'identific_emissao_aviso_debito', 231, 231, descricao=u'*C039', comentario=u'Aviso para débito automatico', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB293R					= TagCaracter(self._tipo_registro, 	u'29.3R', u'CNAB293R',				232, 240, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.desconto2.txt
		txt += self.desconto3.txt
		txt += self.multa.txt
		txt += self.informacao_ao_sacado.txt
		txt += self.informacao3.txt
		txt += self.informacao4.txt
		txt += self.CNAB203R.txt
		txt += self.codigo_ocorrencia_sacado.txt
		txt += self.dados_debito.txt
		txt += self.identific_emissao_aviso_debito.txt
		txt += self.CNAB293R.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.desconto2.txt = arquivo
			self.desconto3.txt = arquivo
			self.multa.txt = arquivo
			self.informacao_ao_sacado.txt = arquivo
			self.informacao3.txt = arquivo
			self.informacao4.txt = arquivo
			self.CNAB203R.txt = arquivo
			self.codigo_ocorrencia_sacado.txt = arquivo
			self.dados_debito.txt = arquivo
			self.identific_emissao_aviso_debito.txt = arquivo
			self.CNAB293R.txt = arquivo
	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.desconto2.alertas)
		alertas.extend(self.desconto3.alertas)
		alertas.extend(self.multa.alertas)
		alertas.extend(self.informacao_ao_sacado.alertas)
		alertas.extend(self.informacao3.alertas)
		alertas.extend(self.informacao4.alertas)
		alertas.extend(self.CNAB203R.alertas)
		alertas.extend(self.codigo_ocorrencia_sacado.alertas)
		alertas.extend(self.dados_debito.alertas)
		alertas.extend(self.identific_emissao_aviso_debito.alertas)
		alertas.extend(self.CNAB293R.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += self.desconto2.text
		txt += self.desconto3.text
		txt += self.multa.text
		txt += gera_text(NIVEIS.N3, self.informacao_ao_sacado.text)
		txt += gera_text(NIVEIS.N3, self.informacao3.text)
		txt += gera_text(NIVEIS.N3, self.informacao4.text)
		txt += gera_text(NIVEIS.N3, self.CNAB203R.text)
		txt += gera_text(NIVEIS.N3, self.codigo_ocorrencia_sacado.text)
		txt += self.dados_debito.text
		txt += gera_text(NIVEIS.N3, self.identific_emissao_aviso_debito.text)
		txt += gera_text(NIVEIS.N3, self.CNAB293R.text)
		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro