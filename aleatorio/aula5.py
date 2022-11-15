"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
print("ola vamos dar um molhada nas notas")
while (4):
    nota1=int(input("digite a nota recebida no 1 bimestre: "))
    nota2=int(input("digite a nota recebida no 2 bimestre: "))
    res= nota1+nota2 
    print("ok")
    if res  >=7:
        print(f"parabens sua nota foi:{res}")
    elif res <=6:
        print(f"infelizmente voce esta reprovado: {res}")
    if res ==10:
        print(f"aprovado com distinçao: {res}")
    else:
        print("digite um numero valido")
        break