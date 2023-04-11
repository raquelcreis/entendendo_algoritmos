# Resumo Pesquisa Binária

- Algoritmo que usa 'arrays'
- Tempo de execução logarítmico O(log n)
- Fica ainda mais rápido conforme os elementos da lista aumentam

# Resumo Big O notation

- Notação especial que diz o quão rápido é um algoritmo (tempo de execução)
- A rapidez de um algoritmo não é medida em segundos, mas pelo crescimento do número de operações

## Exemplos

- O(log n): pesquisa binária
- O(n): tempo linear (pesquisa simples)
- O(n * log n): algoritmo rápido de ordenação (quicksort)
- O(n^2): algoritmo lento de ordenação (ordenação por seleção)
- O(n!): caixeiro viajante


# Caixeiro Viajante

O caixeiro viajante Opus precisa ir em cinco cidades. Mas ele quer passar por todas as cidades percorrendo uma distância mínima. Para isso, temos que analisar cada ordem possível de cidades para visitar, somar todas as distâncias.

| Cidades | Operações | 
|----------|:--------:|
| 6 | 720 |
| 7 | 5040 |
| 8 | 40320 |
| ... | ... |
| 15 |  1307674368000 |

O número de operações aumenta drasticamente.