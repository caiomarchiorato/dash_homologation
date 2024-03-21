from dash import Dash, html, dcc, Output, Input, State
from PIL import Image
#custom
from components.header import generate_header
from callbacks.histogram_callbacks import register_histogram_callbacks
from callbacks.update_query_data import register_query_data_update
from utils.query_execution import create_dataframe_from_query

#instanciando o app
app = Dash(__name__)

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
        style={'width': '100%', 'height': 150, 'margin':'auto'}
            ),
        ),
    
    html.Div(
        dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), style={'width': '80%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': 'auto'}
        )),
    
    html.Button('Submit', id='textarea-state-button', n_clicks=0),
    
    html.Div(id='output-container-button', style={'whiteSpace': 'pre-line'}),
    
    html.Div(id='table-container'),
])

register_query_data_update(app)
register_histogram_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)