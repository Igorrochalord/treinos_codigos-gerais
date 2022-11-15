'''
artigo stf
len
import time
x = time.localtime()
time.sleep  (1)
'''

from random import randint
#import datatime
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
upload(2)
while True:  #COMEÇOS DE ARQUIVOS JUS
    lista=[]
    print("ola sou o projustiça , progama com temas juridicos")
    for i in range(0,5):
        time.sleep(0.6)
        print(f"artigo da constituiçao: {i}")
    escolha=input("qual deseja saber ?: ")
    if escolha == '1':
        print("Art. 1º A República Federativa do Brasil , \nformada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, \n constitui-se em Estado Democrático de Direito")
        artigos = input("deseja saber os artigos ?: ")
        if artigos == 'sim':
            list = ["I - a soberania;"  "II - a cidadania;"  "III - a dignidade da pessoa humana;" " IV - os valores sociais do trabalho e da livre iniciativa;  "]
            print(list)
            deci=input("deseja cuntinuar ?:[sim] [nao]")
            if deci == 'sim':
                print('ok')
            if deci == 'nao':
                    break
    if escolha == "2":
        print("Art. 2º São Poderes da União, independentes e harmônicos entre si, o Legislativo, o Executivo e o Judiciário.")
        escolha2=input("deseja cuntinuar: [S] [N] ")
        if escolha2 == 'S':
            print('entendido')
        if escolha2 == "N":
            break
    if escolha == "3":
        print("Art. 3º Constituem objetivos fundamentais da República Federativa do Brasil:")
        artigos1=input("deseja saber os artigos?: ")
        if artigos1 == "sim":
            print(  "I - construir uma sociedade livre, justa e solidária;" 
                "II - garantir o desenvolvimento nacional;" 
                "III - erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais;"
                "IV - promover o bem de todos, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação")
            escolha2=input("deseja cuntinuar: [S] [N] ")
            if escolha2 == 'S':
                    print('entendido')
            if escolha2 == "N":
                    break
    if escolha == '4':
        print("Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais")
        artigos2=input("deseja saber os artigos?: ")
        if artigos2 == 'sim':
            time.sleep(1)
            print("I - independência nacional; ") #arrumar de acordo com a area juridica 
            time.sleep(1)
            print("II - prevalência dos direitos humanos; ")
            time.sleep(1)
            print("III- autodeterminação dos povos; ")
            time.sleep(1)
            print("IV - não-intervenção; ")
            time.sleep(1)
            print("V - igualdade entre os Estados; ")
            time.sleep(1)
            print("vI - defesa da paz; ")
            time.sleep(1)
            print("VII - solução pacífica dos conflitos; ")
            time.sleep(1)
            print("VIII - repúdio ao terrorismo e ao racismo; ")
            time.sleep(1)
            print("IX - cooperação entre os povos para o progresso da humanidade;")
            time.sleep(1)
            print("X - concessão de asilo político. ")
            time.sleep(1)
            resposta2=input("deseja cuntinuar ? [S] [N]")
            if resposta2 == 'N' :
                print("entendido")
                break
lista=[]
while True:
    user=input("as proximas sao mais complexas deseja entrar ?: [S] [N]")
    if user == 'N':
        break
    if user =='S':
        print("ok")
        registro=input("usuario: ")  #registro ADV   
        senha = input("digite uma senha: ")
        if senha.isnumeric():
            senha = int(senha)
        elif senha.isalpha():
            print('tenta denovo so que usando numeros ')
            senha = input("digite uma senha: ")
            if senha.isnumeric():
                senha = int(senha)

        oab=input('digite sua oab: ')
        if oab.isnumeric():
            oab = int(oab)
        print(f"ok {registro} da {oab} ")
        """
        for i in range(10):
            print("====================================================")
            lista.append(registro)
            lista.append(oab)
            lista.append(escolha)
            print(lista)
            if registro and oab and escolha == True:
                print(lista)
                """
