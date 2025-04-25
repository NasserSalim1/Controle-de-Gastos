###################### Arquivo de teste ######################

import sqlite3
from supabase import create_client

url = 'https://dirdlupkocponlqfiulq.supabase.co'
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRpcmRsdXBrb2Nwb25scWZpdWxxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU0Mzc3NDAsImV4cCI6MjA2MTAxMzc0MH0.vbNrQAzL7rMsLDCJIUyRm1cpw_ZwmXUqzOiLFwX6Lho'

supabase = create_client(url, key)

# Conectando ao SQLite local
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
cursor.execute("SELECT tipo, tipo_pgto, valor, descrição FROM gastos")
dados = cursor.fetchall()

# Inserindo no Supabase
for linha in dados:
    tipo, tipo_pgto, valor, descricao = linha
    valor = valor.replace(',', '.')  # Corrige a vírgula para ponto
    # Inserção sem o campo 'idgastos' porque ele é autoincrementado
    supabase.table('gastos').insert({
        'tipo': tipo,
        'tipo_pgto': tipo_pgto,
        'valor': valor,
        'descrição': descricao
    }).execute()

print("Dados importados com sucesso!")