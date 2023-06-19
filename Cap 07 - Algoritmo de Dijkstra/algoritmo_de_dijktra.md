# Resumo de Algoritmo de Dijkstra
- A pesquisa em largura é usada para calcular o caminho mínimo para um grafo não ponderado
- O algoritmo de Dijkstra é usado para calcular o caminho mínimo para um grafo ponderado (o número associado a uma aresta é chamado de peso)
- O algoritmo de Dijkstra funciona quando todos os pesos são positivos
- O algoritmo de Dijkstra só funciona em gráficos sem ciclos
- Se o seu grafo tiver pesos negativos, use o algoritmo de Bellman-Ford

# Lógica
- Enquanto houver grafos a serem processados
- Pegue o vértice que está mais próximo do início (FIFO)
- Atualize os custos para os seus vizinhos
- Se qualquer um dos custos for atualizado, atualize também o pai
- Marque o vértice como processado
- Volte