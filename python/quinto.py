print("this progam will 'print' the most bigger number")
num1=input("number: ")
num2=input("number: ")
num3=input("number: ")
if num1.isnumeric()and num2.isnumeric()and num2.isnumeric():
    num1=int(num1)
    num2=int(num2)
    num3=int(num3)
    if num1>num2 and num3:
        print(f"{num1} is the bigger of the three")
    elif num2>num3 and num1:
        print(f"{num2} is the bigger of the three")
    elif num3>num1 and num2:
        print(f"{num3} is the bigger of the three")