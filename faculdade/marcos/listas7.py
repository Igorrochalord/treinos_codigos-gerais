
num = []
i = 0
while len(num) != 5:
   i += 1
   print("Diga o número " + str(i) + "º:")
   try:
       numero = int(input())
   except:
       print("Número inválido.")
       i -= 1
       continue
   num.append(numero)
print("Números: " + ", ".join(str(numero) for numero in num))
soma = sum(num)
print("Soma: " + str(soma))
multiplicacao = 1
for numero in num:
   multiplicacao = multiplicacao * numero
print("Multiplicação: " + str(multiplicacao))