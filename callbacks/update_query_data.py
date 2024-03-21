from dash import html, dcc, Output, Input, State
from utils.query_execution import create_dataframe_from_query, execute_query
from layouts.table import generate_table

def create_query_data(query_text):
    return create_dataframe_from_query(query_text)

def register_query_data_update(app):
    @app.callback(
        Output('output-container-button', 'children'),
        Input('textarea-state-button', 'n_clicks'),
        State('textarea-state', 'value')
    )
    def update_query_data(n_clicks, value):
        if n_clicks > 0:
            col_names, result = execute_query(value)
            if col_names and result:
                df = create_query_data(value)
                return (
                    html.Div([
                        html.Div(f'Query Data updated successfully with: {df.shape[0]} rows and {df.shape[1]} columns', style={'textAlign': 'center'}),
                        html.Div(id='query-data', style={'display': 'none'}, children=df.to_json())
                    ]),
                    generate_table(df)
                )
            else:
                return html.Div("Error executing query"), None