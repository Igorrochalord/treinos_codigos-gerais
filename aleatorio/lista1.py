#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
while True:
    x1 = input("digite um numero: ")
    print()
    x2 = input ("digite um numero: ")
    print()
    x3 = input ("digite um numero: ")
    print()
    x4 = input ("digite um numero: ")
    print()
    x5 = input ("digite um numero: ")
    print()
    if x1 and x2 and x3 and x4 and x5:
        x1 = int(x1)
        x2 = int(x2)
        x3 = int(x3)
        x4 = int(x4)
        x5 = int(x5)
        lista = [x1 , x2 , x3 ,x4 , x5]
        print(lista)