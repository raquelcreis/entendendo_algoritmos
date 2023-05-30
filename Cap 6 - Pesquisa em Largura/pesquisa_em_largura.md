# Resumo Pesquisa em Largura

- A pesquisa em largura lhe diz se há um caminho de A para B
- Se esse caminho existir, a pesquisa em largura lhe dará o caminho mínimo.
- Se você tem um problema do tipo "encontre o menor X", tente modelar o seu problema utilizando grafos e use a pesquisa em largura para resolvê-lo.


# Grafos
- Modelo de grafos é um modelo de conexões. Cada grafo é constituído de vértices (também chamados de nós) e arestas que conectam esses vértices.
- Um dígrafo contém setas e as relações seguem a direção das setas (Rama -> Adit significa que Rama deve dinheiro a Adit).
- Grafos não direcionados não contêm setas, e a relação acontece nos dois sentidos (Ross - Rachel significa "Ross namorou Rachel e Rachel namorou Ross").
- A fila e a pilha são estruturas de dados lineares que seguem regras específicas para a inserção e remoção de elementos. Elas são particularmente úteis para controlar o fluxo de visitas aos vértices de um grafo durante a execução de algoritmos de busca, como busca em largura e busca em profundidade.
- Filas são FIFO (First In First Out - primeiro a entrar, primeiro a sair)
- Pilhas são LIFO (Last In First Out - último a entrar, primeiro a sair)
- Você precisa verificar as pessoas na ordem em que elas foram adicionadas à lista de pesquisa. Portanto a lista de pesquisa deve ser uma fila; caso contrário, você não obterá o caminho mínimo.
- Cada vez que você precisar verificar alguém, procure não verificá-lo novamente. Caso contrário, poderá acabar em um loop infinito.