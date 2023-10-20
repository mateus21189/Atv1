
from ConexaoFUL import conectar

import mysql.connector
from tkinter import messagebox



def atualizarCadastro(id, descriTare, datIni,datTer ,pessoResp, observa,prioridade):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tabela_1
            SET descriTare='{descriTare}', datIni='{datIni}',
            datTer='{datTer}', pessoResp='{pessoResp}',observa='{observa}',prioridade='{prioridade}' WHERE id='{id}'
              """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()
