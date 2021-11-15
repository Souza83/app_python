# Como organizar os dados em uma lista ou tupla e realizar operações com elas

lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
nova_lista = lista_animal * 3

tupla = (1, 3, 7)
print(tupla)
print(len(tupla))
print(len(lista))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
lista_numerica[0] = 100
print(type(lista_numerica))
print(lista_numerica)

##################################################################################

#lista_animal[2] = 'hipopotamo'
#print(lista_animal)

###################################################################################

# lista.sort() # ordena em ordem crescente
# lista_animal.sort() # ordena em ordem crescente
# print(lista)
# print(lista_animal)
# lista.reverse() # ordena em ordem decrescente
# lista_animal.reverse() # ordena em ordem decrescente
# print(lista)
# print(lista_animal)

###################################################################################

#print(nova_lista)
# if 'Lobo' in lista_animal:
#     print('Existe lobo na lista')
# else:
#     print('Não existe lobo na lista, então será adicionado.')
#     lista_animal.append('lobo')
#     print(lista_animal)
# #lista_animal.pop(2) # pop com parametro remove o item da posição e sem remove o ultimo
# lista_animal.remove('gato')
# print(lista_animal)
#
# #print(max(lista)) # máximo
# #print(min(lista)) # mínimo
# #print(sum(lista)) # soma
# # for x in lista_animal:
# #     print(x)
# #print(lista[1])
# #print(lista_animal[2])
