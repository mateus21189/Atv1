

from ConexaoFUL import conectar
import mysql.connector
from tkinter import messagebox










def consultar():
    conexao, cursor = conectar()
    try:
        sqlConsulta = "SELECT * FROM tabela_1"
        cursor.execute(sqlConsulta)
        resultado = cursor.fetchall()
        return resultado
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao consultar! "+str(falha))
        return None
    finally:
        conexao.close()
        cursor.close()

