from tkinter import *

class Buttons():
    def botao1(self):
        self.botao_adm = Button(self.window, text= "administrador".upper())
        self.botao_adm.place(relx= 0.25, rely= 0.3, relwidth= 0.5, relheight= 0.15)

    def botao2(self):
        self.botao_user = Button(self.window, text= "usuário".upper())
        self.botao_user.place(relx= 0.25, rely= 0.5, relwidth= 0.5, relheight= 0.15)

class App(Buttons):
    def __init__(self):
        self.window = Tk()
        self.settings()
        self.botao1()
        self.botao2()
        mainloop()
# Configurações da janela
    def settings(self):
        self.window.title("GereFácil App")
        self.window.geometry("480x400")
        self.window.configure(background="#F2522E")
        self.window.minsize(width= 480, height= 400)
# Tela inicial

    def frame_baixo(self):
        pass