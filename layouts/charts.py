from dash import html, dcc
from utils.data_processing import create_histogram

def generate_histogram_layout(query_data, selected_column):
    fig = create_histogram(query_data, selected_column)
    histogram_div = html.Div(id='histogram-container', children=[
            html.H1('Histogram'),
            dcc.Graph(id='histogram', figure= fig)])
    return histogram_div