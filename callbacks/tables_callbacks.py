from dash import Output, Input, State, dcc
from utils.query_execution import create_dataframe_from_query

def register_table_callbacks(app):
    @app.callback(
        Output('table-container', 'children'),
        [Input('button-executar-queries', 'n_clicks')],
        [State('input-queries', 'value')])
    def execute_query_and_update_table(n_clicks, query):
        if n_clicks > 0:
            df = create_dataframe_from_query(query)
            col_names = df.columns.tolist()
            return [
                dcc.Dropdown(
                    id='column-dropdown',
                    options=[{'label': col, 'value': col} for col in col_names],
                    placeholder='Select a coluna'
                )
            ]
        else:
            return "Nenhuma consulta foi executada ainda."
