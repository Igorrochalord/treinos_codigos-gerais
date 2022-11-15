"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato
"""

print("aqui e o pague menos ")
valor1=float(input("valor do produto: "))
valor2=float(input("valor do produto: "))
valor3=float(input("valor do produto: "))
if valor1 < valor2 and valor3:
    print(f"compre o produto no valor de {valor1}")
if valor3 < valor2 and valor1:
    print(f"compre o produto no valor de {valor3}")
if valor2 < valor1 and valor3:
    print(f"compre o produto no valor de {valor2}")