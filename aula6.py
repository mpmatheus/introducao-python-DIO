conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) #une os 2 conjuntos e retira a duplicidade
print('uniao: {}' .format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection (conjunto2) #ele pega apenas os numeros repetidos ente os 2 conjuntos
print('interseccao: {}' .format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2) #pega a diferenca entre o conjunto e o conjunto 2 e mostra so os numeros do conjunto que nao estao no conjunto 2
print('diferenca entre 1 e 2: {}' .format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('diferenca entre 2 e 1: {}'.format(conjunto_diferenca2))
conunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferenca simetrica: {}'.format (conunto_diff_simetrica))
conjunto_a = {1, 2, 3,}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b) #conjunto a é um subconjunto conjunto b
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset (conjunto_a) #b é um superconjunto de a, b tem todos os elementos que tem em a
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)   # converte uma lista em um conjunto
print (conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)




# conjunto = {1, 2, 3, 4, 4, 2} #criar um conjunto 
# conjunto.add(5) #adiciona um numero ao conjunto
# conjunto.discard(2) #remove um numero do conjunto
# print(conjunto)