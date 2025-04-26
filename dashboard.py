# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc 
import plotly.express as px 
import pandas as pd
from supabase_client import supabase

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(supabase.table('gastos').select("*").execute().data)
df_grouped = df.groupby("forma_pagamento").agg({'valor': 'sum'}).reset_index()

#criando o gráfico
fig = px.bar(df_grouped, x="forma_pagamento", y="valor", color="forma_pagamento", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)