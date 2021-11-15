contador_letras = lambda lista: [len(x) for x in lista]

lista_palavras = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_palavras))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b
print(soma(10, 5))
print(subtracao(10, 5))
print(multiplicacao(10, 5))
print(divisao(10, 5))

caluladora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(caluladora))
soma = caluladora['soma']
subtracao = caluladora['subtracao']
multiplicacao = caluladora['multiplicacao']
divisao = caluladora['divisao']
print('A soma entre A e B: {}'.format(soma(10, 5)))
print('A subtração entre A e B: {}'.format(subtracao(10, 5)))
print('A multiplicação entre A e B: {}'.format(multiplicacao(10, 5)))
print('A divisão entre A e B: {}'.format(divisao(10, 5)))