# ModGerenciador
Implementação de um módulo gerenciador de uma tabela de símbolos de um compilador em **Python 3**.

## Funcionamento

A implementação é baseada no uso da tabela hash. A função de codificação de nomes (strings) para uso na tabela hash é do tipo polinomial, com melhoramento baseado no método Horner. Este modelo contem métodos para a manipulação da tabela de símbolos com as seguintes finalidade:

* Inicialização de TS;
* Busca;
* Inserção;
* Deleção;
* Atualização (alteração);

Este projeto foi feito para a classe de Tradução de Linguagens de Programação, 2019-1, Unisul - Tubarão, SC.

Este módulo é implementado de forma que possa ser eventualmente utilizado no trabalho final do matéria como suporte à análise semântica e geração de código intermediário.

É importante notar que um dos requisistos desse projeto é que o programa tenha uma classe principal, que é utilizada para testar a tabela de símbolos. A classe necessariamente precisa constar acessos (hard-coded) à tabela de símbolos de forma a demonstrar seu funcionamento:
* Inserir 10 elementos;
* Mostrar conteúdo da tabela;
* Alterar dados de 5 elementos;
* Mostrar conteúdo da tabela;
* Excluir 3 elementos;
* Mostrar conteúdo da tabela;
* Fazer uma busca por 1 elemento inexistente na tabela. Mostrar mensagem que o elemento não foi encontrado;
* Fazer uma busca por 3 elementos que estão na tabela. Mostra os dados completos dos elementos encontrados.

Este projeto está sobre a licença GNU General Public License v3.0.

## Contribuidores
**Gabriel Cavalcante**
