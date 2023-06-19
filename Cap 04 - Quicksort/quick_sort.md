# Resumo Quicksort
## Dividir para conquistar

- Os algoritmos DC são recursivos.
1. Descubra o caso-base, que deve ser o caso mais simples possível
2. Divida ou diminua o seu problema até que ele se torne o caso-base

- Algoritmo de Euclides
"Caso você encontre o maior quadrado que divide este segmento, ele será o maior quadrado que irá dividir toda a fazenda".
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

- O algoritmo DC não é um simples algoritmo que você aplica em um problema, mas sim uma maneira de pensar sobre o problema. 

## Quicksort

1. Escolhe o elemento do array que será o pivô.

2. Após essa escolha, é feito o particionamento.
    2.1. Um subarray contendo todos os números menores do que o pivô.
    2.2. O pivô.
    2.3. Um subarray contendo todos os números maiores do que o pivô.

Os subarrays não estão ordenados, só particionados.

- O desempenho do quicksort depende bastante da escolha do pivô. O melhor caso é o caso médio.