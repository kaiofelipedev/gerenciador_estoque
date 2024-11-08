from tkinter import *
import tela_login as tl


class TelaInicial:
    def __init__(self, window):
        self.window = window
        self.perfil_adm = ""
        self.perfil_usuario = ""
        # Frame
        self.frm = Frame(self.window, background="#D9AD29", border=8,
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
        self.perfil_adm = 'adm'
        self.frm.place_forget()
        tl.TelaLogin(self.window)
        print(self.perfil_adm)

    def login_usuario(self):
        self.perfil_usuario = 'usuario'
        self.frm.place_forget()
        tl.TelaLogin(self.window)
        print(self.perfil_usuario)