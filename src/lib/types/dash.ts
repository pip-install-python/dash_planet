export interface DashBaseProps {
    loading_state?: {
        is_loading: boolean;
        prop_name: string;
        component_name: string;
    };
    setProps?: (props: Record<string, any>) => void;
}

export interface DashPlanetProps extends DashBaseProps {
    id?: string;
    centerContent?: React.ReactNode;
    children?: React.ReactNode;
    n_clicks?: number;
    open?: boolean;
    orbitRadius?: number;
    rotation?: number;
    hideOrbit?: boolean;
    autoClose?: boolean;
    dragablePlanet?: boolean;
    dragRadiusPlanet?: number;
    dragableSatellites?: boolean;
    dragRadiusSatellites?: number;
    bounce?: boolean;
    bounceOnOpen?: boolean;
    bounceOnClose?: boolean;
    bounceDirection?: 'TOP' | 'BOTTOM' | 'LEFT' | 'RIGHT';
    satelliteOrientation?: 'DEFAULT' | 'INSIDE' | 'OUTSIDE' | 'READABLE';
    mass: 1,
    tension: 500,
    friction: 17,
    /** API key for unlocking full functionality */
    apiKey?: string;
}