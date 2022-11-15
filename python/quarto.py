
nota1=input("Please put your grates: ")
nota2=input("Please put your grates: ")
nota3=input("Please put your grates: ")
if nota1.isnumeric() and nota2.isnumeric()and nota3.isnumeric():
    nota1=int(nota1)
    nota2=int(nota2)
    nota3=int(nota3)
    so=nota1+nota2+nota3
    media = so /3
    if media <=5:
        print(f"Thank You but you don't have the media: {media}")
    elif media >=6:
        print(f"your total grates are: {media} you passed")