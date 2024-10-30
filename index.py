from tkinter import *


class Janela():
    def __init__(self, window):
        janela = window
        janela.title("GereFácil App")# title so aceita um argumento!
        janela.geometry("700x400+300+100")# width, height, x, y
        janela.minsize(550, 350)
        janela.config(background="#F2522E", highlightthickness=8,
                  highlightcolor="#592202", border=8, relief=RAISED)


class TelaInicial:
    def __init__(self):
        # Frame
        self.frm = Frame(window, background="#D9AD29", border=8,
                highlightcolor="#592202", highlightthickness=8,
                highlightbackground="#592202", relief=RAISED)
        self.frm.place(relwidth=.8, relheight=.7, relx=.1, rely=.1)
        # Label
        self.lb = Label(self.frm, text="Welcome", border=4, relief=RAISED,
                        font=("Verdana", 14, "bold"), background="#F2522E",highlightbackground="#592202", highlightthickness=2)
        self.lb.place(relwidth=.3, relheight=.2, relx=.35)
        # Botão Adm
        self.bt_adm = Button(self.frm, text="Administrador", bd=6, relief=RAISED,
                         font=("Verdana", 12, "bold"), background="#F2522E",activebackground="#F27B35", activeforeground="white",
                         command=self.login_adm)
        self.bt_adm.place(relx=.1, rely=.5, relwidth=.35, relheight=.25)
        # Botão usuário
        self.bt_user = Button(self.frm, text="Usuário", relief=RAISED, bd=6,
                     font=("Verdana", 12, "bold"), background="#F2522E", activebackground="#F27B35",activeforeground="white",
                     command=self.login_usuario)
        self.bt_user.place(relx=.55, rely=.5, relwidth=.35, relheight=.25)


    def login_adm(self):
        perfil = 'adm'
        self.frm.place_forget()
        TelaLogin()
        print(perfil)

    def login_usuario(self):
        perfil = 'usuario'
        self.frm.place_forget()
        TelaLogin()
        print(perfil)


class TelaLogin:
    def __init__(self):
        self.frm_login = Frame(window, background="#D9AD29", border=8,
                highlightcolor="#592202", highlightthickness=8,
                highlightbackground="#592202", relief=RAISED)
        self.frm_login.place(relwidth=.5, relheight=.7, relx=.25, rely=.1)
        # Label 'Login'
        self.lb_login = Label(self.frm_login, text="Login", border=4, relief=RAISED,
                        font=("Verdana", 12, "bold"), background="#F2522E",highlightbackground="#592202", highlightthickness=2)
        self.lb_login.place(relx=.1, rely=.1, relwidth=.3, relheight=.2)
        # Label 'Senha'
        self.lb_senha = Label(self.frm_login, text="Senha", border=4, relief=RAISED,
                        font=("Verdana", 12, "bold"), background="#F2522E",highlightbackground="#592202", highlightthickness=2)
        self.lb_senha.place(relx=.1, rely=.48, relwidth=.3, relheight=.2)
        # Entry de 'Login'
        self.entry_login = Entry(self.frm_login, font=("Arial", 12),
                                bg="#592202", fg="white", borderwidth=6,
                                relief="groove", insertbackground="white",
                                insertwidth=10)
        self.entry_login.place(relx=.1, rely=.32, relwidth=.6, relheight=.15)
        # Entry de 'Senha'
        self.entry_senha = Entry(self.frm_login, font=18,
                                bg="#592202", fg="white", borderwidth=6,
                                relief="groove", show="@", insertbackground="white",
                                insertwidth=10)
        self.entry_senha.place(relx=.1, rely=.7, relwidth=.6, relheight=.15)
        # Botão 'voltar'
        self.bt_voltar = Button(self.frm_login, text="Voltar", relief=RAISED, bd=6,
                     font=("Verdana", 10, "bold"), background="#F2522E", activebackground="#F27B35",activeforeground="white",
                     command=self.voltar_tela_inicial)
        self.bt_voltar.place(relx=.73, rely=0.01, relwidth=.25, relheight=.15)

    def voltar_tela_inicial(self):
        self.frm_login.place_forget()
        TelaInicial()


# Variável recebendo o Tk (janela) 
window = Tk()
Janela(window)
TelaInicial()
window.mainloop()# executando o loop para mostrar a janela
