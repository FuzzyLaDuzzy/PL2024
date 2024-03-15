# TPC5 - Máquina de Venda Automática

Este código implementa um simulador de máquina de venda automática simples em Python. 

A máquina possui funcionalidades básicas para listar os itens disponíveis, adicionar saldo, selecionar um item para compra e sair da máquina.

# Comandos Disponíveis

LISTAR: Lista os itens disponíveis na máquina junto com seus preços e quantidades.

MOEDA: Adiciona saldo à máquina. A moeda deve ser seguida por um número representando a quantidade de dinheiro a ser adicionada e a unidade (centímetros ou euros).

SELECIONAR: Seleciona um item para compra. Deve ser seguido pelo ID do item desejado.

SAIR: Encerra a execução do programa, exibindo o troco atual.

# Exemplo de Uso

```
Enter a command: LISTAR
ID: 1, Nome: água, Preço: 2 euros and 20 centimos, Quantidade: 10
ID: 2, Nome: bolo, Preço: 1 euros and 60 centimos, Quantidade: 5
ID: 3, Nome: iced tea, Preço: 3 euros and 20 centimos, Quantidade: 7
Saldo: 0 euros
Enter a command: MOEDA 5e
Adicionado 5 euros ao saldo. Saldo atual: 5 euros
Enter a command: SELECIONAR 2
Saldo: 3.4 euros
Enter a command: SAIR
Troco :
1 x 2e
1 x 1e
2 x 20c
```
