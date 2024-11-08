from tkinter import *
import tela_inicial as ti
import mysql.connector
import tela_adm as ta

class TelaLogin:
    def __init__(self, window):
        self.window = window
        self.frm_login = Frame(self.window, background="#D9AD29", border=8,
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
        self.entry_login.focus()
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
        # Botão 'Entrar'
        self.bt_entrar = Button(self.frm_login, text="Entrar", relief=RAISED, bd=6,
                     font=("Verdana", 10, "bold"), background="#F2522E", activebackground="#F27B35",activeforeground="white",
                     command=self.checarlogin)
        self.bt_entrar.place(relx=.73, rely=.83, relwidth=.25, relheight=.15)
#############################   CONTINUAR DAQUI   #################################
    def checarlogin(self):
        self.user = ti.TelaInicial(self.window)
        login = self.entry_login.get()
        senha = self.entry_senha.get()
        mydb = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "124578",
            database= "db_gerefacil"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT login, senha, perfil FROM usuarios")
        resultado = mycursor.fetchall()
        print(resultado)
        for x in resultado:
            if login in x[0] and senha in x[1] and self.user.perfil_adm in x[2]:
                self.ir_tela_adm()
            else:
                print("senha incorreta")

        mydb.close()
####################################################################################
    def voltar_tela_inicial(self):
        self.frm_login.place_forget()
        ti.TelaInicial(self.window)

    def ir_tela_adm(self):
        self.frm_login.place_forget()
        ta.TelaAdm(self.window)