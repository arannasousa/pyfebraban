# -*- coding: utf-8 -*-
u"""
Integrantes:    Arannã Sousa Santos, asousas@live.com
Ano:            2015
Mês:            04
"""
__author__ = u'Aranna'

if __name__ == u'__main__':
	# este código faz a leitura de um arquivo de REMESSA do banco para nós
	# ele faz a checagem de cada dado e separa numa estrutura em árvore para facilitar a leitura dos dados (desenvolvimento)

	from banco_do_brasil import ArquivoBB

	a = ArquivoBB()

	# gera o conteudo necessario rçrç

	# a._le_txt(open(u'./rem_pqrsty.txt', u'r'))

	a._le_txt(open(u'./rem_1-BB.txt', u'r'))

	a.txt = a._txt

	print u'alertas: ', len(a.alertas)

	for alerta in a.alertas:
		print alerta

	if not a.alertas:
		print u'verbose:'
		print a.text

	print u'txt:'
	print a.txt
