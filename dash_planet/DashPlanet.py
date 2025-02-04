# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashPlanet(Component):
    """A DashPlanet component.
DashPlanet is an interactive orbit menu component that displays children in a circular orbit.
Free tier limitations apply unless a valid API key is provided.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The satellite items that orbit around the center. These can be any
    valid React nodes. Free tier limits apply unless a valid API key
    is provided.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- apiKey (string; optional):
    API key for unlocking full functionality. Without a valid key, the
    component will operate in free tier mode with limited features.

- autoClose (boolean; optional):
    Whether to automatically close when clicking outside. When True,
    the menu closes when clicking anywhere outside the component.

- bounce (boolean; optional):
    Whether to bounce on both open and close. When True, applies
    bounce animation in the specified bounceDirection. Requires valid
    API key.

- bounceDirection (a value equal to: 'TOP', 'BOTTOM', 'LEFT', 'RIGHT'; optional):
    Direction of the bounce animation. Determines which direction the
    bounce effect is applied.

- bounceOnClose (boolean; optional):
    Whether to bounce only on close. When True, applies bounce
    animation only when closing the menu. Requires valid API key.

- bounceOnOpen (boolean; optional):
    Whether to bounce only on open. When True, applies bounce
    animation only when opening the menu. Requires valid API key.

- centerContent (a list of or a singular dash component, string or number; optional):
    The center content of the planet menu. This can be any valid React
    node.

- dragRadiusPlanet (number; optional):
    Maximum drag radius for the planet in pixels. Controls how far the
    center content can be dragged when dragablePlanet is True.

- dragRadiusSatellites (number; optional):
    Maximum drag radius for satellites in pixels. Controls how far
    satellite items can be dragged when dragableSatellites is True.

- dragablePlanet (boolean; optional):
    Whether the planet can be dragged. When True, the center content
    can be dragged within the dragRadiusPlanet limit. Requires valid
    API key.

- dragableSatellites (boolean; optional):
    Whether satellites can be dragged. When True, satellite items can
    be dragged within the dragRadiusSatellites limit. Requires valid
    API key.

- friction (number; optional):
    Friction for spring physics animations. Controls the spring
    damping.

- hideOrbit (boolean; optional):
    Whether to hide the orbit line. When True, the circular orbit path
    is not visible.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.

- mass (number; optional):
    Mass for spring physics animations. Controls the weight/inertia of
    animations.

- n_clicks (number; optional):
    Number of times the planet has been clicked. This value is updated
    automatically when the planet is clicked.

- open (boolean; optional):
    Whether the planet menu is open. Controls the visibility of
    satellite items.

- orbitRadius (number; optional):
    Radius of the orbit in pixels. Controls how far the satellites are
    from the center.

- rotation (number; optional):
    Rotation angle in degrees. Controls the starting position of
    satellites.

- satelliteOrientation (a value equal to: 'DEFAULT', 'INSIDE', 'OUTSIDE', 'READABLE'; optional):
    Orientation of the satellites. Controls how satellite items are
    rotated in their orbit.

- tension (number; optional):
    Tension for spring physics animations. Controls the spring
    stiffness."""
    _children_props = ['centerContent']
    _base_nodes = ['centerContent', 'children']
    _namespace = 'dash_planet'
    _type = 'DashPlanet'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, centerContent=Component.UNDEFINED, n_clicks=Component.UNDEFINED, open=Component.UNDEFINED, orbitRadius=Component.UNDEFINED, rotation=Component.UNDEFINED, hideOrbit=Component.UNDEFINED, autoClose=Component.UNDEFINED, dragablePlanet=Component.UNDEFINED, dragRadiusPlanet=Component.UNDEFINED, dragableSatellites=Component.UNDEFINED, dragRadiusSatellites=Component.UNDEFINED, bounce=Component.UNDEFINED, bounceOnOpen=Component.UNDEFINED, bounceOnClose=Component.UNDEFINED, bounceDirection=Component.UNDEFINED, satelliteOrientation=Component.UNDEFINED, mass=Component.UNDEFINED, tension=Component.UNDEFINED, friction=Component.UNDEFINED, apiKey=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'apiKey', 'autoClose', 'bounce', 'bounceDirection', 'bounceOnClose', 'bounceOnOpen', 'centerContent', 'dragRadiusPlanet', 'dragRadiusSatellites', 'dragablePlanet', 'dragableSatellites', 'friction', 'hideOrbit', 'loading_state', 'mass', 'n_clicks', 'open', 'orbitRadius', 'rotation', 'satelliteOrientation', 'tension']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'apiKey', 'autoClose', 'bounce', 'bounceDirection', 'bounceOnClose', 'bounceOnOpen', 'centerContent', 'dragRadiusPlanet', 'dragRadiusSatellites', 'dragablePlanet', 'dragableSatellites', 'friction', 'hideOrbit', 'loading_state', 'mass', 'n_clicks', 'open', 'orbitRadius', 'rotation', 'satelliteOrientation', 'tension']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DashPlanet, self).__init__(children=children, **args)
