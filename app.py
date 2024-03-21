from dash import Dash, html, dcc, Output, Input, State
from PIL import Image
#custom
from components.header import generate_header
from callbacks.histogram_callbacks import register_histogram_callbacks
from utils.query_execution import execute_query, create_dataframe_from_query
from layouts.table import generate_table

# query_data = create_dataframe_from_query('data/queries/')
# col_name = query_data.columns

#instanciando o app
app = Dash(__name__)

def create_query_data(query_text):
    return create_dataframe_from_query(query_text)

pil_img = Image.open('components/assets/logo.png')

app.layout = html.Div(children=[
    html.Div(
        generate_header(pil_img),
        style={'textAlign': 'center'}
    ),
    
    html.Div(
        dcc.Textarea(
        id='textarea-state',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '80%', 'height': 150, 'margin':'auto'}
            ),
        ),
    
    html.Button('Submit', id='textarea-state-button', n_clicks=0),
    
    html.Div(id='output-container-button', style={'whiteSpace': 'pre-line'}),
    
    html.Div(id='table-container'),
    
    html.Div(id='datatable-interactivity-container')
    
])

@app.callback(
    Output('output-container-button', 'children'),
    Input('textarea-state-button', 'n_clicks'),
    State('textarea-state', 'value')
)
def update_query_data(n_clicks, value):
    if n_clicks > 0:
        col_names, result = execute_query(value)
        if col_names and result:
            df = create_query_data(value)
            return (
                html.Div([
                    html.Div(f'Query Data updated successfully with: {df.shape[0]} rows and {df.shape[1]} columns', style={'textAlign': 'center'}),
                    html.Div(id='query-data', style={'display': 'none'}, children=df.to_json())
                ]),
                generate_table(df)
            )
        else:
            return html.Div("Error executing query"), None

register_histogram_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)