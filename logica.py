from heranca import heranca
from banco import Banco

class Logica:
    def __init__(self):
        self.banco = Banco()  # Instância da classe Banco

    def inserircliente(self):
        usu = heranca()
        usu.tipo = self.tipo.get()
        # Atribua os outros dados

        return usu.inserecliente()

    def consultarcliente(self):
        usu = heranca()
        idgastos = self.idgastos.get()
        return usu.consultacliente(idgastos)
        
    # Crie os outros métodos aqui, como atualizar e excluir

    def mostratela(self):
        try:
            c = self.banco.conexao.cursor()
            self.tree.delete(*self.tree.get_children())
            c.execute("SELECT * FROM usuarios")
            fetch = c.fetchall()
            for data in fetch:
                self.tree.insert('', 'end', values=(data[0], data[1], data[2]))
            c.close()
        except Exception as e:
            return f"Erro de consulta: {str(e)}"
