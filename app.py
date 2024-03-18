from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

#custom
from layouts.table import create_table
from utils.query_execution import create_dataframe_from_query, execute_query
from utils.data_processing import create_histogram 

col_name, _ = execute_query('data/queries/')
query_data = create_dataframe_from_query('data/queries/')

#instanciando o app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
        dcc.Dropdown(col_name, 'produtividade', id='column-dropdown', placeholder='Select a coluna'),
            html.Div(id='table-container'
        )
    ]),
    
    html.Div(id='histogram-container', children=[
        html.H1('Histogram'),
        dcc.Graph(id='histogram')
    ]),
    
    create_table()
])

@app.callback(
    Output('table-container', 'children'),
    [Input('column-dropdown', 'value')])
def update_output(value):
    return f'You have selected {value}'

@app.callback(
    Output('histogram', 'figure'),
    [Input('column-dropdown', 'value')])
def update_histograms(selected_columns):
    if selected_columns:
        fig = create_histogram(query_data, selected_columns)
        print(f'Coluna selecionada {selected_columns}')
        return fig
    else:
        print('No column selected')
        return {'data': [], 'layout': {}}
    
    
if __name__ == '__main__':
    app.run_server(debug=True)