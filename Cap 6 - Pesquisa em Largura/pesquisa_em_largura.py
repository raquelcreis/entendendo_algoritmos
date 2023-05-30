#Exemplo: o dono de uma fazenda de mangas está procurando um vendedor de mangas que possa vender sua colheita.
# Será que ele tem algum vendedor de mangas no Facebook?
# Ele pode procurar entre os seus amigos e entre os amigos dos seus amigos.


def pesquisa(nome):
    fila_de_pesquisa = deque() #cria fila com 2 finais
    fila_de_pesquisa += grafo[nome] #adiciona todos os amigos para a lista de pesquisa
    verificadas = [] #armazenamento das pessoas já verificadas
    
    while fila_de_pesquisa: #enquanto a fila de pesquisa não está vazia
        pessoa = fila_de_pesquisa.popleft() #pego a primeira pessoa da fila
        if not pessoa in verificadas: #verifico se essa pessoa já foi verificada
            if pessoa_e_vendedor(pessoa):
                print(pessoa,"vende mangas")
                return True #encerra aqui. pesquisa realizada.
            else:
                fila_de_pesquisa +=grafo[pessoa] #adiciona todos os amigos para a lista de pesquisa
                verificadas.append(pessoa) #marca a pessoa como verificadas (evita loop eterno)