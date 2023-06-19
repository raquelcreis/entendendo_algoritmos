def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo<custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

# Ache o nodo mais barato que você não tenha processado ainda
nodo = ache_no_custo_mais_baixo(custos)
# Se você já tiver processado todos os nodos, esse loop já foi feito
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    # Procure em todos os vizinhos desse nodo
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
         # Se for mais barato chegar ao vizinho por meio desse nodo
        if custos[n] > novo_custo:
            # Atualize o custo para esse nodo
            custos[n] = novo_custo
            # Assim, esse nodo vai se tornar o novo pai do vizinho
            pais[n] = nodo
    processados.append(nodo)
    # Ache o próximo nodo para processar e refaça o loop
    nodo = ache_no_custo_mais_baixo(custos)