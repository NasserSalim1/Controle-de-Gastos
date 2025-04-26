from flask import Flask, render_template, request, redirect, url_for
from supabase_client import supabase

app = Flask(__name__)

@app.route('/')
def index():
    data = supabase.table('gastos').select("*").execute().data
    return render_template('index.html', registros=data)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        novo = {
            "tipo_movimentacao": request.form['tipo_movimentacao'],
            "forma_pagamento": request.form['forma_pagamento'],
            "valor": float(request.form['valor']),
            "categoria": request.form['categoria'],
            "descricao": request.form['descricao']
        }
        supabase.table('gastos').insert(novo).execute()
        return redirect(url_for('index'))
    return render_template('form.html', acao='Adicionar')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        atualizado = {
            "tipo_movimentacao": request.form['tipo_movimentacao'],
            "forma_pagamento": request.form['forma_pagamento'],
            "valor": float(request.form['valor']),
            "categoria": request.form['categoria'],
            "descricao": request.form['descricao']
        }
        supabase.table('gastos').update(atualizado).eq('id', id).execute()
        return redirect(url_for('index'))
    registro = supabase.table('gastos').select("*").eq('id', id).execute().data[0]
    return render_template('form.html', acao='Editar', registro=registro)

@app.route('/excluir/<int:id>')
def excluir(id):
    supabase.table('gastos').delete().eq('id', id).execute()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)