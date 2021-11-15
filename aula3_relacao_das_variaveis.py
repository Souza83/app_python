# Como criar um código em Python que funcione de acordo com a relação das variáveis

a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Voce digitou errado! Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Voce digitou errado! Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Voce digitou errado! Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Voce digitou errado! Quarto bimestre: '))
media = (a + b + c + d) / 4
print(media)

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par')
# else:
#     print('Não foi digitado um número par.')

#############################################################################################
# a = int(input('Entre com um valor: '))
# resto = a % 2
# if resto == 0:
#     print('Esse numero é par.')
# else:
#     print('Esse numero é impar')

##############################################################################################
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# c = int(input('Entre com o terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior valor é: {}' .format(a))
# elif b > a and b > c:
#     print('O maior valor é: {}' .format(b))
# else:
#     print('O maior valor é: {}'.format(c))
# print('Fim do programa')
