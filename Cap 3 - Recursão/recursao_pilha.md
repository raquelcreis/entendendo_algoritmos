# Resumo Recursão

- A função chama ela mesma
- Mais fácil de cair no caso de loop infinito.
- *Caso-recursivo:* é quando a função chama a si mesma.
- *Caso-base:* é quando a função não chama a si mesma novamente de forma que o programa não se torna um loop infinito.

## Pilha

- Quando você INSERE um item, ele é colocado no TOPO da pilha.
- Quando você LÊ um item, lê apenas o item do TOPO da pilha e ele é RETIRADO da lista.
- *Push*: adicione um novo item ao topo
- *Pop*: remova o item do topo e leia-o

## Pilha de chamada (call stack)

```
def sauda(nome):
    print(...)
    sauda2(nome) #push & pop
    print(...)
    tchau() #push & pop

def sauda2(nome): # quando for chamada, ficará na pilha de chamada
    print(...)

def tchau(): # quando for chamada, ficará na pilha de chamada
    print(...)
 ```

- Quando você chama uma função a partir de outra, a chamada de função fica pausada em um estado parcialmente completo.
- A pilha de chamada é usada para guardar as variáveis de múltiplas funções.
- Desvantagem: custo. A pilha pode ficar muito grande e ocupar muita memória.
    - Reescrever seu código utilizando loops
    - Utilizar tail recursion
