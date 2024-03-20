from dash import Dash, html, dcc, dash_table
from PIL import Image
#custom
from components.header import generate_header
from callbacks.histogram_callbacks import register_histogram_callbacks
from utils.query_execution import create_dataframe_from_query

query_data = create_dataframe_from_query('data/queries/')
col_name = query_data.columns

#instanciando o app
app = Dash(__name__)

print(col_name)
pil_img = Image.open('components/assets/logo.png')

app.layout = html.Div(children=[
    
    # html.Div([
    #     dcc.Input(id="input-queries", type="text", placeholder="Digite a query"),
    #     html.Button("Executar queries", id="button-executar-queries", n_clicks=0),
    # ]),
    
    generate_header(pil_img),
    html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "selectable": True} for i in query_data.columns
        ],
        data=query_data.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-interactivity-container')
    ]),

    # html.Div([generate_histogram_layout(query_data, col) for col in col_name]
    # ),
])

register_histogram_callbacks(app, query_data)

if __name__ == '__main__':
    app.run_server(debug=True)