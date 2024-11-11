from tkinter import *
import tela_adm as ta

class NovoProduto:
    def __init__(self, window):
        self.window = window
        # Frame de novo produto
        self.frm_produto = Frame(self.window, bg="#592202", highlightthickness=5,
                                 highlightbackground="#D9AD29", bd=10, relief=RAISED)
        self.frm_produto.place(relx=.2, rely=.1, relwidth=.6, relheight=.8)
        # Label de 'Produto'
        self.lb_produto = Label(self.frm_produto, text="Produto", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_produto.grid(column=0, row=0, pady=10)
        # Label de 'Descrição'
        self.lb_descricao = Label(self.frm_produto, text="Descrição", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_descricao.grid(column=0, row=1, pady=10)
        # Label de 'Quantidade'
        self.lb_qtd = Label(self.frm_produto, text="Quantidade", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_qtd.grid(column=0, row=2, pady=10)
        # Entry de 'Produto'
        self.entry_produto = Entry(self.frm_produto, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                insertwidth=10)
        self.entry_produto.grid(column=1, row=0)
        # Entry de 'Descrição'
        self.entry_descricao = Entry(self.frm_produto, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                insertwidth=10)
        self.entry_descricao.grid(column=1, row=1)
        # Entry de 'Quantidade'
        self.entry_qtd = Entry(self.frm_produto, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                insertwidth=10, width=5)
        self.entry_qtd.grid(column=1, row=2)

