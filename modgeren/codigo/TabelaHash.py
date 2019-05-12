# coding=utf-8
"""
Classe TabelaHash

Classe responsável pelas ações da estrutura de dados da tabela hash
"""

from modgeren.codigo.No import No

# Variável responsável pelo tamanho inicial do array interno
CAPACIDADE_INICIAL = 200


class TabelaHash():

    # A tabela é inicializada com três propriedades
    def __init__(self):
        self.capacidade = CAPACIDADE_INICIAL
        self.tamanho = 0
        self.balde = [None] * self.capacidade

    # Método que gera um hash para uma determinada chave
    # Entrada: chave - string
    # Saída: Index de zero até self.capacidade
    def hash(self, chave):

        hashsum = 0

        # Faz um loop pela chave, depois por cada caractere na chave
        for index, i in enumerate(chave):
            # Adiciona (index + tamanho da chave) ^ (código do charactere atual)
            hashsum += (index + len(chave)) ** ord(i)

            # Mantem o hashsum num tamanho razoável
            # No caso [0, self.capacidade -1]
            hashsum = hashsum % self.capacidade

        return hashsum

    # Metodo de busca de um elemento pela chave
    # Entrada: chave - string
    # Saida: valor do nó ou nada
    def busca_elem(self, chave):

        # Computa o index usando a função hash
        index = self.hash(chave)
        # Ponteiro no primeiro nó na lista do balde
        no = self.balde[index]

        # Um loop para achar a chave, ou chegar ao fim da lista
        while no is not None and no.chave != chave:
            no = no.next
        # Se o nó estiver vazio
        if no is None:
            # Retorna nada
            print('Elemento {} inexistente na tabela.\n'.format(chave))
            return None
        else:
            print('Elemento {} tem as informações:\n{} na tabela.\n'
                  .format(chave, no.valor))
            # Retorna o valor do no
            return no.valor

    # Método de inserção de um elemento
    # Entrada: chave - string
    #          valor - qualquer coisa
    # Saída: vazia
    def insere_elem(self, chave, valor):

        # Incrementa o tamanho
        self.tamanho += 1
        # Computa o index da chave
        index = self.hash(chave)
        # Vai para o nó correspondente ao hash
        no = self.balde[index]
        # Se o nó estiver vazio
        if no is None:
            # Cria um nó, adiciona, retorna nada
            self.balde[index] = No(chave, valor)
            print("Elemento inserido: ")
            self.busca_elem(chave)
            return

        prev = no

        while no is not None:
            prev = no
            no = no.next

        # Adiciona novo nó ao final da lista com chave providenciada
        prev.next = No(chave, valor)

    # Método de deleção de um nó pela chave
    # Entrada: chave - string
    # Saída: valor removido ou nada
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
            print("Chave não encontrada.\n")
            return None
        else:
            # Chave é encontrada
            self.tamanho -= 1
            resultado = no.valor
            # Deleta esse elemento na lista
            if prev is None:
                self.balde[index] = no.next
            else:
                # Remove o nó da lista, removendo suas associações
                prev.next = prev.next.next
            # Returna o resultado após remoção
            return resultado

    # Método de atualização/alteração de um elemento
    # Entrada: chave - string
    #           valor - qualquer coisa
    # Saída: novas informações do nó ou nada
    def altera_elem(self, chave, valor):

        # Computa hash
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
                print("Chave não encontrada.\n")
            else:
                # Chave é encontrada
                no.valor = valor
                print("Valor alterado: ")
                self.busca_elem(chave)
