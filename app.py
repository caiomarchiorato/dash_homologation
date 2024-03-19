from dash import Dash, html, dcc
#custom
from callbacks.tables_callbacks import register_table_callbacks
from callbacks.histogram_callbacks import register_histogram_callbacks
from layouts.table import create_table
from layouts.charts import generate_histogram_layout
from utils.query_execution import create_dataframe_from_query, execute_query

col_name, _ = execute_query('data/queries/')
query_data = create_dataframe_from_query('data/queries/')

#instanciando o app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
        dcc.Input(id="input-queries", type="text", placeholder="Digite a query"),
        html.Button("Executar queries", id="button-executar-queries", n_clicks=0),
    ]),
    html.Div([
        dcc.Dropdown(col_name, id='column-dropdown', placeholder='Select a coluna'),
            html.Div(id='table-container'
        )
    ]),
    
    generate_histogram_layout(query_data, col_name[0]),    
    create_table()
])


# @app.callback(
#     Output('table-container', 'children'),
#     [Input('button-executar-queries', 'n_clicks')],
#     [State('input-queries', 'value')]
# )
# def execute_query_and_update_table(n_clicks, query):
#     if n_clicks > 0:
#         df = create_dataframe_from_query(query)
#         global query_data
#         query_data = df
#         return f"A consulta foi executada com sucesso: {query}"
#     else:
#         return "Nenhuma consulta foi executada ainda."

register_table_callbacks(app)
register_histogram_callbacks(app, query_data)


if __name__ == '__main__':
    app.run_server(debug=True)