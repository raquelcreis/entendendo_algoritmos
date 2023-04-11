def pesquisa_binaria(lista,item):
    """Localiza um item em uma lista ordenada

    Args:
        lista (_list_)
        item (_object_)

    Returns:
        _object_: posição do item encontrado
        _None_ : se o item não for localizado na lista
    """
    # alto e baixo = zona de pesquisa
    baixo = 0 
    alto = len(lista) - 1

    while baixo <= alto: # enquanto você não conseguiu chegar a um único elemento
        meio = int((baixo + alto)/2) # verifique o elemento central
        chute = lista[meio]
        if chute == item: # achou o item!!
            return meio
        if chute > item: # o chute foi alto
            alto = meio - 1 # vamos reduzir a zona de pesquisa pela metade
        else: # o chute foi baixo
            baixo = meio + 1 # vamos reduzir a zona de pesquisa pela metade
    return None # o item não existe na zona de pesquisa