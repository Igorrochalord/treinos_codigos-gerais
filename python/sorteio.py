'''
from random import randrange, uniform
print(randrange(0, 9)) #faixa de inteiro
print(uniform(0, 9)) #faixa de ponto flutuante
Você pode importar tudo e usar o que deseja:

from random import *
random.seed() #inicia a semente dos número pseudo randômicos
random.randrange(0, 9, 2) # pares entre 0 e 9
random.choice('abcdefghij') # seleciona um dos elementos aleatoriamente
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items) # embaralha os itens aleatoriamente
'''





import random
while True:
    print("oia o sorteio")
    print()
    num=int(input('digite um numero:'))
    items=[1,2,3,4,5,6,7,8,9,10]
    x=random.randrange(1,10)
    if num == x:
        print(f"parabens{x}")
        
    else:
            print("tenta denovo")
