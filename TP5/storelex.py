import ply.lex as lex

tokens = (
    'LISTAR',
    'MOEDA',
    'SAIR',
    'SELECIONAR',
    'NUMBER',
    'CENTIMOS',
    'EUROS'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_SAIR = r'SAIR'
t_SELECIONAR = r'SELECIONAR'
t_CENTIMOS = r'c'
t_EUROS = r'e'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore spaces
t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = [
    {'id': 1, 'nome': 'água', 'preco_euros': 2, 'preco_centimos': 20, 'quantidade': 10},
    {'id': 2, 'nome': 'bolo', 'preco_euros': 1, 'preco_centimos': 60, 'quantidade': 5},
    {'id': 3, 'nome': 'iced tea', 'preco_euros': 3, 'preco_centimos': 20, 'quantidade': 7},
]

saldo = 0

while True:
    command = input("Enter a command: ")
    lexer.input(command)
    for token in lexer:
        if token.type == 'LISTAR':
            for item in data:
                print(f"ID: {item['id']}, Nome: {item['nome']}, Preço: {item['preco_euros']} euros and {item['preco_centimos']} centimos, Quantidade: {item['quantidade']}")
            print(f"Saldo: {saldo} euros")
        elif token.type == 'MOEDA':
            while True:
                amount = next(lexer, None)
                if amount is None or amount.type != 'NUMBER':
                    break
                currency = next(lexer, None)
                if currency is None or (currency.type != 'CENTIMOS' and currency.type != 'EUROS'):
                    break
                if currency.type == 'CENTIMOS':
                    amount.value /= 100
                saldo += amount.value
                print(f"Adicionado {amount.value} euros ao saldo. Saldo atual: {saldo} euros")
        elif token.type == 'SELECIONAR':
            id = next(lexer)
            if id.type == 'NUMBER':
                for item in data:
                    if item['id'] == id.value:
                        if item['quantidade'] <= 0:
                            print("Erro: Este item está fora de estoque.")
                            break
                        total_price = item['preco_euros'] + item['preco_centimos'] / 100
                        if saldo < total_price:
                            print("Erro: Saldo insuficiente para comprar este item.")
                            break
                        saldo -= total_price
                        saldo = round(saldo,2)
                        item['quantidade'] -= 1
                        print(f"Saldo: {saldo} euros")
        elif token.type == 'SAIR':
            print(f"Troco : {saldo} euros")
            exit(0)
