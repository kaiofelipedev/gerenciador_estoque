import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

class Grafico:
    def __init__(self):
        mydb = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "124578",
            database= "db_gerefacil")

        qtd = []
        nomes = []
        mycursor = mydb.cursor()

        mycursor.execute("SELECT qtd FROM produtos")
        quantidade = mycursor.fetchall()

        for x in quantidade:
            qtd += x

        mycursor.execute("SELECT nome_produto FROM produtos")
        produto = mycursor.fetchall()

        for y in produto:
            nomes += y


        grafico = np.array(qtd)
        titulos = nomes
        plt.pie(grafico, labels=titulos, shadow=True)
        plt.title("Estoque Atual")
        plt.show()
