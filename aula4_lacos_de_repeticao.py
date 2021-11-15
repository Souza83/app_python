# Como criar laços de repetição em Python

a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Voce digitou errado! Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Voce digitou errado! Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Voce digitou errado! Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Voce digitou errado! Quarto bimestre: '))
media = (a + b + c + d) / 4
print(media)

###############################################################################################

# nota = int(input('Digite nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida!!! Entre com uma nota válida: '))
# print(nota)

################################################################################################

# a = 0
# while a <= 10:
#     print(a)
#     a+=1

#################################################################################################

# a = int(input('Digite um valor: '))
# for num in range (a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#          print(num)

#################################################################################################

# a = int(input('Digite um valor: '))
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('O numero {} é primo.'.format(a))
# else:
#     print('O numero {} não é primo.'.format(a))

#################################################################################################

# for x in range (1, 101):
#     print(x)