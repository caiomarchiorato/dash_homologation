from dash import dash_table
from utils.query_execution import create_dataframe_from_query

def create_table():
    query_data = create_dataframe_from_query('data/queries/')
    
    tableColors = {
        'header': 'rgb(48, 102, 175)',
        'header_font': 'white'
    }

    layout = dash_table.DataTable(
        data=query_data.to_dict('records'),
        columns=[{'id': i, 'name': i} for i in query_data.columns],
        style_header={
            'backgroundColor': tableColors['header'],
            'fontWeight': 'bold',
            'color': tableColors['header_font']
        },
        page_size=5
    )
    
    return layout