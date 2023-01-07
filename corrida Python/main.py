# (A)Ambulancia (B)Bombeiro (C)CorsadaKath
# Painel com 6 'bolinhas' de cada carro
# Pista com 3 carros e 5 casas, ganha quem completar 5 pontos primeiro
# O andar dos Carros será definido por um while, os números deverão ser selecionados pelo Usuário

import random
import tkinter.messagebox
from tkinter import *

if __name__ == '__main__':
    check = 'N/A'
    root = Tk()
    a, b, c = 0, 0, 0
    painel = []
    btn = []
    label = []

    def criaPainel():
        aleatorio = 0
        contA = 0
        contB = 0
        contC = 0
        for i in range(18):
            while True:
                aleatorio = random.randint(1, 3)
                if aleatorio == 1 and contA < 6:
                    painel.append(aleatorio)
                    contA += 1
                    break
                elif aleatorio == 2 and contB < 6:
                    painel.append(aleatorio)
                    contB += 1
                    break
                elif aleatorio == 3 and contC < 6:
                    painel.append(aleatorio)
                    contC += 1
                    break
        j = 0
        for i in range(18):
            btn.append(Button(root, text=str(i), command=lambda j=j: pickNumero(j), width=5))
            btn[j].pack(side='left', padx=1)
            j += 1
        label.append(Label(root, text="A = " + str(a)))
        label.append(Label(root, text="B = " + str(b)))
        label.append(Label(root, text="C = " + str(c)))
        label[0].place(x=20,y=20)
        label[1].place(x=20, y=40)
        label[2].place(x=20, y=60)


    def pickNumero(numero):
        global a
        global b
        global c
        if painel[numero] == 1:
            btn[numero].configure(text='A')
            btn[numero]['bg'] = "gray"
            a += 1
        elif painel[numero] == 2:
            btn[numero].configure(text='B')
            btn[numero]['bg'] = "red"
            b += 1
        elif painel[numero] == 3:
            btn[numero].configure(text='C')
            btn[numero]['bg'] = "yellow"
            c += 1
        painel[numero] = 0
        refreshPlacar(a,b,c)
        if a == 6:
            tkinter.messagebox.showinfo("O JOGO ACABOU!", "O carro A venceu!")
            root.destroy()
        if b == 6:
            tkinter.messagebox.showinfo("O JOGO ACABOU!", "O carro B venceu!")
            root.destroy()
        if c == 6:
            tkinter.messagebox.showinfo("O JOGO ACABOU!", "O carro C venceu!")
            root.destroy()


    def refreshPlacar(a,b,c):
        label[0].configure(text="A = " + str(a))
        label[1].configure(text="B = " + str(b))
        label[2].configure(text="C = " + str(c))

    criaPainel()
    root.geometry('850x300')
    root.mainloop()
