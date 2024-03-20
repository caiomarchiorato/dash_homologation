from dash import dash_table, html
from utils.query_execution import create_dataframe_from_query
from config.default_styles import DEFAULT_COLOR_PRIMARY, DEFAULT_COLOR_SECONDARY, DEFAULT_FONT_FAMILY

def create_table(query_data=None):
    if query_data is None:
        data = create_dataframe_from_query('data/queries/')

    styleTable = {
                'maxWidth': '80%',
                'margin': 'auto',  
                'backgroundColor': DEFAULT_COLOR_SECONDARY,
                'fontFamily': DEFAULT_FONT_FAMILY
            }
    
    styleCell = {
                "padding": "15px",
                "midWidth": "0px",
                "width": "25%",
                "textAlign": "center",
                "border": "white",
            }
    
    styleHeader = {
                "backgroundColor": DEFAULT_COLOR_PRIMARY,
                "fontWeight": "bold",
                "color": DEFAULT_COLOR_SECONDARY,
                "fontFamily": DEFAULT_FONT_FAMILY,
            }

    layout = html.Div([
        dash_table.DataTable(
            id='table',
            sort_action = 'native',
            filter_action = 'native',
            data=data.to_dict('records'),
            columns=[{'id': i, 'name': i} for i in data.columns],
            style_table= styleTable,
            style_data={"whiteSpace": "normal"},
            style_cell= styleCell,
            style_header=styleHeader,
            page_size=10
        )
    ])
    
    return layout