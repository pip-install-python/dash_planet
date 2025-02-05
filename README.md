# Dash Planet 🪐

DashPlanet is an interactive orbital menu component for Dash applications that displays content in a circular orbit around a central element. It provides an engaging and intuitive way to present navigation options or related content items.

Check out the docs for demos and examples: [DashPlanet Docs](https://pip-install-python.com/pip/dash_planet)

### Features

| **Free Tier**                         | **Premium Features** |
|:-----------------------------------------|:----------------|
| ✓ Up to 3 satellite elements in orbit    | 🌟 Unlimited satellite elements |
| ✓ Basic orbital animation                | 🌙 Semicircle Menu layout |
| ✓ Customizable orbit radius and rotation | ⚡ Enhanced animation controls |
| ✓ Click-to-toggle functionality          | 💎 Supports independent Dash Components development |

Buy a DashPlanet API Key: [here](https://pipinstallpython.pythonanywhere.com/catalogue/dash-planet_95/)

### Installation

```bash
pip install dash-planet
```

### Quick Start

```python
from dash import Dash
from dash_planet import DashPlanet
import dash_mantine_components as dmc
from dash_iconify import DashIconify

app = Dash(__name__)

app.layout = DashPlanet(
    id='my-planet',
    centerContent=dmc.Avatar(
        size="lg",
        radius="xl",
        src="path/to/avatar.png"
    ),
    children=[
        # Your satellite elements here...
        
        # Example satellite element
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line", width=20, height=20),
            size="lg",
            variant="filled",
            id="action-icon",
            n_clicks=0,
            mb=10,
        ),
    ],
    orbitRadius=80,
    rotation=0,
    apiKey="your-api-key-here"
)

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Props

### Core Props

| Prop            | Type    | Default | Description                                  |
|-----------------|---------|---------|----------------------------------------------|
| `id`            | string  | None    | Component identifier for Dash callbacks      |
| `centerContent` | node    | None    | Content displayed in the center of the orbit |
| `children`      | node    | None    | Satellite elements to be displayed in orbit  |
| `open`          | boolean | False   | Controls visibility of satellites            |
| `orbitRadius`   | number  | 120     | Radius of the orbit in pixels                |
| `rotation`      | number  | 0       | Initial rotation angle in degrees            |
| `hideOrbit`     | boolean | False   | Toggle orbit line visibility                 |

### Animation Props

| Prop       | Type   | Default | Description             |
|------------|--------|---------|-------------------------|
| `mass`     | number | 1       | Mass for spring physics |
| `tension`  | number | 500     | Spring tension          |
| `friction` | number | 17      | Spring friction         |

### Premium Props (Requires API Key)

| Prop                   | Type    | Default   | Description                                                                 |
|------------------------|---------|-----------|-----------------------------------------------------------------------------|
| `apiKey`               | string  | None      | API key for premium features                                                |
| `dragablePlanet`       | boolean | False     | Enable center content dragging                                              |
| `dragableSatellites`   | boolean | False     | Enable satellite dragging                                                   |
| `bounce`               | boolean | False     | Enable bounce animation                                                     |
| `bounceDirection`      | enum    | 'TOP'     | Bounce animation direction ('TOP' \| 'BOTTOM' \| 'LEFT' \| 'RIGHT')         |
| `satelliteOrientation` | enum    | 'DEFAULT' | Satellite rotation style ('DEFAULT' \| 'INSIDE' \| 'OUTSIDE' \| 'READABLE') |

### Callbacks

#### Basic Toggle Example
```python
from dash import Input, Output, callback

@callback(
    Output("my-planet", "open"),
    Input("my-planet", "n_clicks")
)
def toggle_planet(n_clicks):
    if n_clicks is None:
        return False
    return n_clicks % 2 == 1
```

#### Dynamic Rotation Example
```python
@callback(
    Output("my-planet", "rotation"),
    Input("rotation-input", "value")
)
def update_rotation(value):
    return value
```

#### Satellite Elements

Satellites can be any valid Dash component. Here's an example using icons:

```python
from dash_iconify import DashIconify

satellites = [
    html.Div([
        DashIconify(
            icon="mdi:email",
            width=40,
            height=40,
            color="white"
        )
    ], style={'width': '40px', 'height': '40px'})
    for _ in range(3)
]
```

#### Advanced Animation Control

The component supports spring physics-based animations with customizable parameters:

```python
DashPlanet(
    mass=4,           # Controls animation weight
    tension=500,      # Controls spring stiffness
    friction=19,      # Controls damping
)
```

#### Styling

The component accepts standard Dash styling through the `style` prop and CSS classes. Example:

```python
DashPlanet(
    style={
        'backgroundColor': 'white',
        'borderRadius': '50%',
        'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
    }
)
```

### API Key Validation
To use premium features, provide a valid API key:


```python
DashPlanet(
    apiKey="your-api-key-here",
)
```

### Browser Support
DashPlanet is compatible with modern browsers that support CSS transforms and React Spring animations:

Chrome (latest)
Firefox (latest)
Safari (latest)
Edge (latest)

### Dependencies

dash ≥ 2.0.0
react ≥ 18.3.1
