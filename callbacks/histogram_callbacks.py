import pandas as pd
from layouts.charts import generate_histogram_layout
from dash import Output, Input

def register_histogram_callbacks(app, query_data):
    @app.callback(
        Output('datatable-interactivity-container', 'children'),
        Input('datatable-interactivity', 'derived_virtual_data'),
        Input('datatable-interactivity', 'derived_virtual_selected_rows'),
        )
    def update_histograms(rows, derived_virtual_selected_rows):
        if derived_virtual_selected_rows is None:
            derived_virtual_selected_rows = []
        dff = query_data if rows is None else pd.DataFrame(rows)
        
        histogram_layout = []
        for col in dff.columns:
            histogram_layout.append(generate_histogram_layout(dff, col))
        
        return histogram_layout