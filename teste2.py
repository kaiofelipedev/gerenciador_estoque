import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Entry")

# Criar uma Entry
entry = tk.Entry(root, 
                 width=30,  # Largura da Entry
                 font=("Arial", 12),  # Fonte e tamanho do texto
                 bg="lightgray",  # Cor de fundo
                 fg="black",  # Cor do texto
                 borderwidth=2,  # Largura da borda
                 relief="groove"  # Estilo da borda
                 )

# Adicionar a Entry à janela
entry.pack(padx=10, pady=10)

# Iniciar o loop principal
root.mainloop()