from tkinter import *

# Configurações da janela
class Settings:
    def __init__(self, janela):
        janela.title("GereFácil App")
        janela.geometry("700x400+300+100")   
        janela.focus_set()
        janela.config(background="#F2522E")

# Frame inicial
class Frame1:
    def __init__(self):
        self.frm_inicio = Frame(janela, background="#592202", borderwidth=2, highlightbackground="#F27B35", highlightthickness=3)
        self.frm_inicio.place(relx=.1, rely=.1, relwidth=.8, relheight=.7)
        Button(self.frm_inicio, text="administrador".upper(), command=Frame2).place(relx=.18, rely=.4, relwidth=.3, relheight=.2)
        Button(self.frm_inicio, text="usuário".upper()).place(relx=.52, rely=.4, relwidth=.3, relheight=.2)

# Frame de login de adm
class Frame2:
    def __init__(self):
        self.login_adm = Frame(janela, background="#592202", borderwidth=2, highlightbackground="#F27B35", highlightthickness=3)
        self.login_adm.place(relx=.1, rely=.1, relwidth=.8, relheight=.7)
        Label(self.login_adm, text="Login").place(relx=.3, rely=.18, relwidth=.12, relheight=.1)
        Entry(self.login_adm, width=20).place(relx=.3, rely=.3, relwidth=.4, relheight=.1)
        Label(self.login_adm, text="Senha").place(relx=.3, rely=.5, relwidth=.12, relheight=.1)
        Entry(self.login_adm, width=20, show="*").place(relx=.3, rely=.62, relwidth=.4, relheight=.1)
        Button(self.login_adm, text="Entrar", command=Frame3).place(relx=.29, rely=.89, relwidth=.2, relheight=.1)
        Button(self.login_adm, text="Voltar", command=Frame1).place(relx=.51, rely=.89, relwidth=.2, relheight=.1)

# Freme de teste(pode retirar)
class Frame3:
    def __init__(self):
        self.frm_3 = Frame(janela, background="#592202", borderwidth=2, highlightbackground="#F27B35", highlightthickness=3)
        self.frm_3.place(relx=.1, rely=.1, relwidth=.8, relheight=.7)
        Label(self.frm_3, text="aleluia".upper()).place(relx=.3, rely=.18, relwidth=.12, relheight=.1)
        Button(self.frm_3, text="Voltar", command=Frame1).place(relx=.51, rely=.89, relwidth=.2, relheight=.1)


janela = Tk()
Settings(janela)
Frame1()
janela.mainloop()