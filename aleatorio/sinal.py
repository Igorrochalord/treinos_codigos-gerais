from tkinter import *
from time import sleep

semaforo = Tk()
semaforo.title("lolo as 10")
for i in range (4):
    sleep(0.6)
    print("vermelho")
    label_vermelho = Label(semaforo,text='maconha')
    label_vermelho["bg"] = ["red"]
    label_vermelho.pack()
    label_vermelho.destroy()
for i in range (4):
    sleep(0.6)
    print("amarelo")
    label_amarelo = Label(semaforo,text='cocaina')
    label_amarelo["bg"] = ["yellow"]
    label_amarelo.pack()
    label_amarelo.event_add()
for i in range (4):
    sleep(0.6)
    print("verde")
    label_verde = Label(semaforo,text='maconha')
    label_verde["bg"] = ["green"]
    label_verde.pack()
    label_verde.destroy()



semaforo.mainloop()