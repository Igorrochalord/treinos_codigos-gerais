'''
for/else
'''

variavel = ['luiz otavio' , 'joaozinho', 'maria']
comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True
if comeca_com_j:
    print("existe uma palavra que começa com j.")
else:
    print("nao existe palavra com j")