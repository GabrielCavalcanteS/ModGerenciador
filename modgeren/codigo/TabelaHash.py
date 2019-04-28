# coding=utf-8
"""
Classe TabelaHash

Classe responsável pelas ações da estrutura de dados tabela hash
"""

from modgeren.codigo.No import No

# Variável responsável pelo tamanho inicial do array interno
CAPACIDADE_INICIAL = 200

class TabelaHash:
    # A tabela é inicializada com três propriedades
    def __init__(self):
        self.capacidade = CAPACIDADE_INICIAL
        self.tamanho = 0
        self.balde = [None] * self.capacidade

    # Método para a tabela hash
    def hash(self, chave):

        hashsum = 0

        # Faz um loop pela chave, depois por cada caractere na chave
        for index, i in enumerate(chave):

            hashsum +=(index + len(chave)) ** ord(i)

            # Mantem o hashsum num tamanho razoável
            hashsum = hashsum % self.capacidade
        return hashsum

    # Metodo de busca de um elemento
    def busca_elem(self, chave):
        # Computa o index usando a função hash
        index = self.hash(chave)
        no = self.balde[index]

        # Um loop para achar a chave, ou chegar ao fim da lista
        while no is not None and no.chave != chave:
            no = no.next
        if no is None:
            return None
        else:
            return no.valor

    # Método de inserção de um elemento
    def insere_elem(self, chave, valor):
        self.tamanho += 1
        index = self.hash(chave)
        no = self.balde[index]
        # Se o nó estiver vazio
        if no is None:
            self.balde[index] = No(chave, valor)
            return

        prev = no

        while no is not None:
            no = no.next

        prev.next = No(chave, valor)

    # Método de deleção de um elemento
    def remove_elem(self, chave):
        # Computa o hash
        index = self.hash(chave)
        no = self.balde[index]
        prev = None
        # Itera até o nó requisitado
        while no is not None and no.chave != chave:
            prev = no
            no = no.next
        # O nó é encontrado ou não
        if no is None:
            # Chave não encontrada
            return None
        else:
            # A chave é encontrada
            self.tamanho -= 1
            resultado = no.valor
            # Deleta esse elemento na lista
            if prev is None:
                self.balde[index] = no.next  # May be None, or the next match
            else:
                prev.next = prev.next.next  # LinkedList delete by skipping over
            # Return the deleted result
            return resultado

    # TODO Método de atualização/alteração de um elemento
    def altera_elem(self):
