# coding=utf-8
"""
Classe No

Esta classe representa o nó utilizado na estrutura de dados Tabela Hash.
"""


class No:

    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.next = None
