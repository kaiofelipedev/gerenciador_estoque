from tkinter import *
from tkinter import ttk
import tela_inicial as ti

class TelaUsuario:
    def __init__(self, window):
        # Frame
        self.window = window
        self.frm_usuario = Frame(self.window, background="#D9AD29", highlightthickness=1,
                  highlightcolor="#592202", border=5, relief=RAISED)
        self.frm_usuario.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)

        # Label 'Usuário'

        self.lb_usuario = Label(self.frm_usuario,  text="Usuário", border=4, relief=SUNKEN,
                        font=("Verdana", 14, "bold"), background="#592202", highlightthickness=4,
                        fg="white")
        self.lb_usuario.place(relwidth=.2, relheight=.12)

        # Label 'Estoque Atual'

        self.lb_estoque = Label(self.frm_usuario,  text="Estoque Atual", border=4, relief=SUNKEN,
                        font=("Verdana", 12, "bold"), background="#592202", fg="white")
        self.lb_estoque.place(relx=.3, rely=.15, relwidth=.4, relheight=.1)

        # Botão sair
        
        self.bt_sair = Button(self.frm_usuario, text="Sair", fg="white", border=4,
                            font=("Verdana", 10, "bold"),highlightthickness=4,relief=RAISED, background="#F2522E", highlightbackground="#592202",
                            command=self.bt_sair)
        self.bt_sair.place(relx=.9, relwidth=.1, relheight=.08)

        ###########   Treeview   ############

        self.tv = ttk.Treeview(self.frm_usuario, columns=("Id", "Produto",
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
        self.tv.place(relx=.02, rely=.27, relwidth=.96, relheight=.7)
        self.tv.insert("", "end", values=(1, "teclado", "teclado desktop", 15))

    def bt_sair(self):
        self.frm_usuario.place_forget()
        ti.TelaInicial(self.window)
