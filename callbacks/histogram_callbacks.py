import pandas as pd
from layouts.charts import generate_histogram_layout
from utils.query_execution import create_dataframe_from_query
from dash import Output, Input

def register_histogram_callbacks(app):
    @app.callback(
        Output('datatable-interactivity-container', 'children'),
        Input('output-container-button', 'derived_virtual_data'),
        Input('output-container-button', 'derived_virtual_selected_rows'),
        Input('textarea-state', 'value')
        )
    def update_histograms(rows, derived_virtual_selected_rows, value):
        if value is None:
            return []
        else:
            if derived_virtual_selected_rows is None:
                derived_virtual_selected_rows = []
            
        
            query_data = create_dataframe_from_query(value)
            dff = query_data if rows is None else pd.DataFrame(rows)
            
            histogram_layout = []
            for col in dff.columns:
                histogram_layout.append(generate_histogram_layout(dff, col))
            
            return histogram_layout