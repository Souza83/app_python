# Lidando com módulos, importação de classes, métodos e construção de funções anônimas (lambda)

from aula7_Televisao import Televisao
from aula7_Calculadora1 import Calculadora
from aula8_ContadorLetras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras da lista é: {}'.format(total_letras))
    print(teste())