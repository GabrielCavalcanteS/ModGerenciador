"""
Método Principal

"""
from modgeren.codigo import TabelaHash
from modgeren.codigo import No


class Main:
    # TODO Testar métodos com inserções, deleções, alterações, buscas e valores diferentes
    # Variável para a nova tabela hash
    tabela_hash = TabelaHash.TabelaHash()
    no = No

    aux1 = ["256575"]
    aux2 = ["1543565"]
    aux3 = ["756545"]
    aux4 = ["921355"]
    aux5 = ["865751235"]
    aux6 = ["512355"]
    aux7 = ["459085"]
    aux8 = ["355654195"]
    aux9 = ["143547355"]
    aux10 = ["555"]

    # Adiciona 10
    tabela_hash.insere_elem('aux2', aux1)
    tabela_hash.insere_elem('aux3', aux2)
    tabela_hash.insere_elem('aux4', aux3)
    tabela_hash.insere_elem('aux5', aux4)
    tabela_hash.insere_elem('aux6', aux5)
    tabela_hash.insere_elem('aux7', aux6)
    tabela_hash.insere_elem('aux8', aux7)
    tabela_hash.insere_elem('aux9', aux8)
    tabela_hash.insere_elem('aux10', aux9)
    tabela_hash.insere_elem('aux1', aux10)
    # Mostra tabela
    print('Tabela após adicionar 10: \n', tabela_hash)

    tabela_hash.altera_elem('aux10', aux3)
    tabela_hash.altera_elem('aux1', aux6)
    tabela_hash.altera_elem('aux2', aux8)
    tabela_hash.altera_elem('aux5', aux1)
    tabela_hash.altera_elem('aux7', aux9)
    print(tabela_hash)
    tabela_hash.busca_elem('aux12')
