from dash import html
from config.default_styles import DEFAULT_COLOR_PRIMARY, DEFAULT_COLOR_SECONDARY, DEFAULT_FONT_FAMILY

def generate_header(img):
    header_container_style = {
        'display': 'flex',          
        'alignItems': 'center',     
        'justifyContent': 'space-between', 
        'backgroundColor': DEFAULT_COLOR_SECONDARY, 
        'padingLeft': '0px',
        'paddingRight': '0px',
        'paddingTop': '0px',
        'paddingBottom': '20px',
        'boxShadow': '0px 4px 4px -2px rgba(0, 0, 0, 0.1)',
        'width': '100%',
    }
    
    title_style = {
        'textAlign': 'center', 
        'margin': '0', 
        'flexGrow': '1',
        'color': DEFAULT_COLOR_PRIMARY,
        'fontFamily': DEFAULT_FONT_FAMILY
    }
    
    image_style = {'height': '80px', 'width': 'auto'}
    
    header = html.Div(
        children=[
            html.Img(id="nuvem-logo", src=img, style=image_style),
            html.H1('', style=title_style),
        ],
        style=header_container_style
    )
    return header