# Resumo Arrays & Listas Concatenadas

## Arrays
- Sequência contígua de memória
- Desperdício de memória
- Mover os itens, caso seja necessário inserir novos itens

## Listas Concatenadas
- Armazenamento em diferentes locais de memória
- Cada item armazena o endereço do próximo item da lista
- Caso você queira saber o último elemento, precisa percorrer todos os elementos

|  | Arrays | Listas |
|----------|:--------:|--------:|
| Leitura | O(1) | O(n) |
| Inserção | O(n) | O(1) |
| Eliminação | O(n) | O(1) |

Dica:
- Array: aleatório
- Lista: sequencial

# Resumo Ordenação por Selecão (Crescente)

1. Crie uma nova lista vazia para armazenar a lista ordenada
2. Faça um loop na lista original e encontre o menor valor dentro do loop
3. Armazena o índice do menor valor
4. Adicione o menor valor encontrado na nova lista criada no passo 1 usando o método append()
5. Remova o menor valor encontrado da lista original usando o método pop() e o índice encontrado no passo 3
6.Repita os passos 2 a 4 até que a lista original esteja vazia
7. Retorne a nova lista criada no passo 1, que contém a lista original ordenada

- Tempo de execução: O(n * n) = O(n^2)