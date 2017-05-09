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
from ... import TIPO_REGISTRO, NIVEIS, gera_text, C040

from .controle import Controle
from .servico import Servico

class SegmentoS(TXT):
	def __init__(self, lote=u'0001', num_seq=u'00001', segmento=u'S'):
		super(SegmentoS, self).__init__()

		self._lote = lote
		self._num_seq = num_seq		# numero sequencial do registro no lote
		self._segmento = segmento

		# -------------------------------------------------------------------------------------
		# 	com essa informacao, eu consigo localizar os dados desse REGISTRO
		# -------------------------------------------------------------------------------------
		self._tipo_registro = TIPO_REGISTRO.SEGMENTO

		self.controle				= Controle(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.servico				= Servico(lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		# 	tag CHAVE, com essa informacao, as tags seguintes podem variar
		self.tipo_de_impressao		= TagInteiro(self._tipo_registro, 	u'08.3S', u'tipo_de_impressao',		 18,  18, descricao=u'*C040', comentario=u'Identificação da impressão', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		# -------------------------------------------------------
		# 	tipo de impressao 1 ou 2
		# -------------------------------------------------------
		self.numero_da_linha		= TagInteiro(self._tipo_registro,	u'09.3S', u'numero_da_linha',	 19,  20, descricao=u'*C041', comentario=u'Número da linha a ser impresso', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.mensagem				= TagCaracter(self._tipo_registro, 	u'10.3S', u'mensagem',			 21, 160, descricao=u'*C042', comentario=u'Mensagem a ser impressa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.tipo_fonte				= TagInteiro(self._tipo_registro,	u'11.3S', u'tipo_fonte',		161, 162, descricao=u'*C043', comentario=u'Tipo do caracter a ser impresso', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB123S				= TagCaracter(self._tipo_registro, 	u'12.3S', u'CNAB123S',			163, 240, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)

		# -------------------------------------------------------
		# 	tipo de impressao 3
		# -------------------------------------------------------
		self.informacao5			= TagCaracter(self._tipo_registro, 	u'09.3S', u'informacao5',		 19,  58, descricao=u'*C037', comentario=u'Mensagem a ser impressa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.informacao6			= TagCaracter(self._tipo_registro, 	u'10.3S', u'informacao6',		 59,  98, descricao=u'*C037', comentario=u'Mensagem a ser impressa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.informacao7			= TagCaracter(self._tipo_registro, 	u'11.3S', u'informacao7',		 99, 138, descricao=u'*C037', comentario=u'Mensagem a ser impressa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.informacao8			= TagCaracter(self._tipo_registro, 	u'12.3S', u'informacao8',		139, 178, descricao=u'*C037', comentario=u'Mensagem a ser impressa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.informacao9			= TagCaracter(self._tipo_registro, 	u'13.3S', u'informacao9',		179, 218, descricao=u'*C037', comentario=u'Mensagem a ser impressa', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)
		self.CNAB143S				= TagCaracter(self._tipo_registro, 	u'14.3S', u'CNAB143S',			219, 240, descricao=u'G004', comentario=u'Uso exclusivo FEBRABAN/CNAB', lote=self._lote, segmento=self._segmento, num_seq=self._num_seq)


	def get_txt(self):
		txt = u''
		txt += self.controle.txt
		txt += self.servico.txt
		txt += self.tipo_de_impressao.txt
		# --------------------------------------------------------
		# 	se for tipo 3
		# --------------------------------------------------------
		if unicode(self.tipo_de_impressao.valor) == C040.CORPO_INSTRUCAO_FICHA_COMPENSASAO_BLOQUETO:
			txt += self.informacao5.txt
			txt += self.informacao6.txt
			txt += self.informacao7.txt
			txt += self.informacao8.txt
			txt += self.informacao9.txt
			txt += self.CNAB143S.txt
		# --------------------------------------------------------
		# 	se for tipo 1 ou 2
		# --------------------------------------------------------
		else:
			txt += self.numero_da_linha.txt
			txt += self.mensagem.txt
			txt += self.tipo_fonte.txt
			txt += self.CNAB123S.txt
		return txt

	def set_txt(self, arquivo):
		if self._le_txt(arquivo):
			self.controle.txt = arquivo
			self.servico.txt = arquivo
			self.tipo_de_impressao.txt = arquivo
			# --------------------------------------------------------
			# 	se for tipo 3
			# --------------------------------------------------------
			if unicode(self.tipo_de_impressao.valor) == C040.CORPO_INSTRUCAO_FICHA_COMPENSASAO_BLOQUETO:
				self.informacao5.txt = arquivo
				self.informacao6.txt = arquivo
				self.informacao7.txt = arquivo
				self.informacao8.txt = arquivo
				self.informacao9.txt = arquivo
				self.CNAB143S.txt = arquivo
			# --------------------------------------------------------
			# 	se for tipo 1 ou 2
			# --------------------------------------------------------
			else:
				self.numero_da_linha.txt = arquivo
				self.mensagem.txt = arquivo
				self.tipo_fonte.txt = arquivo
				self.CNAB123S.txt = arquivo

	txt = property(get_txt, set_txt)

	def get_alertas(self):
		alertas = []
		alertas.extend(self.controle.alertas)
		alertas.extend(self.servico.alertas)
		alertas.extend(self.tipo_de_impressao.alertas)
		# --------------------------------------------------------
		# 	se for tipo 3
		# --------------------------------------------------------
		if unicode(self.tipo_de_impressao.valor) == C040.CORPO_INSTRUCAO_FICHA_COMPENSASAO_BLOQUETO:
			alertas.extend(self.informacao5.alertas)
			alertas.extend(self.informacao6.alertas)
			alertas.extend(self.informacao7.alertas)
			alertas.extend(self.informacao8.alertas)
			alertas.extend(self.informacao9.alertas)
			alertas.extend(self.CNAB143S.alertas)
		# --------------------------------------------------------
		# 	se for tipo 1 ou 2
		# --------------------------------------------------------
		else:
			alertas.extend(self.numero_da_linha.alertas)
			alertas.extend(self.mensagem.alertas)
			alertas.extend(self.tipo_fonte.alertas)
			alertas.extend(self.CNAB123S.alertas)
		return alertas

	alertas = property(get_alertas)

	def get_text(self):
		txt = gera_text(NIVEIS.N2, unicode(__name__) + u'\n')
		txt += self.controle.text
		txt += self.servico.text
		txt += gera_text(NIVEIS.N3, self.tipo_de_impressao.text)
		# --------------------------------------------------------
		# 	se for tipo 3
		# --------------------------------------------------------
		if unicode(self.tipo_de_impressao.valor) == C040.CORPO_INSTRUCAO_FICHA_COMPENSASAO_BLOQUETO:
			txt += gera_text(NIVEIS.N3, self.informacao5.text)
			txt += gera_text(NIVEIS.N3, self.informacao6.text)
			txt += gera_text(NIVEIS.N3, self.informacao7.text)
			txt += gera_text(NIVEIS.N3, self.informacao8.text)
			txt += gera_text(NIVEIS.N3, self.informacao9.text)
			txt += gera_text(NIVEIS.N3, self.CNAB143S.text)
		# --------------------------------------------------------
		# 	se for tipo 1 ou 2
		# --------------------------------------------------------
		else:
			txt += gera_text(NIVEIS.N3, self.numero_da_linha.text)
			txt += gera_text(NIVEIS.N3, self.mensagem.text)
			txt += gera_text(NIVEIS.N3, self.tipo_fonte.text)
			txt += gera_text(NIVEIS.N3, self.CNAB123S.text)

		return txt

	text = property(get_text)

	@property
	def segmentoCorreto(self):
		"""
		Checa se o dado passado é deste segmento mesmo

		"""
		return self.servico.segmento.valor == self._segmento and \
			   unicode(self.controle.registro.valor) == self._tipo_registro