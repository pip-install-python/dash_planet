# AUTO GENERATED FILE - DO NOT EDIT

export dashplanet

"""
    dashplanet(;kwargs...)
    dashplanet(children::Any;kwargs...)
    dashplanet(children_maker::Function;kwargs...)


A DashPlanet component.
DashPlanet is an interactive orbit menu component that displays children in a circular orbit.
Free tier limitations apply unless a valid API key is provided.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The satellite items that orbit around the center. These can be any valid React nodes.
Free tier limits apply unless a valid API key is provided.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `apiKey` (String; optional): API key for unlocking full functionality. Without a valid key, the component
will operate in free tier mode with limited features.
- `autoClose` (Bool; optional): Whether to automatically close when clicking outside. When true, the menu closes
when clicking anywhere outside the component.
- `bounce` (Bool; optional): Whether to bounce on both open and close. When true, applies bounce animation
in the specified bounceDirection. Requires valid API key.
- `bounceDirection` (a value equal to: 'TOP', 'BOTTOM', 'LEFT', 'RIGHT'; optional): Direction of the bounce animation. Determines which direction the bounce effect
is applied.
- `bounceOnClose` (Bool; optional): Whether to bounce only on close. When true, applies bounce animation only when
closing the menu. Requires valid API key.
- `bounceOnOpen` (Bool; optional): Whether to bounce only on open. When true, applies bounce animation only when
opening the menu. Requires valid API key.
- `centerContent` (a list of or a singular dash component, string or number; optional): The center content of the planet menu. This can be any valid React node.
- `dragRadiusPlanet` (Real; optional): Maximum drag radius for the planet in pixels. Controls how far the center content
can be dragged when dragablePlanet is true.
- `dragRadiusSatellites` (Real; optional): Maximum drag radius for satellites in pixels. Controls how far satellite items
can be dragged when dragableSatellites is true.
- `dragablePlanet` (Bool; optional): Whether the planet can be dragged. When true, the center content can be dragged
within the dragRadiusPlanet limit. Requires valid API key.
- `dragableSatellites` (Bool; optional): Whether satellites can be dragged. When true, satellite items can be dragged
within the dragRadiusSatellites limit. Requires valid API key.
- `friction` (Real; optional): Friction for spring physics animations. Controls the spring damping.
- `hideOrbit` (Bool; optional): Whether to hide the orbit line. When true, the circular orbit path is not visible.
- `loading_state` (optional): Object that holds the loading state object coming from dash-renderer.. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `mass` (Real; optional): Mass for spring physics animations. Controls the weight/inertia of animations.
- `n_clicks` (Real; optional): Number of times the planet has been clicked. This value is updated automatically
when the planet is clicked.
- `open` (Bool; optional): Whether the planet menu is open. Controls the visibility of satellite items.
- `orbitRadius` (Real; optional): Radius of the orbit in pixels. Controls how far the satellites are from the center.
- `rotation` (Real; optional): Rotation angle in degrees. Controls the starting position of satellites.
- `satelliteOrientation` (a value equal to: 'DEFAULT', 'INSIDE', 'OUTSIDE', 'READABLE'; optional): Orientation of the satellites. Controls how satellite items are rotated in their orbit.
- `tension` (Real; optional): Tension for spring physics animations. Controls the spring stiffness.
"""
function dashplanet(; kwargs...)
        available_props = Symbol[:children, :id, :apiKey, :autoClose, :bounce, :bounceDirection, :bounceOnClose, :bounceOnOpen, :centerContent, :dragRadiusPlanet, :dragRadiusSatellites, :dragablePlanet, :dragableSatellites, :friction, :hideOrbit, :loading_state, :mass, :n_clicks, :open, :orbitRadius, :rotation, :satelliteOrientation, :tension]
        wild_props = Symbol[]
        return Component("dashplanet", "DashPlanet", "dash_planet", available_props, wild_props; kwargs...)
end

dashplanet(children::Any; kwargs...) = dashplanet(;kwargs..., children = children)
dashplanet(children_maker::Function; kwargs...) = dashplanet(children_maker(); kwargs...)

