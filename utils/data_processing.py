import plotly.express as px

def create_histogram(data, column: None):
    fig = px.histogram(data, x=column)
    return fig