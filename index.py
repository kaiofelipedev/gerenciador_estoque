from tkinter import *
import tela_inicial as ti


class Janela():
    def __init__(self, window):
        janela = window
        janela.title("GereFácil App")# title so aceita um argumento!
        janela.geometry("700x400+300+100")# width, height, x, y
        janela.minsize(550, 350)
        janela.config(background="#F2522E", highlightthickness=8,
                  highlightcolor="#592202", border=8, relief=RAISED)


# Variável recebendo o Tk (janela) 
window = Tk()
Janela(window)
ti.TelaInicial(window)
window.mainloop()# executando o loop para mostrar a janela
