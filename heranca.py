from Banco import Banco

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
            c = banco.conexao.cursor()
            c.execute("INSERT INTO gastos (tipo, tipo_pgto, valor, descrição) VALUES (?, ?, ?, ?)",
                      (self.tipo, self.tipo_pgto, self.valor, self.descrição))
            banco.conexao.commit()
            return "Cadastro realizado!"
        except Exception as e:
            return f"Erro de cadastro: {str(e)}"

    # Atualizar gasto
    def alteracliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                UPDATE gastos
                SET tipo = ?, tipo_pgto = ?, valor = ?, descrição = ?
                WHERE idgastos = ?
            """, (self.tipo, self.tipo_pgto, self.valor, self.descrição, self.idgastos))
            banco.conexao.commit()
            c.close()
            return "Gasto atualizado!"
        except Exception as e:
            return f"Erro na atualização: {str(e)}"

    # Deletar gasto
    def deletacliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM gastos WHERE idgastos = ?", (self.idgastos,))
            banco.conexao.commit()
            c.close()
            return "Gasto deletado!"
        except Exception as e:
            return f"O gasto não foi deletado: {str(e)}"

    # Consultar gasto
    def consultaGasto(self, idgastos):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM gastos WHERE idgastos = ?", (idgastos,))
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
