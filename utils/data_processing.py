import plotly.express as px

def create_histogram(data, column):
    fig = px.histogram(data, x=column)
    print(fig)
    return fig