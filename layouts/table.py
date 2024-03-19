from dash import dash_table, html
from utils.query_execution import create_dataframe_from_query

def create_table(query_data=None):
    if query_data is None:
        query_data = create_dataframe_from_query('data/queries/')
    
    tableColors = {
        'header': 'rgb(48, 102, 175)',
        'header_font': 'white'
    }

    layout = html.Div([
        html.Button("Executar Consultas", id="execute-query-button", n_clicks=0),
        dash_table.DataTable(
            id='table',
            data=query_data.to_dict('records'),
            columns=[{'id': i, 'name': i} for i in query_data.columns],
            style_table={
                'maxWidth': '80%',
                'margin': 'auto',  
                'backgroundColor': '#f9f9f9'
            },
            style_data={"whiteSpace": "normal"},
            style_cell={
                "padding": "15px",
                "midWidth": "0px",
                "width": "25%",
                "textAlign": "center",
                "border": "white",
            },
            style_header={
                "backgroundColor": tableColors['header'],
                "fontWeight": "bold",
                "color": tableColors['header_font'],
            },
            page_size=5
        )
    ])
    
    return layout