from dash import html, dcc
from utils.data_processing import create_histogram

def generate_histogram_layout(query_data, selected_column):
        fig = create_histogram(query_data, selected_column)
        histogram_div = html.Div(id='histogram-container', children=[
                                        dcc.Graph(id='histogram', figure= fig),
                                                                ],
                        style={'width': '50%', 'display': 'inline-block'})
        return histogram_div