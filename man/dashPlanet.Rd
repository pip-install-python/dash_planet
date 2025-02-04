% Auto-generated: do not edit by hand
\name{dashPlanet}

\alias{dashPlanet}

\title{DashPlanet component}

\description{
DashPlanet is an interactive orbit menu component that displays children in a circular orbit. Free tier limitations apply unless a valid API key is provided.
}

\usage{
dashPlanet(children=NULL, id=NULL, apiKey=NULL, autoClose=NULL,
bounce=NULL, bounceDirection=NULL, bounceOnClose=NULL,
bounceOnOpen=NULL, centerContent=NULL,
dragRadiusPlanet=NULL, dragRadiusSatellites=NULL,
dragablePlanet=NULL, dragableSatellites=NULL, friction=NULL,
hideOrbit=NULL, loading_state=NULL, mass=NULL,
n_clicks=NULL, open=NULL, orbitRadius=NULL, rotation=NULL,
satelliteOrientation=NULL, tension=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. The satellite items that orbit around the center. These can be any valid React nodes.
Free tier limits apply unless a valid API key is provided.}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{apiKey}{Character. API key for unlocking full functionality. Without a valid key, the component
will operate in free tier mode with limited features.}

\item{autoClose}{Logical. Whether to automatically close when clicking outside. When true, the menu closes
when clicking anywhere outside the component.}

\item{bounce}{Logical. Whether to bounce on both open and close. When true, applies bounce animation
in the specified bounceDirection. Requires valid API key.}

\item{bounceDirection}{A value equal to: 'top', 'bottom', 'left', 'right'. Direction of the bounce animation. Determines which direction the bounce effect
is applied.}

\item{bounceOnClose}{Logical. Whether to bounce only on close. When true, applies bounce animation only when
closing the menu. Requires valid API key.}

\item{bounceOnOpen}{Logical. Whether to bounce only on open. When true, applies bounce animation only when
opening the menu. Requires valid API key.}

\item{centerContent}{A list of or a singular dash component, string or number. The center content of the planet menu. This can be any valid React node.}

\item{dragRadiusPlanet}{Numeric. Maximum drag radius for the planet in pixels. Controls how far the center content
can be dragged when dragablePlanet is true.}

\item{dragRadiusSatellites}{Numeric. Maximum drag radius for satellites in pixels. Controls how far satellite items
can be dragged when dragableSatellites is true.}

\item{dragablePlanet}{Logical. Whether the planet can be dragged. When true, the center content can be dragged
within the dragRadiusPlanet limit. Requires valid API key.}

\item{dragableSatellites}{Logical. Whether satellites can be dragged. When true, satellite items can be dragged
within the dragRadiusSatellites limit. Requires valid API key.}

\item{friction}{Numeric. Friction for spring physics animations. Controls the spring damping.}

\item{hideOrbit}{Logical. Whether to hide the orbit line. When true, the circular orbit path is not visible.}

\item{loading_state}{Lists containing elements 'is_loading', 'prop_name', 'component_name'.
those elements have the following types:
  - is_loading (logical; optional): determines if the component is loading or not
  - prop_name (character; optional): holds which property is loading
  - component_name (character; optional): holds the name of the component that is loading. Object that holds the loading state object coming from dash-renderer.}

\item{mass}{Numeric. Mass for spring physics animations. Controls the weight/inertia of animations.}

\item{n_clicks}{Numeric. Number of times the planet has been clicked. This value is updated automatically
when the planet is clicked.}

\item{open}{Logical. Whether the planet menu is open. Controls the visibility of satellite items.}

\item{orbitRadius}{Numeric. Radius of the orbit in pixels. Controls how far the satellites are from the center.}

\item{rotation}{Numeric. Rotation angle in degrees. Controls the starting position of satellites.}

\item{satelliteOrientation}{A value equal to: 'default', 'inside', 'outside', 'readable'. Orientation of the satellites. Controls how satellite items are rotated in their orbit.}

\item{tension}{Numeric. Tension for spring physics animations. Controls the spring stiffness.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

