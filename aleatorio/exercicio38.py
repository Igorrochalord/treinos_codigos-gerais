
from time import sleep
from random import randint
while True:
    print("determinador de salario")
    x=input("qual linguagem deseja escolher 1=[PT-BR] 2=[ENGLISH] 3=[GERMANY]: ") 
    if x=='2':
                print("Salary Determiner")
                name=input("name: ")
                age=input("age: ")
                job=input("last job: ")
                position=input("desired position: ")
                salary=input("last salary: ")
                salaryd=input("desired salary: ")
                registration=[]
                if name.isnumeric():
                    name=int(name)
                    sleep(1)
                    print("Invalid name, enter letters not numbers")
                    if name.isalpha():
                        sleep(1)
                        print("saved")
                    if age.isnumeric():
                        age=int(age)
                        sleep(1)
                        print("ok saved")
                    elif age.isalpha():
                        print("try again")
                registration.append(name)
                registration.append(age)
                registration.append(position)
                registration.append(salary)
                registration.append(salaryd)
                sleep(0.2)
                print(registration)
                print()
                for i in range(6):
                    sleep(0.2)
                    print("=============LOADING===================")
                    print(f"ok sir {name} ")
                    print()
                    print()
                    print("let's analyze your cpf")
                    cpf=int(input("CPF: "[:8]))
                    if cpf <=9:
                        print(f"sir {name} you missed the security step \nwe will start over ")
                        print(registration)
                        for i in range(30):
                            sleep(1)
                            print("END OF PROGRAM")
                            break
                        print("understood ")
                    registration.append(cpf)
                    print("ok you passed the security step, now we will generate a password for you")
                    password=randint(100,100000000)
                    security=password*74
                    print(f"your password is {security}")
                    break
    
    elif x=="1":
        nome=input("nome: ")
        idade=input("idade: ")
        cargo=input("ultimo cargo: ")
        cargod=input("cargo desejado: ")
        salario=input("ultimo salario: ")
        salariod=input("salario desejado: ")
        cadastro=[]
        if nome.isnumeric():
            nome=int(nome)
            sleep(1)
            print("invalidade de nome , digite letras nao numeros")
        if nome.isalpha():
            sleep(1)
            print("guardado")
        if idade.isnumeric():
            idade=int(idade)
            sleep(1)
            print("ok guardado")
        elif idade.isalpha():
            print("tenta denovo")
        cadastro.append(nome)
        cadastro.append(idade)
        cadastro.append(cargo)
        cadastro.append(salario)
        cadastro.append(salariod)
        sleep(0.2)
        print(cadastro)
        print()
        for i in range(6):
            sleep(1)
            print("===========CARREGANDO=================")       
        print(f"ok senhor {nome}  ")
        print()
        print()
        print("vamos analisar seu cpf")
        cpf=int(input("CPF: "[:8]))
        if cpf <=9:
                print(f"senhor {nome} voce errou a etapa de segurança \n iremos recomeçar ")
                print(cadastro)
                for i in range(30):
                    sleep(1)
                print("FIM DO PROGAMA")
                break   
        if cpf.isnumeric():
            cpf=int(cpf)
            print("entendido ")
            cadastro.append(cpf)
        print("ok o senhor passou na etapa de segurança , agora iremos gerar uma senha para você")
        senha=randint(100,100000000)
        segurança= senha*74
        print(f"sua senha e {segurança}")

