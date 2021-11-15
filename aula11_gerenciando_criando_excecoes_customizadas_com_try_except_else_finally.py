# Gerenciando e criando exceções customizadas com try, except, else e finally

lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar a divisão por 0.')

except ArithmeticError:
    print('Não foi possível realizar uma operação aritimética.')

except IndexError:
    print('Erro ao acessar um indice inválido da lista.')

except Exception as ex:
    print('Erro desconhecido. Erro {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa.')
    arquivo.close()
    print('Arquivo fechado.')