from tkinter import *
import tela_adm as ta
import mysql.connector

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
        self.lb_produto.place(rely=.01, relx=.01, relwidth=.3, relheight=.1)
        # Label de 'Descrição'
        self.lb_descricao = Label(self.frm_produto, text="Descrição", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_descricao.place(rely=.15, relx=.01, relwidth=.3, relheight=.1)
        # Label de 'Quantidade'
        self.lb_qtd = Label(self.frm_produto, text="Quantidade", fg="#F2522E",
                        font=("Verdana", 14, "bold"), background="#592202")
        self.lb_qtd.place(rely=.3, relx=.01, relwidth=.35, relheight=.1)
        # Entry de 'Produto'
        self.entry_produto = Entry(self.frm_produto, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                insertwidth=10)
        self.entry_produto.place(rely=.03, relx=.35, relwidth=.5, relheight=.08)
        self.entry_produto.focus()
        # Entry de 'Descrição'
        self.entry_descricao = Entry(self.frm_produto, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                insertwidth=10)
        self.entry_descricao.place(rely=.17, relx=.35, relwidth=.5, relheight=.08)
        # Entry de 'Quantidade'
        self.entry_qtd = Entry(self.frm_produto, font=("Arial", 12, "bold"),
                                bg="#D9AD29", fg="#592202", borderwidth=2,
                                relief="groove", insertbackground="#592202",
                                insertwidth=10, width=5)
        self.entry_qtd.place(rely=.31, relx=.4, relwidth=.15, relheight=.08)
        # Botão 'Cadastrar'
        self.bt_cadastrar = Button(self.frm_produto, text="Cadastrar", font=("Verdana", 12, "bold"),
                                   background="#D9AD29", foreground="#592202", border=6,
                                   relief=RAISED, activebackground="#D9AD29", activeforeground="green",
                                   command=self.cadastrar)
        self.bt_cadastrar.place(relx=.2, rely=.7, relwidth=.3, relheight=.2)
        # Botão 'Voltar'
        self.bt_voltar = Button(self.frm_produto, text="Voltar", bd=6, relief=RAISED,
                         font=("Verdana", 12, "bold"), background="#F2522E",activebackground="#F27B35", activeforeground="white", command=self.tela_adm)
        self.bt_voltar.place(relx=.8, rely=.9, relwidth=.2, relheight=.1)

    def tela_adm(self):
        self.frm_produto.place_forget()
        ta.TelaAdm(self.window)

    def cadastrar(self):
        produto = self.entry_produto.get()
        descricao = self.entry_descricao.get()
        qtd = self.entry_qtd.get()
        mydb = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "124578",
            database="db_gerefacil")
        
        mycursor = mydb.cursor()
        sql = ("INSERT INTO produtos (nome_produto, descricao, qtd) VALUES (%s, %s, %s)")
        val = (produto, descricao, qtd)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        self.entry_produto.delete(0, END)
        self.entry_descricao.delete(0, END)
        self.entry_qtd.delete(0, END)
        self.entry_produto.focus()
