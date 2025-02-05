import dash
from dash import html, Input, Output, State, callback, dcc, ALL, _dash_renderer
from dash_planet import DashPlanet
from dash_iconify import DashIconify
import os
import json
import dash_mantine_components as dmc

# Set React version
_dash_renderer._set_react_version("18.3.1")

# Get API URL from environment or use default
API_URL = os.getenv("API_URL", "http://localhost:8000/api/api-keys")
API_KEY = os.getenv("API_KEY", "your-default-api-key")  # Add this line

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Enable CORS for development
app.enable_dev_tools(
    dev_tools_hot_reload=True,
    dev_tools_props_check=True,
    dev_tools_serve_dev_bundles=True,
    dev_tools_prune_errors=False,
)

styles = {
    "container": {
        "width": "100%",
        "height": "100vh",
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "center",
        "padding": "20px",
    },
    "header": {
        "textAlign": "center",
        "marginBottom": "20px",
        "width": "100%",
        "maxWidth": "600px",
    },
    "apiInput": {
        "width": "100%",
        "maxWidth": "400px",
        "padding": "8px",
        "marginBottom": "10px",
        "border": "1px solid #ccc",
        "borderRadius": "4px",
    },
    "description": {
        "fontSize": "14px",
        "color": "#666",
        "marginBottom": "20px",
        "textAlign": "center",
    },
    "demoArea": {
        "display": "flex",
        "width": "100%",
        "height": "500px",  # Fixed height for demo area
        "backgroundColor": "white",
        "justifyContent": "center",
        "alignItems": "center",
        "position": "relative",
    },
    "planet": {
        "height": "120px",
        "width": "120px",
        "borderRadius": "50%",
        "backgroundColor": "#1976d2",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "color": "white",
        "cursor": "pointer",
        "transition": "all 0.3s",
        "position": "relative",
    },
    "satellite": {
        "height": "40px",
        "width": "40px",
        # 'borderRadius': '50%',
        # 'backgroundColor': '#ff4081',
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "color": "white",
        "cursor": "pointer",
        "zIndex": 1,
    },
    "gridColumn": {
        "height": "300px",
        "width": "100%",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "position": "relative",
        "padding": "20px",
        "boxSizing": "border-box",
    },
    "features": {
        "marginTop": "20px",
        "padding": "20px",
        "backgroundColor": "#f5f5f5",
        "borderRadius": "8px",
        "maxWidth": "600px",
        "width": "100%",
    },
    "featureList": {"listStyle": "none", "padding": "0", "margin": "0"},
    "featureItem": {
        "padding": "8px 0",
        "display": "flex",
        "alignItems": "center",
        "gap": "8px",
    },
}


def generate_satellites(count):
    """Generate satellite elements with icons"""
    icons = [
        "fxemoji:email",
        "noto:calendar",
        "emojione-v1:bar-chart",
        "emojione:gear",
        "flat-color-icons:file",
        "emojione-v1:open-folder",
        "twemoji:heart-on-fire",
        "flat-color-icons:home",
    ]
    return [
        html.Div(
            [
                DashIconify(
                    icon=icons[i % len(icons)], width=40, height=40, color="white"
                )
            ],
            style=styles["satellite"],
            id={"type": "satellite", "index": i},
        )
        for i in range(count)
    ]


