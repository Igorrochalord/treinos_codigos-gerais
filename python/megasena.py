from random import randint
import time 

def upload(x):
    print("=============================")
    for i in range(x):
        for x in range(1):
            print("=       =")
            time.sleep(0.2)
            for x in range(1):
                print("==       ==")
                time.sleep(0.2)
                for x in range(1):
                    print("===      ===")
                    time.sleep(0.2)
                    for x in range(1):
                        print("====    ====")
                        time.sleep(0.2)
                        for x in range(1):
                             print("=====   =====")
                             time.sleep(0.2)
                             for x in range(1):
                                print("====== ======")
                                time.sleep(0.2)
                                for x in range(1):
                                    print("=============")
                                    time.sleep(0.2)                                      
numero_escolhido=[]
numeros_sortidos=[]
certos = []
x = 0
print('==================MEGA-SENA=====================================')
print("voce tera que digita cincos numeros")
contador = 0
while True:
    numero = input(f"numero {contador} : ")
    if numero.isnumeric():
        numero=int(numero)
        numero_escolhido.append(numero)
        contador += 1        

    else:
        print("digite um numero")
        
    if contador == 5:
        print("vamos começar")
        break
upload(4)
print("vamos sortear os numeros ")
for i in range(0, 5):
    sorteio=randint(1,50)
    numeros_sortidos.append(sorteio)
for i in range(0,5):
    if numero_escolhido[i]==numeros_sortidos[i]:
        certos.append('certos')
print(f"voce acertou {x} numeros ")
