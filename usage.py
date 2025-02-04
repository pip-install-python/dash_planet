import dash
from dash import html, Input, Output, callback
from dash_planet import DashPlanet

app = dash.Dash(__name__)

# Define styles to mimic the Material-UI styling
styles = {
    'root': {
        'display': 'flex',
        'flex': '1',
        'width': '100%',
        'backgroundColor': 'white',
        'justifyContent': 'center',
        'alignItems': 'center',
        'minHeight': '600px',
        'position': 'relative'
    },
    'planet': {
        'height': '100px',
        'width': '100px',
        'borderRadius': '50%',
        'backgroundColor': '#1976d2',  # Material-UI primary color
        'transition': 'all 0.3s',
        'cursor': 'pointer',
        'position': 'relative',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center'
    },
    'planetception': {
        'height': '30px',
        'width': '30px',
        'backgroundColor': '#9c27b0',  # Material-UI secondary color
        'borderRadius': '50%',
        'transition': 'all 0.3s',
        'cursor': 'pointer',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'position': 'relative',
        'zIndex': 2
    },
    'satellite': {
        'height': '20px',
        'width': '20px',
        'borderRadius': '50%',
        'backgroundColor': '#ff4081',  # Material-UI secondary color
        'cursor': 'pointer',
        'position': 'relative',
        'zIndex': 1
    }
}

def generate_satellites(count):
    """Generate satellite elements"""
    return [
        html.Div(style=styles['satellite'])
        for _ in range(count)
    ]

# Create the nested planets structure
app.layout = html.Div([
    html.Div([
        DashPlanet(
            id='main-planet',
            centerContent=html.Img(src='https://www.icegif.com/wp-content/uploads/2023/10/icegif-588.gif', style={'width': '150px'}),
            open=False,  # Set initial state to closed
            orbitRadius=220,
            bounce=True,
            bounceOnOpen=True,
            rotation=30,
            children=[
                # First nested planet
                DashPlanet(
                    id='planet-1',
                    centerContent=html.Img(src='https://brianin3d.wordpress.com/wp-content/uploads/2012/01/just_earth_800.gif?w=584', style={'width': '25px'}, className='planetception'),
                    autoClose=True,
                    orbitRadius=60,
                    bounce=True,
                    bounceOnOpen=True,
                    satelliteOrientation='OUTSIDE',
                    open=False,
                    children=generate_satellites(3)
                ),
                # Second nested planet
                DashPlanet(
                    id='planet-2',
                    centerContent=html.Div(style=styles['planetception'], className='planetception'),
                    autoClose=True,
                    orbitRadius=60,
                    bounce=True,
                    bounceOnOpen=True,
                    satelliteOrientation='OUTSIDE',
                    open=False,
                    children=generate_satellites(3)
                ),
                # Third nested planet
                DashPlanet(
                    id='planet-3',
                    centerContent=html.Div(style=styles['planetception'], className='planetception'),
                    autoClose=True,
                    orbitRadius=60,
                    bounce=True,
                    bounceOnOpen=True,
                    satelliteOrientation='OUTSIDE',
                    open=False,
                    children=generate_satellites(3)
                ),
            ]
        )
    ], style=styles['root'])
], style={'width': '100%', 'height': '100vh'})

# Add callbacks to manage state
@callback(
    Output('main-planet', 'open'),
    Input('main-planet', 'n_clicks'),
    prevent_initial_call=True
)
def toggle_main_planet(n_clicks):
    if n_clicks is None:
        return False
    return True

# Add custom CSS for hover effects
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .planet:hover {
                box-shadow: 0px 0px 15px 10px rgba(103, 58, 183, 0.3) !important;
            }
            .planetception:hover {
                box-shadow: 0px 0px 15px 10px rgba(103, 58, 183, 0.3) !important;
            }
            body {
                margin: 0;
                padding: 0;
                overflow: hidden;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run_server(debug=True, port='8622')