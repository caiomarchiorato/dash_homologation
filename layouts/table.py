from dash import dash_table, html
from utils.query_execution import create_dataframe_from_query
from config.default_styles import DEFAULT_COLOR_PRIMARY, DEFAULT_COLOR_SECONDARY, DEFAULT_FONT_FAMILY

def generate_table(query_data=None):
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
            }

    layout =  html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "selectable": True} for i in query_data.columns
        ],
        data=query_data.to_dict('records'),
        style_table=styleTable,
        style_cell=styleCell,
        style_header=styleHeader,
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-interactivity-container')
    ])
    
    return layout