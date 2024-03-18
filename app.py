from dash import Dash, html, dash_table
import plotly.express as px
import pandas as pd
#custom
from layouts.table import create_table
from utils.query_execution import create_dataframe_from_query


#instanciando o app
app = Dash(__name__)
app.layout = create_table()

if __name__ == '__main__':
    app.run_server(debug=True)