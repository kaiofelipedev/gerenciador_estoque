from tkinter import *

def Login_adm():
    frm_inicio.place_forget()
    login_adm.place(relx=.1, rely=.1, relwidth=.8, relheight=.7)

def back_top():
    login_adm.place_forget()
    frm_inicio.place(relx=.1, rely=.1, relwidth=.8, relheight=.7)


janela = Tk()
# tela
janela.title("GereFácil App")
janela.geometry("700x400+300+100")
janela.focus_set()
janela.config(background="#F2522E")
# frames da tela inicial
frm_inicio = Frame(janela, background="#592202", borderwidth=2, highlightbackground="#F27B35", highlightthickness=3)
frm_inicio.place(relx=.1, rely=.1, relwidth=.8, relheight=.7)
# botões da tela inicial
Button(frm_inicio, text="administrador".upper(), command=Login_adm).place(relx=.18, rely=.4, relwidth=.3, relheight=.2)
Button(frm_inicio, text="usuário".upper()).place(relx=.52, rely=.4, relwidth=.3, relheight=.2)
#tela login adm
login_adm = Frame(janela, background="#592202", borderwidth=2, highlightbackground="#F27B35", highlightthickness=3)
Label(login_adm, text="Login").place(relx=.3, rely=.18, relwidth=.12, relheight=.1)
Entry(login_adm, width=20).place(relx=.3, rely=.3, relwidth=.4, relheight=.1)
Label(login_adm, text="Senha").place(relx=.3, rely=.5, relwidth=.12, relheight=.1)
Entry(login_adm, width=20, show="*").place(relx=.3, rely=.62, relwidth=.4, relheight=.1)
Button(login_adm, text="Entrar").place(relx=.29, rely=.89, relwidth=.2, relheight=.1)
Button(login_adm, text="Voltar", command=back_top).place(relx=.51, rely=.89, relwidth=.2, relheight=.1)

janela.mainloop()