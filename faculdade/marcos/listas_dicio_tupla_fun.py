from time import sleep
print("aula com o Mestre Marcos. ")
print("-------")
sleep(1)
'''
dicionario e defenido pr {}
cor= {"green":"verde","blue":"azul","red":"vermelho"}
listas=[]
dicio={}
tuplas=()

'''

'''
cor= {"green":"verde","blue":"azul","red":"vermelho"}
sleep(1)
print(cor)
sleep(1)
print(cor["green"])
sleep(1)
print(cor["blue"])
sleep(1)
print(cor["red"])
sleep(1)
cor["yellow"]="amarelo"
sleep(1)
print(cor)
cor["green"]="frog"
print(cor)
'''
'''
pessoa={"nome":"marcos","idade":"33","profissao":"professor"}
print(pessoa)
'''

#pessoatupla=("marcos",33,"professor")




#---------------------------------------------------------

idade=[]
media2=[]
x=input("digite sua idade: ")
x=int(x)
idade.append(x)
x2=input("digite sua idade:  ")
x2=int(x2)
idade.append(x2)
x3=input("digite sua idade: ")
x3=int(x3)
idade.append(x3)
soma=sum(idade)
media=soma/len(idade)
idade.append(media)
media2.append(media)
print(idade)
print(media)
