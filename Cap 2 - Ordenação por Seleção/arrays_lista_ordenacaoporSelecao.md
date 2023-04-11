# Resumo Arrays & Listas Concatenadas

## Arrays
- Sequência contígua de memória
- Desperdício de memória
- Mover os itens, caso seja necessário inserir novos itens

## Listas Concatenadas
- Armazenamento em diferentes locais de memória
- Cada item armazena o endereço do próximo item da lista
- Caso você queira saber o último elemento, precisa percorrer todos os elementos

| Arrays | Listas |
|----------|:--------:|
| Leitura, O(1) | Leitura, O(n) |
| Inserção, O(n) | Inserção, O(1) |
| Eliminação, O(n) | Eliminação, O(1) |