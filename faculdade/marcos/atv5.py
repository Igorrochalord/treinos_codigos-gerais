def somaImposto(taxa, Custo):
    return (1 + taxa/100)*Custo
x1 = float(input('Digite a taxa de imposto: '))
x2= float(input('Digite o custo: '))
print('Valor com imposto:', somaImposto(x1,x2))