forms_props = dmc.GridCol(
    children=[
        dmc.Paper(
            children=[
                dmc.Stack(
                    [
                        dmc.Grid(
                            [
                                dmc.GridCol(
                                    dmc.Stack(
                                        [
                                            # Physics Controls
                                            dmc.Text(
                                                "Physics", fw=700, size="sm", c="dimmed"
                                            ),
                                            dmc.Group(
                                                [
                                                    dmc.NumberInput(
                                                        id="mass-input",
                                                        label="Mass",
                                                        value=1,
                                                        min=1,
                                                        max=10,
                                                        step=0.5,
                                                        style={"width": 100},
                                                    ),
                                                    dmc.NumberInput(
                                                        id="tension-input",
                                                        label="Tension",
                                                        value=200,
                                                        min=100,
                                                        max=1000,
                                                        step=50,
                                                        style={"width": 100},
                                                    ),
                                                    dmc.NumberInput(
                                                        id="friction-input",
                                                        label="Friction",
                                                        value=32,
                                                        min=1,
                                                        max=50,
                                                        step=1,
                                                        style={"width": 100},
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    span={"xs": 12, "md": 6},
                                ),
                                dmc.GridCol(
                                    dmc.Stack(
                                        [
                                            # Orbit Controls
                                            dmc.Text(
                                                "Orbit",
                                                fw=700,
                                                size="sm",
                                                c="dimmed",
                                                mt="md",
                                            ),
                                            dmc.Group(
                                                [
                                                    dmc.NumberInput(
                                                        id="orbit-radius-input",
                                                        label="Radius",
                                                        value=80,
                                                        min=40,
                                                        max=200,
                                                        step=10,
                                                        style={"width": 100},
                                                    ),
                                                    dmc.NumberInput(
                                                        id="rotation-input",
                                                        label="Rotation",
                                                        value=0,
                                                        min=0,
                                                        max=360,
                                                        step=15,
                                                        style={"width": 100},
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    span={"xs": 12, "md": 6},
                                ),
                            ],
                            grow=True,
                        ),
                        dmc.Grid(
                            [
                                dmc.GridCol(
                                    dmc.Stack(
                                        [
                                            dmc.Text(
                                                "Rotation Animation",
                                                fw=700,
                                                size="sm",
                                                c="dimmed",
                                                mt="md",
                                            ),
                                            dmc.Group(
                                                [
                                                    dmc.Switch(
                                                        id="animate-rotation-input",
                                                        label="Animate Rotation",
                                                        checked=False,
                                                    ),
                                                    dmc.NumberInput(
                                                        id="rotation-speed-input",
                                                        label="Speed",
                                                        value=2,
                                                        min=0.1,
                                                        max=10,
                                                        step=0.1,
                                                        style={"width": 100},
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    span={"xs": 12, "md": 6},
                                ),
                                dmc.GridCol(
                                    dmc.Stack(
                                        [
                                            # Animation Controls
                                            dmc.Text(
                                                "Animation",
                                                fw=700,
                                                size="sm",
                                                c="dimmed",
                                                mt="md",
                                            ),
                                            dmc.Group(
                                                [
                                                    dmc.Switch(
                                                        id="bounce-input",
                                                        label="Bounce",
                                                        checked=True,
                                                    ),
                                                    dmc.Switch(
                                                        id="hide-orbit-input",
                                                        label="Hide Orbit",
                                                        checked=True,
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    span={"xs": 12, "md": 6},
                                ),
                            ]
                        ),
                        dmc.Grid(
                            [
                                dmc.GridCol(
                                    # Satellite Orientation
                                    dmc.Select(
                                        id="satellite-orientation-input",
                                        label="Satellite Orientation",
                                        data=[
                                            {"value": "DEFAULT", "label": "Default"},
                                            {"value": "INSIDE", "label": "Inside"},
                                            {"value": "OUTSIDE", "label": "Outside"},
                                            {"value": "READABLE", "label": "Readable"},
                                        ],
                                        value="DEFAULT",
                                        style={"width": "100%"},
                                    ),
                                    span={"xs": 12, "md": 12},
                                )
                            ]
                        ),
                        dcc.Interval(
                            id="rotation-interval",
                            interval=50,  # 50ms = 20fps
                            disabled=True,
                        ),
                    ]
                ),
            ],
            p="md",
            shadow="sm",
            radius="md",
            withBorder=True,
            style={"maxWidth": "100%", "width": "100%"},
        )
    ],
    style={
        "height": "100%",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "position": "relative",
        "overflow": "auto",
    },
    span={"md": 4, "sm": 12},
)


# Create layout
app.layout = dmc.MantineProvider(
    [
        dmc.Stack(
            [
                html.H1("DashPlanet Demo", style={"marginBottom": "10px"}),
                html.P(
                    [
                        "Free tier includes up to 3 satellites. ",
                        "Enter an API key to unlock all features.",
                    ],
                    style=styles["description"],
                ),
                dmc.Center(
                    dmc.Anchor(href='https://pipinstallpython.pythonanywhere.com/catalogue/dash-planet_95/', children='Buy a DashPlanet API', target='_blank', size='lg', c='blue')
                ),
                dmc.Group(
                    [
                        dcc.Input(
                            id="api-key-input",
                            type="text",
                            placeholder="Enter your API key to check if it works",
                            value="",
                            style=styles["apiInput"],
                        ),
                        dmc.Switch(
                            id="use-env-api-key",
                            label="Use Environment API Key",
                            checked=False,
                        ),
                    ],
                    justify="center",
                ),
                html.Div(
                    id="api-key-status", style={"color": "#666", "marginBottom": "10px"}
                ),
                # Hidden API URL input
                dcc.Input(
                    id="api-url-input",
                    type="text",
                    value=f"{API_URL}/validate",
                    style={"display": "none"},
                ),
            ],
            justify="center",
            align="center",
            gap="md",
        ),
        dmc.Space(h=20),
        dmc.Text("Props Control Panel", size="xl", fw=700, ta="center"),
        dmc.Grid(
            children=[
                forms_props,
                dmc.GridCol(
                    dmc.Stack(
                        [
                            DashPlanet(
                                id="demo-planet",
                                centerContent=dmc.Indicator(
                                    dmc.Avatar(
                                        size="lg",
                                        radius="xl",
                                        src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-3.png",
                                    ),
                                    inline=True,
                                    offset=7,
                                    position="bottom-end",
                                    color="red",
                                    withBorder=True,
                                    size=16,
                                ),
                                open=True,
                                orbitRadius=80,
                                hideOrbit=True,
                                bounce=True,
                                bounceOnOpen=True,
                                rotation=0,
                                dragablePlanet=True,
                                dragableSatellites=True,
                                satelliteOrientation="DEFAULT",
                                children=generate_satellites(8),
                                mass=4,
                                tension=500,
                                friction=19,
                                apiKey="",
                            ),
                            html.Div(
                                [
                                    # API validation status
                                    html.Div(id="validation-status"),
                                    dmc.Text(
                                        "Click a satellite to see its function",
                                        id="action-text",
                                        ta="center",
                                        mt="120px",
                                    ),
                                ]
                            ),
                        ],
                        mt="100px",
                    ),
                    span={"md": 4, "sm": 12},
                    style=styles["gridColumn"],
                ),
                dmc.GridCol(
                    html.Div(
                        [
                            html.H2("Features", style={"marginBottom": "15px"}),
                            html.Ul(
                                [
                                    html.Li(
                                        [
                                            DashIconify(
                                                icon="mdi:check", color="#4CAF50"
                                            ),
                                            "Free Tier: Up to 3 satellites",
                                        ],
                                        style=styles["featureItem"],
                                    ),
                                    html.Li(
                                        [
                                            DashIconify(
                                                icon="mdi:star", color="#FFC107"
                                            ),
                                            "Premium: Unlimited satellites",
                                        ],
                                        style=styles["featureItem"],
                                    ),
                                    html.Li(
                                        [
                                            DashIconify(
                                                icon="mdi:gesture", color="#2196F3"
                                            ),
                                            "Semicircle Menu layout",
                                        ],
                                        style=styles["featureItem"],
                                    ),
                                    html.Li(
                                        [
                                            DashIconify(
                                                icon="mdi:animation", color="#9C27B0"
                                            ),
                                            "Enhanced animation controls",
                                        ],
                                        style=styles["featureItem"],
                                    ),
                                    html.Li(
                                        [
                                            DashIconify(
                                                icon="fluent-emoji:sparkling-heart", color="#9C27B0"
                                            ),
                                            "Supports independent Dash Components development",
                                        ],
                                        style=styles["featureItem"],
                                    ),
                                ],
                                style=styles["featureList"],
                            ),
                        ],
                        style=styles["features"],
                    ),
                    style={
                        "height": "300px",
                        "display": "flex",
                        "justifyContent": "center",
                        "alignItems": "center",
                        "position": "relative",
                    },
                    span={"md": 4, "sm": 12},
                ),
            ],
            gutter="xl",
        ),
    ]
)


# Update callbacks
@callback(
    [
        Output("demo-planet", "apiKey"),
        Output("api-key-input", "disabled"),
        Output("api-key-status", "children"),
        Output("api-key-status", "style"),
    ],
    [
        Input("api-key-input", "value"),
        Input("api-url-input", "value"),
        Input("use-env-api-key", "checked")
    ],
    prevent_initial_call=True,
)
def update_api_key(api_key, api_url, use_env_key):
    """Update API key based on input or environment variable"""
    if use_env_key:
        return API_KEY, True, "DEMO with API Key", {"color": "#4CAF50"}

    if not api_key:
        return None, False, "Using free tier", {"color": "#666"}

    return api_key, False, f"Using API key: {api_key[:8]}...", {"color": "#4CAF50"}


@callback(
    Output("demo-planet", "open"),
    Input("demo-planet", "n_clicks"),
    prevent_initial_call=True,
)
def toggle_planet(n_clicks):
    """Toggle planet open/closed state"""
    if n_clicks is None:
        return dash.no_update
    return n_clicks % 2 == 1


# Add this callback to handle satellite clicks
@callback(
    Output("action-text", "children"),
    Input({"type": "satellite", "index": ALL}, "n_clicks"),
    prevent_initial_call=True,
)
def handle_satellite_click(clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "Click a satellite to see its function"

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]
    satellite_index = json.loads(triggered_id)["index"]

    # Map indices to actions
    actions = [
        "Compose new email",
        "Open calendar",
        "View analytics",
        "Open settings",
        "New document",
        "Browse files",
        "Favorite item",
        "Return home",
    ]

    return f"Selected: {actions[satellite_index % len(actions)]}"


# Add these callbacks after your existing callbacks:
@callback(
    Output("demo-planet", "mass"),
    Input("mass-input", "value"),
    prevent_initial_call=True,
)
def update_mass(value):
    return value


@callback(
    Output("demo-planet", "tension"),
    Input("tension-input", "value"),
    prevent_initial_call=True,
)
def update_tension(value):
    return value


@callback(
    Output("demo-planet", "friction"),
    Input("friction-input", "value"),
    prevent_initial_call=True,
)
def update_friction(value):
    return value


@callback(
    Output("demo-planet", "orbitRadius"),
    Input("orbit-radius-input", "value"),
    prevent_initial_call=True,
)
def update_orbit_radius(value):
    return value


@callback(
    Output("demo-planet", "rotation"),
    Input("rotation-input", "value"),
    prevent_initial_call=True,
)
def update_rotation(value):
    return value


@callback(
    Output("demo-planet", "bounce"),
    Input("bounce-input", "checked"),
    prevent_initial_call=True,
)
def update_bounce(checked):
    return checked


@callback(
    Output("demo-planet", "hideOrbit"),
    Input("hide-orbit-input", "checked"),
    prevent_initial_call=True,
)
def update_hide_orbit(checked):
    return checked


@callback(
    Output("demo-planet", "satelliteOrientation"),
    Input("satellite-orientation-input", "value"),
    prevent_initial_call=True,
)
def update_satellite_orientation(value):
    return value


@callback(
    [Output("rotation-interval", "disabled"), Output("rotation-input", "disabled")],
    Input("animate-rotation-input", "checked"),
)
def toggle_animation(animate):
    return not animate, animate


# Callback to update rotation based on the interval
@callback(
    Output("demo-planet", "rotation", allow_duplicate=True),
    [Input("rotation-interval", "n_intervals"), Input("rotation-speed-input", "value")],
    State("demo-planet", "rotation"),
    prevent_initial_call=True,
)
def update_rotation(n_intervals, speed, current_rotation):
    if current_rotation is None:
        current_rotation = 0
    # Calculate new rotation angle
    new_rotation = (current_rotation + speed) % 360
    return new_rotation


# Callback to handle manual rotation input
@callback(
    Output("rotation-input", "disabled", allow_duplicate=True),
    Input("animate-rotation-input", "checked"),
    prevent_initial_call=True,
)
def toggle_rotation_input(animate):
    return animate


# Add custom CSS for hover effects
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>DashPlanet Demo - Free and Premium Features</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                background-color: #fafafa;
            }
            .planet:hover {
                box-shadow: 0px 0px 15px 10px rgba(103, 58, 183, 0.3) !important;
            }
            .satellite:hover {
                transform: scale(1.1);
                box-shadow: 0px 0px 10px 5px rgba(255, 64, 129, 0.3) !important;
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
"""

if __name__ == "__main__":
    app.run_server(debug=True, port=8359)
