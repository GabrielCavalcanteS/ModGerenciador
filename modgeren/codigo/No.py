# coding=utf-8
"""
Classe No

Esta classe representa o nó utilizado na estrutura de dados de um Nó.
"""


class No():

    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.next = None

    def __str__(self):
        return "<No: (%s, %s), next: %s>" % \
               (self.chave, self.valor, self.next is not None)

    def __repr__(self):
        return str(self)


