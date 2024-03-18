from dash import Dash, html, dash_table
import plotly.express as px
import pandas as pd

#custom
from utils.data_processing import generate_table
from utils.query_execution import create_dataframe_from_query

tableColors = {
    'header': 'rgb(48, 102, 175)',
    'header_font': 'white'
}

app = Dash(__name__)

query_data = create_dataframe_from_query('data/queries/')

app.layout = dash_table.DataTable(query_data.to_dict('records'),
    columns=[{'id': i, 'name': i} for i in query_data.columns],
    style_header={'backgroundColor': tableColors['header'],
                'fontWeight': 'bold',
                'color': tableColors['header_font']},
    page_size = 5
)



if __name__ == '__main__':
    app.run_server(debug=True)