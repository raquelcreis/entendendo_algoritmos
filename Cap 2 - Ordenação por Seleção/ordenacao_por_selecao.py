def buscaMenor(arr):
    menor = arr[0] #armazena o menor valor
    menor_indice = 0 #armazena o índice do menor valor
    for i in range(1,len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice
    
def ordenacaoporSelecao(arr): #ordenaçõe em um array
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) #encontra o menor elemento do array e adiciona ao novo array
        novoArr.append(arr.pop(menor))
    return novoArr
