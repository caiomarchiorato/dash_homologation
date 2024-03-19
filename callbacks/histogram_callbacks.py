from dash import Output, Input
from utils.data_processing import create_histogram

def register_histogram_callbacks(app, query_data):
    @app.callback(
        Output('histogram', 'figure'),
        [Input('column-dropdown', 'value')])
    def update_histograms(selected_columns):
        if selected_columns:
            fig = create_histogram(query_data, selected_columns)
            print(f'Coluna selecionada {selected_columns}')
            return fig
        else:
            print('No column selected')
            return {'data': [], 'layout': {}}