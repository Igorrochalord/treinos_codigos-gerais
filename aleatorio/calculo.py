from multiprocessing.resource_sharer import stop


while True:
    print('ola ser vivo')
    print("")
    valor1=input("valor: ")
    valor2=input("valor: ")
    operador=input("bote um operador: ")
    
    if valor1.isnumeric() and valor2.isnumeric:
        valor1=int(valor1)
        valor2=int(valor2)
    if operador == '*':
        x = valor1 * valor2
        print(f"multiplicaçao {[x]}")
        for i in range(0 , 11):
            i = i* x 
            print(f'a tabuada brinde: {[i]}')
    if operador == '%':
        x = valor1 % valor2
        print(f"a divisao deu: {[x]}")
        
    elif operador == '+':
        x = valor1 + valor2
        print(f"a adiccao deu: {[x]}")
    elif operador == '-':
        x = valor1 - valor2
        print(f"a subtraçao deu: {[x]}")      
    pr = input("deseja cuntinuar [S]im // [N]ao: ")
    if pr == 's':
        print('ok')
    elif pr == 'n':
        print("ok")
        break