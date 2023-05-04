# Resumo Tabelas Hash

Provavelmente você nunca terá que implementar uma tabela hash na vida, porque as linguagens de programação já fornecem implementação dessa funcionalidade.
É possível usar tabela hash do Python e acreditar que ela operará no caso médio de desempenho: tempo de execução constante.

PS: tempo de execução constante não significa instantaneamente, mas sim um tempo que continuará sempre o mesmo, independentemente de quão grande a tabela hash possa ficar.

## Função hash

É uma função na qual você insere uma string e ela retorna um número.

## Colisões

Duas chaves são indicadas para o mesmo espaço (isso é um problema). Se diversas chaves mapeiam para o mesmo espaço, inicie uma lista encadeada neste espaço. 

## Observações

- Você pode fazer uma tabela hash ao combinar uma função hash com um array
- Colisões são problemas. É necessário haver uma função hash que minimize colisões. 
- As tabelas hash são extremamente rápidas para pesquisar, inserir e remover itens.
- Tabelas hash são boas para modelar relações entre dois itens.
- As tabelas hash são utilizadas como cache de dados
- As tabelas hash são ótimas para localizar duplicatas