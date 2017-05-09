# coding=utf-8
"""
Desenvolvedor:	asantos
E-mail:			Arannã Sousa Santos
Mês:			04
Ano:			2015
Empresa:		TINS - SOLUCOES CORPORATIVAS
"""
from ..febraban.constantes import *
from ..febraban.tipo_servico import *


CODIGO_BANCO = u'001'


class C004(C004):
	descricao = u'Código de movimento remessa'

	ENTRADA_TITULOS = U'01'
	PEDIDO_BAIXA = U'02'
	ABATIMENTO_CONCESSAO = u'04'
	ABATIMENTO_CANCELAMENTO = U'05'
	ALTERACAO_VENCIMENTO = U'06'
	DESCONTO_CONCESSAO = U'07'
	DESCONTO_CANCELAMENTO = U'08'
	PROTESTAR = U'09'
	CANCELA_SUSTENTACAO_INSTRUCAO_PROTESTO = U'10'
	RECUSA_DA_ALEGACAO_SACADO = U'30'
	ALTERACAO_OUTROS_DADOS = U'31'
	ALTERACAO_MODALIDADE = U'40'


# -----------------------------------------
# sobre escreve
# -----------------------------------------
class C006(object):
	descricao = u'Código da carteira'

	CARTEIRA_SIMPLES_11_12 = U'1'
	COBRANCA_VINCULADA_11_17 = U'2'
	COBRANCA_CAUCIONADA_11_17 = U'3'
	COBRANCA_CARTEIRA_31 = U'3'
	COBRANCA_DESCONTADA_11_17 = U'4'
	COBRANCA_CARTEIRA_51 = U'4'
	COBRANCA_SIMPLES_17 = U'5'


class C047(C047):
	"""
	Complicadissimo, depende do 44 e possui 5 duplas, ou seja, até 5 erros juntos no mesmo campo
	"""

	descricao = u'Identificação para Rejeições, Tarifas, Custas, Liquidação e Baixas'


class C016(object):
	descricao = u'Identificação de título aceito/não aceito'

	ACEITE = u'A'
	NAO_ACEITE = u'N'


class C021(object):
	descricao = u'Código do desconto 1/2/3'

	VALOR_FIXO_ATE_A_DATA_INFORMADA = u'1'
	PERCENTUAL_ATE_A_DATA_INFORMADA = u'2'

	VALOR_POR_ANTECIPACAO_DIA_CORRIDO = u'3'
	VALOR_POR_ANTECIPACAO_DIA_UTIL = u'4'

	PERCENTUAL_SOBRE_VALOR_NOMINAL_DIA_CORRIDO = u'5'
	PERCENTUAL_SOBRE_VALOR_NOMINAL_DIA_UTIL = u'6'

	CANCELAMENTO_DESCONTO = u'7'
