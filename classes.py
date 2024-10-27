from tkinter import *

class App():
    def __init__(self):
        self.window = Tk()
        self.settings()
        self.botoes()
        mainloop()

    def settings(self):
        self.window.title("GereFácil App")
        self.window.geometry("480x400")
        self.window.configure(background="#262626")
        self.window.minsize(width= 480, height= 400)

    def botoes(self):
        self.botao_adm = Button(self.window, text="administrador".upper(), background="#A6A6A6")
        self.botao_adm.place(relx= 0.2, rely= 0.25, relwidth= 0.6, relheight= 0.2)

        self.botao_usuario = Button(self.window, text="usuário".upper(), background="#A6A6A6")
        self.botao_usuario.place(relx= 0.2, rely= 0.55, relwidth= 0.6, relheight= 0.2)