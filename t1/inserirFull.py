import mysql.connector

from tkinter import messagebox

from ConexaoFUL import conectar

from mysql.connector.connection import MySQLConnection

def inserir(descriTare,datIni,datTer,pessoResp,obser,prioridade):
    conexao, cursor = conectar()
    try:
        sql = f""" 
            INSERT INTO tabela_1
            (descriTare,datIni,datTer,pessoResp,observa,prioridade)
            values
            ('{descriTare}','{datIni}','{datTer}','{pessoResp}','{obser}','{prioridade}')           
            """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
    except mysql.connector.Error as falhas:
        messagebox.showerror("Falha","Falha ao cadastrar"+str(falhas))
    finally:
        conexao.close()
        cursor.close()
