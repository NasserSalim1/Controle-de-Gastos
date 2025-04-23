#importanto os dados dos SQLite
import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
            c = self.conexao.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS gastos (
                    idgastos INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT,
                    tipo_pgto TEXT,
                    valor TEXT,
                    descrição TEXT
                    )""")
            self.conexao.commit()
            c.close()