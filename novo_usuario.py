from tkinter import *
import tela_adm as ta
import mysql.connector

class NovoUsuario:
    def __init__(self, window):
        self.window = window
        # Frame de novo usuário
        self.frm_new_user = Frame(self.window, bg="#592202", highlightthickness=5,
                                 highlightbackground="#D9AD29", bd=10, relief=RAISED)
        self.frm_new_user.place(relx=.2, rely=.1, relwidth=.6, relheight=.8)
        # Label de 'Nome'
        self.lb_nome = Label(self.frm_new_user, text="Nome", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_nome.grid(column=0, row=0, padx=10, sticky="nsew")
        # Label de 'Login'
        self.lb_login = Label(self.frm_new_user, text="Login", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_login.grid(column=0, row=2, padx=10, sticky="nsew")
        # Label de 'Senha'
        self.lb_senha = Label(self.frm_new_user, text="Senha", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_senha.grid(column=1, row=2, padx=10, sticky="nsew")
        # Label de 'Perfil'
        self.lb_perfil = Label(self.frm_new_user, text="Perfil", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_perfil.grid(column=1, row=0, padx=10, sticky="nsew")
        # Entry de 'Nome'
        self.entry_nome = Entry(self.frm_new_user, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                width=15, insertwidth=10)
        self.entry_nome.grid(column=0, row=1, pady=10, sticky="nsew")
        self.entry_nome.focus()
        # Entry de 'Login'
        self.entry_login = Entry(self.frm_new_user, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                width=15, insertwidth=10)
        self.entry_login.grid(column=0, row=3, padx=10, sticky="nsew")
        # Entry de 'Senha'
        self.entry_senha = Entry(self.frm_new_user, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                width=15, insertwidth=10, show="@")
        self.entry_senha.grid(column=1, row=3, padx=10, sticky="nsew")
        # Entry de 'Perfil'
        self.entry_perfil = Entry(self.frm_new_user, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                width=10, insertwidth=10)
        self.entry_perfil.grid(column=1, row=1, pady=10)
        # Botão 'Cadastrar'
        self.bt_cadastrar = Button(self.frm_new_user, text="Cadastrar", font=("Verdana", 12, "bold"),
                                   background="#D9AD29", foreground="#592202", border=6,
                                   relief=RAISED, activebackground="#D9AD29", activeforeground="green",
                                   command=self.cadastrar_usuario)
        self.bt_cadastrar.place(relx=.2, rely=.8, relwidth=.3, relheight=.2)
        # Botão 'Voltar'
        self.bt_voltar = Button(self.frm_new_user, text="Voltar", bd=6, relief=RAISED,
                         font=("Verdana", 12, "bold"), background="#F2522E",activebackground="#F27B35", activeforeground="white", command=self.tela_adm)
        self.bt_voltar.place(relx=.8, rely=.9, relwidth=.2, relheight=.1)

    def tela_adm(self):
        self.frm_new_user.place_forget()
        ta.TelaAdm(self.window)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        login = self.entry_login.get()
        senha = self.entry_senha.get()
        perfil = self.entry_perfil.get()
        mydb = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "124578",
            database="db_gerefacil")
        
        mycursor = mydb.cursor()
        sql = ("INSERT INTO usuarios (nome, login, senha, perfil) VALUES (%s, %s, %s, %s)")
        val = (nome, login, senha, perfil)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        self.entry_nome.delete(0, END)
        self.entry_login.delete(0, END)
        self.entry_senha.delete(0, END)
        self.entry_perfil.delete(0, END)