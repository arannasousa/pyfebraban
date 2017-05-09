# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
__author__ = u'asantos'

from .....febraban import NIVEIS, gera_text

from .....febraban.segmentos.segmentoQ import dados_sacado
from .inscricao import Inscricao

class DadosSacado(dados_sacado.DadosSacado):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'Q'):
		super(DadosSacado, self).__init__(lote=lote, num_seq=num_seq, segmento=segmento)

		self.inscricao	= Inscricao(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

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