# README

## Ferramenta de Soma

Este script recebe uma sequência de entrada através da entrada padrão (stdin). Ele processa a entrada, interpretando palavras-chave 'on', 'off', e '=', bem como números inteiros. A função process_input() lê a entrada, mantém um total acumulado e atualiza esse total dependendo das instruções 'on', 'off', e dos números fornecidos. Quando a instrução '=' é encontrada, o script imprime o total acumulado até o momento.


Exemplo de uso :

```
echo "on 5 off 10 on 15 = 20" | python script.py

```
Aqui o terminal iria imprimir "Sum is: 20", que é o resultado da soma no momento que encontra o "=".
