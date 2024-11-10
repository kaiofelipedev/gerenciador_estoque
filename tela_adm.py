from tkinter import *
from tkinter import ttk
import tela_inicial as ti

class TelaAdm:
    def __init__(self, window):
        self.window = window
        self.frm_adm = Frame(self.window, background="#D9AD29", highlightthickness=1,
                  highlightcolor="#592202", border=5, relief=RAISED)
        self.frm_adm.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
        # Label 'Adm'
        self.lb_adm = Label(self.frm_adm,  text="Adm", border=4, relief=SUNKEN,
                        font=("Verdana", 14, "bold"), background="#592202", highlightthickness=4,
                        fg="white")
        self.lb_adm.place(relwidth=.2, relheight=.12)
        # Botão 'Sair'
        self.bt_sair = Button(self.frm_adm, text="Sair", fg="white", border=4,
                            font=("Verdana", 10, "bold"),highlightthickness=4,relief=RAISED, background="#F2522E",
                            highlightbackground="#592202", command=self.inicio)
        self.bt_sair.place(relx=.9, relwidth=.1, relheight=.08)
        # Botão 'Novo Produto'
        self.novo_produto = Button(self.frm_adm,  text="Novo Produto", border=8,
                        font=("Verdana", 9, "bold"), relief=SUNKEN, fg="white",
                        background="#592202")
        self.novo_produto.place(relx=.01, rely=.87, relwidth=.2, relheight=.12)
        # Botão 'Novo Usuário'
        self.novo_user = Button(self.frm_adm,  text="Novo Usuário", border=8,
                        font=("Verdana", 9, "bold"), relief=SUNKEN, fg="white",
                        background="#592202")
        self.novo_user.place(relx=.4, rely=.87, relwidth=.2, relheight=.12)
        # Botão 'Gráfico'
        self.bt_grafico = Button(self.frm_adm,  text="Gráfico", border=8,
                        font=("Verdana", 9, "bold"), relief=SUNKEN, fg="white",
                        background="#592202")
        self.bt_grafico.place(relx=.79, rely=.87, relwidth=.2, relheight=.12)
        ###########   Treeview   ############
        self.tv = ttk.Treeview(self.frm_adm, columns=("Id", "Produto",
        "Descrição", "Qtd"))
        self.tv.column("#0", width=0)
        self.tv.column("Id", width=1, stretch=True, anchor="center")
        self.tv.heading("Id", text="ID")
        self.tv.column("Produto", width=30, stretch=True, anchor="center")
        self.tv.heading("Produto", text="Produto")
        self.tv.column("Descrição", width=120, stretch=True, anchor="center")
        self.tv.heading("Descrição", text="Descrição")
        self.tv.column("Qtd", width=1, stretch=True, anchor="center")
        self.tv.heading("Qtd", text="Qtd")
        self.tv.place(relx=.02, rely=.14, relwidth=.96, relheight=.7)
        self.tv.insert("", "end", values=(1, "teclado", "teclado desktop", 15))

    def inicio(self):
        self.frm_adm.place_forget()
        ti.TelaInicial(self.window)
