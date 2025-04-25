from Banco import Banco
from supabase import create_client
# from supabase import create_client, Client

url = 'https://dirdlupkocponlqfiulq.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRpcmRsdXBrb2Nwb25scWZpdWxxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU0Mzc3NDAsImV4cCI6MjA2MTAxMzc0MH0.vbNrQAzL7rMsLDCJIUyRm1cpw_ZwmXUqzOiLFwX6Lho'

supabase = create_client(url, key)

class heranca(object):
    def __init__(self, idgastos=0, tipo="", tipo_pgto="", valor="", descrição="", xview="", yview=""):
        self.info = {}
        self.idgastos = idgastos
        self.tipo = tipo
        self.tipo_pgto = tipo_pgto
        self.valor = valor
        self.descrição = descrição
        self.xview = xview
        self.yview = yview

    # Inserir gasto
    def inseregasto(self):
        banco = Banco()
        try:
            # Insere no banco local
            c = banco.conexao.cursor()
            c.execute("INSERT INTO gastos (tipo, tipo_pgto, valor, descrição) VALUES (?, ?, ?, ?)",
                      (self.tipo, self.tipo_pgto, self.valor, self.descrição))
            banco.conexao.commit()

            # Insere no Supabase
            supabase.table('gastos').insert({
                # Inserção sem o campo 'idgastos' porque ele é autoincrementado
                'tipo': self.tipo,
                'tipo_pgto': self.tipo_pgto,
                'valor': self.valor,
                'descrição': self.descrição
            }).execute()

            return "Cadastro realizado com sucesso!"
        except Exception as e:
            return f"Erro de cadastro: {str(e)}"
        
    # Atualizar gasto
    def alteragasto(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                UPDATE gastos
                SET tipo = ?, tipo_pgto = ?, valor = ?, descrição = ?
                WHERE idgastos = ?
            """, (self.tipo, self.tipo_pgto, self.valor, self.descrição, self.idgastos))
            banco.conexao.commit()
        
        # Atualizar no Supabase

            return "Gasto atualizado com sucesso!"
        except Exception as e:
            return f"Erro ao atualizar gasto: {str(e)}"

    # Deletar gasto
    def deletagasto(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM gastos WHERE idgastos = ?", (self.idgastos,))
            banco.conexao.commit()
        
            # Deletar no Supabase

            return "Gasto deletado com sucesso!"
        except Exception as e:
            return f"Erro ao deletar gasto: {str(e)}"    

    # Consultar gasto
    def consultaGasto(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM gastos WHERE idgastos = ?", (self.idgastos,))
            resultado = c.fetchone()
            c.close()
            banco.conexao.close()
            if resultado:
                self.idgastos = resultado[0]
                self.tipo = resultado[1]
                self.tipo_pgto = resultado[2]
                self.valor = resultado[3]
                self.descrição = resultado[4]
                return "Consulta realizada com sucesso!"
            else:
                return "Gasto não encontrado!"
        except Exception as e:
            return f"Erro de consulta: {str(e)}"
