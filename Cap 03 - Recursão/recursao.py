# Problema: Existe uma chave que abre uma mala misteriosa. A sua avó diz que a chave está em uma caixa. Esta caixa contém mais caixas com mais caixas dentro delas.

# Solução 1: Usando loops

def procura_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_para_busca()
    while pilha is not vazia:
        caixa = pilha.pega_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("Achei a chave!")

# Solução 2: Usando recursão

def procura_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procura_pela_chave(item) #RECURSÃO!
        elif item.e_uma_chave():
            print("Achei a chave!")
            
# "Os loops podem melhorar o desempenho do seu programa. A recursão melhora o desempenho do seu programador.
# Escolha o que for mais importante para a sua situação" Leigh Caldwell.

# Caso Base e Caso Recursivo

def regressiva(i):
    print(i)
    if i <= 1: # caso base
        return
    else:
        regressiva(i-1)
        
# Pilha de Chamada

def sauda(nome):
    print("Olá " + nome + "!")
    sauda2(nome) #pilha de chamada, função pausada em um estado parcialmente pausado
    print("Preparando para dizer tchau...")
    tchau() #pilha de chamada, função pausada em um estado parcialmente pausado
    
def sauda2(nome):
    print("Como vai "+ nome + "?")
    
def tchau():
    print("ok,tchau")