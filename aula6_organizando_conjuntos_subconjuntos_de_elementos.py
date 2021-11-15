# Organizando conjuntos e subconjuntos de elementos em Python

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2) # une os conjuntos
print('Uniao: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2) # relaciona valor repetido
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferente1 = conjunto.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferente1))
conjunto_diferente2 = conjunto2.difference(conjunto)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferente2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simetrica entre 1 e 2: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b) # se é um subconjunto
print('A é um subconjunto de B: {}'.format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('B é um subconjunto de A: {}'.format(conjunto_subset))
conjunto_superset = conjunto_a.issuperset(conjunto_b) # se é um superconjunto
print('A é um superconjunto de B: {}'.format(conjunto_superset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista = list(conjunto_animais)
print(lista)


# print(type(conjunto))
# print(conjunto)
# conjunto.add(5) # adiciona
# print(conjunto)
# conjunto.discard(2) # descarta
# print(conjunto)