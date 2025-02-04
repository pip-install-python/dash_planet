import React, { useEffect, useState, useRef } from 'react';
import PropTypes from 'prop-types';
import { Planet } from './Planet';
import { getLoadingState } from '../utils/dash3';
import { validateApiKey } from '../utils/apiClient';

const FREE_TIER_LIMIT = 3;

/**
 * DashPlanet is an interactive orbit menu component that displays children in a circular orbit.
 * Free tier limitations apply unless a valid API key is provided.
 */
const DashPlanet = (props) => {
    const {
        id,
        centerContent,
        children,
        open = false,
        orbitRadius = 120,
        rotation = 0,
        hideOrbit = false,
        autoClose = false,
        dragablePlanet = false,
        dragRadiusPlanet = 12,
        dragableSatellites = false,
        dragRadiusSatellites = 12,
        bounce = false,
        bounceOnOpen = false,
        bounceOnClose = false,
        bounceDirection = 'TOP',
        satelliteOrientation = 'DEFAULT',
        mass = 1,
        tension = 500,
        friction = 17,
        n_clicks = 0,
        apiKey,
        loading_state,
        setProps
    } = props;

    const [validatedKey, setValidatedKey] = useState(false);
    const isLoading = getLoadingState(loading_state);
    const itemsCount = React.Children.count(children); // Moved outside useEffect

    useEffect(() => {
        const validateKey = async () => {
            if (!apiKey) {
                setValidatedKey(false);
                return;
            }

            try {
                const result = await validateApiKey(apiKey, 'DashPlanet', itemsCount);
                setValidatedKey(Boolean(apiKey && result.valid));
            } catch (error) {
                console.error('API validation error:', error);
                setValidatedKey(false);
            }
        };

        validateKey();
    }, [apiKey, itemsCount]);

    const handleClick = (e) => {
        if (setProps) {
            setProps({
                n_clicks: n_clicks + 1,
                open: !open
            });
        }
    };

    const handleClose = (e) => {
        if (setProps) {
            setProps({ open: false });
        }
    };

    const limitedChildren = React.Children.toArray(children).slice(0, validatedKey ? undefined : FREE_TIER_LIMIT);
    const satellites = React.Children.map(limitedChildren, (child) => child || null);

    return (
        <div id={id} style={{
            width: '100%',
            height: '100%',
            position: 'relative',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center'
        }}>
            <div style={{
                position: 'relative',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center'
            }}>
                <Planet
                    centerContent={centerContent}
                    open={open}
                    onClick={handleClick}
                    onClose={handleClose}
                    orbitRadius={orbitRadius}
                    rotation={rotation}
                    hideOrbit={hideOrbit}
                    autoClose={autoClose}
                    dragablePlanet={validatedKey && dragablePlanet}
                    dragRadiusPlanet={dragRadiusPlanet}
                    dragableSatellites={validatedKey && dragableSatellites}
                    dragRadiusSatellites={dragRadiusSatellites}
                    bounce={validatedKey && bounce}
                    bounceOnOpen={validatedKey && bounceOnOpen}
                    bounceOnClose={validatedKey && bounceOnClose}
                    bounceDirection={bounceDirection}
                    satelliteOrientation={satelliteOrientation}
                    mass={mass}
                    tension={tension}
                    friction={friction}
                    isLoading={isLoading}
                >
                    {satellites}
                </Planet>
            </div>
        </div>
    );
};

DashPlanet.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The center content of the planet menu. This can be any valid React node.
     */
    centerContent: PropTypes.node,

    /**
     * The satellite items that orbit around the center. These can be any valid React nodes.
     * Free tier limits apply unless a valid API key is provided.
     */
    children: PropTypes.node,

    /**
     * Number of times the planet has been clicked. This value is updated automatically
     * when the planet is clicked.
     */
    n_clicks: PropTypes.number,

    /**
     * Whether the planet menu is open. Controls the visibility of satellite items.
     */
    open: PropTypes.bool,

    /**
     * Radius of the orbit in pixels. Controls how far the satellites are from the center.
     */
    orbitRadius: PropTypes.number,

    /**
     * Rotation angle in degrees. Controls the starting position of satellites.
     */
    rotation: PropTypes.number,

    /**
     * Whether to hide the orbit line. When true, the circular orbit path is not visible.
     */
    hideOrbit: PropTypes.bool,

    /**
     * Whether to automatically close when clicking outside. When true, the menu closes
     * when clicking anywhere outside the component.
     */
    autoClose: PropTypes.bool,

    /**
     * Whether the planet can be dragged. When true, the center content can be dragged
     * within the dragRadiusPlanet limit. Requires valid API key.
     */
    dragablePlanet: PropTypes.bool,

    /**
     * Maximum drag radius for the planet in pixels. Controls how far the center content
     * can be dragged when dragablePlanet is true.
     */
    dragRadiusPlanet: PropTypes.number,

    /**
     * Whether satellites can be dragged. When true, satellite items can be dragged
     * within the dragRadiusSatellites limit. Requires valid API key.
     */
    dragableSatellites: PropTypes.bool,

    /**
     * Maximum drag radius for satellites in pixels. Controls how far satellite items
     * can be dragged when dragableSatellites is true.
     */
    dragRadiusSatellites: PropTypes.number,

    /**
     * Whether to bounce on both open and close. When true, applies bounce animation
     * in the specified bounceDirection. Requires valid API key.
     */
    bounce: PropTypes.bool,

    /**
     * Whether to bounce only on open. When true, applies bounce animation only when
     * opening the menu. Requires valid API key.
     */
    bounceOnOpen: PropTypes.bool,

    /**
     * Whether to bounce only on close. When true, applies bounce animation only when
     * closing the menu. Requires valid API key.
     */
    bounceOnClose: PropTypes.bool,

    /**
     * Direction of the bounce animation. Determines which direction the bounce effect
     * is applied.
     */
    bounceDirection: PropTypes.oneOf(['TOP', 'BOTTOM', 'LEFT', 'RIGHT']),

    /**
     * Orientation of the satellites. Controls how satellite items are rotated in their orbit.
     */
    satelliteOrientation: PropTypes.oneOf(['DEFAULT', 'INSIDE', 'OUTSIDE', 'READABLE']),

    /**
     * Mass for spring physics animations. Controls the weight/inertia of animations.
     */
    mass: PropTypes.number,

    /**
     * Tension for spring physics animations. Controls the spring stiffness.
     */
    tension: PropTypes.number,

    /**
     * Friction for spring physics animations. Controls the spring damping.
     */
    friction: PropTypes.number,

    /**
     * API key for unlocking full functionality. Without a valid key, the component
     * will operate in free tier mode with limited features.
     */
    apiKey: PropTypes.string,

    /**
     * Object that holds the loading state object coming from dash-renderer.
     */
    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string,
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     */
    setProps: PropTypes.func
};

export default DashPlanet;