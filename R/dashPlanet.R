# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashPlanet <- function(children=NULL, id=NULL, apiKey=NULL, autoClose=NULL, bounce=NULL, bounceDirection=NULL, bounceOnClose=NULL, bounceOnOpen=NULL, centerContent=NULL, dragRadiusPlanet=NULL, dragRadiusSatellites=NULL, dragablePlanet=NULL, dragableSatellites=NULL, friction=NULL, hideOrbit=NULL, loading_state=NULL, mass=NULL, n_clicks=NULL, open=NULL, orbitRadius=NULL, rotation=NULL, satelliteOrientation=NULL, tension=NULL) {
    
    props <- list(children=children, id=id, apiKey=apiKey, autoClose=autoClose, bounce=bounce, bounceDirection=bounceDirection, bounceOnClose=bounceOnClose, bounceOnOpen=bounceOnOpen, centerContent=centerContent, dragRadiusPlanet=dragRadiusPlanet, dragRadiusSatellites=dragRadiusSatellites, dragablePlanet=dragablePlanet, dragableSatellites=dragableSatellites, friction=friction, hideOrbit=hideOrbit, loading_state=loading_state, mass=mass, n_clicks=n_clicks, open=open, orbitRadius=orbitRadius, rotation=rotation, satelliteOrientation=satelliteOrientation, tension=tension)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashPlanet',
        namespace = 'dash_planet',
        propNames = c('children', 'id', 'apiKey', 'autoClose', 'bounce', 'bounceDirection', 'bounceOnClose', 'bounceOnOpen', 'centerContent', 'dragRadiusPlanet', 'dragRadiusSatellites', 'dragablePlanet', 'dragableSatellites', 'friction', 'hideOrbit', 'loading_state', 'mass', 'n_clicks', 'open', 'orbitRadius', 'rotation', 'satelliteOrientation', 'tension'),
        package = 'dashPlanet'
        )

    structure(component, class = c('dash_component', 'list'))
}
