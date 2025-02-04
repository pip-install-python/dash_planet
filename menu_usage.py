import dash
from dash import html, Input, Output, callback, State
from dash_planet import DashPlanet
from dash_iconify import DashIconify

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
        'flexDirection': 'column',
        'minHeight': '600px',
        'position': 'relative',
        'gap': '20px'
    },
    'paperButton': {
        'padding': '8px',
        'borderRadius': '50%',
        'cursor': 'pointer',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'boxShadow': '0px 2px 4px -1px rgba(0,0,0,0.2), 0px 4px 5px 0px rgba(0,0,0,0.14), 0px 1px 10px 0px rgba(0,0,0,0.12)',
        'transition': 'box-shadow 0.3s ease-in-out',
        'width': '40px',
        'height': '40px',
    },
    'mainButton': {
        'backgroundColor': '#4da37c',
        'color': 'white',
    },
    'subButton': {
        'backgroundColor': 'white',
        'color': '#424242',
    },
    'text': {
        'fontSize': '18px',
        'color': '#424242',
        'fontFamily': 'Arial, sans-serif',
        'margin': '20px 0',
        'marginLeft': '58px',
    }
}


def create_paper_button(icon_name, is_main=False, id=None, href=None):
    """Create a paper button with icon"""
    button_style = {
        **styles['paperButton'],
        **(styles['mainButton'] if is_main else styles['subButton'])
    }

    button_content = DashIconify(
        icon=icon_name,
        width=24,
        height=24,
        color=button_style['color']
    )

    # Create div props excluding id if it's None
    div_props = {
        'children': button_content,
        'style': button_style,
        'className': 'paper-button'
    }
    if id:
        div_props['id'] = id

    if href:
        # Wrap in an anchor tag if href is provided
        return html.A(
            html.Div(**div_props),
            href=href,
            target="_blank",  # Open in new tab
            style={'textDecoration': 'none'}
        )
    else:
        return html.Div(**div_props)


# Create the menu structure
app.layout = html.Div([
    html.Div([
        # Planet Menu
        DashPlanet(
            id='menu-planet',
            centerContent=create_paper_button("ic:baseline-menu", True),
            hideOrbit=True,
            autoClose=True,
            orbitRadius=60,
            bounce=True,
            bounceOnClose=True,
            children=[
                create_paper_button(
                    "ic:outline-info",
                    id='info-button',

                ),
                create_paper_button(
                    "ic:baseline-edit",
                    id='edit-button',

                ),
                create_paper_button(
                    "ic:baseline-delete",
                    id='delete-button',

                ),
            ]
        ),
        html.Br(),
        html.Br(),
        # Text display area
        html.Center(html.Div(
            "Click a button to see what it does!",
            id='action-text',
            style=styles['text']
        ))
    ], style=styles['root'])
], style={'width': '100%', 'height': '100vh'})


# Add callbacks to update the text
@callback(
    Output('action-text', 'children'),
    [Input('info-button', 'n_clicks'),
     Input('edit-button', 'n_clicks'),
     Input('delete-button', 'n_clicks')],
    prevent_initial_call=True
)
def update_text(info_clicks, edit_clicks, delete_clicks):
    # Get the ID of the button that was clicked
    ctx = dash.callback_context
    if not ctx.triggered:
        return "Click a button to see what it does!"

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'info-button':
        return "Opening documentation..."
    elif button_id == 'edit-button':
        return "Opening editor..."
    elif button_id == 'delete-button':
        return "Opening delete confirmation..."

    return "Click a button to see what it does!"


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
            .paper-button:hover {
                box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2), 
                           0px 8px 10px 1px rgba(0,0,0,0.14), 
                           0px 3px 14px 2px rgba(0,0,0,0.12) !important;
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
    app.run_server(debug=True, port='8222')