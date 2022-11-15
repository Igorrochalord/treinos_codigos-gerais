'''
split , join,enumerate 
*split - dividir uma string
*join -juntar uma lista
*enumerate - enumerar elementos em uma lista

'''

a = 'o brasil e o pais do futbol , o brasil e penta. '
lista = a.split(' ')
for indice , valor in enumerate(lista):
    print(indice,valor , lista [indice])