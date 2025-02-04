// src/lib/components/Planet.js
import React from 'react';
import { ClickAwayListener } from '@mui/material';
import useResizeObserver from 'use-resize-observer';
import { DragableContainer } from './DragableContainer';
import { Orbit } from './Orbit';
import { Satellite } from './Satellite';

const DEFAULT_MASS = 1;
const DEFAULT_TENSION = 500;
const DEFAULT_FRICTION = 17;
const DEFAULT_ROTATION = 0;
const DEFAULT_RADIUS = 100;

export function Planet(props) {
    const {
        centerContent,
        children,
        open,
        onClick,
        mass = DEFAULT_MASS,
        tension = DEFAULT_TENSION,
        friction = DEFAULT_FRICTION,
        orbitRadius = DEFAULT_RADIUS,
        rotation = DEFAULT_ROTATION,
        orbitStyle,
        hideOrbit,
        onClose,
        autoClose,
        dragablePlanet,
        dragRadiusPlanet,
        dragableSatellites,
        dragRadiusSatellites,
        bounceRadius,
        bounce,
        bounceOnOpen,
        bounceOnClose,
        bounceDirection,
        satelliteOrientation,
    } = props;

    const { ref, height = 0, width = 0 } = useResizeObserver();
    const [_open, setOpen] = React.useState(!!open);

    React.useEffect(() => {
        setOpen(!!open);
    }, [open]);

    const satellites = React.Children.map(children, (c, i) => {
        if (!c) return null;
        return (
            <Satellite
                key={i}
                index={i}
                open={_open}
                satelliteCount={React.Children.count(children)}
                planetHeight={height}
                planetWidth={width}
                mass={mass}
                friction={friction}
                tension={tension}
                orbitRadius={orbitRadius * 1.1}
                rotation={rotation}
                dragable={!!dragableSatellites}
                dragRadius={dragRadiusSatellites}
                orientation={satelliteOrientation}
            >
                {c}
            </Satellite>
        );
    });

    const handlePlanetClick = (e) => {
        if (onClick) {
            onClick(e);
        } else if (autoClose) {
            setOpen(!_open);
            if (_open && onClose) {
                onClose(e);
            }
        } else {
            setOpen(true);
        }
    };

    const handleClickAway = (e) => {
        if (autoClose) {
            setOpen(false);
        }
        if (onClose && _open) {
            onClose(e);
        }
    };

    return (
        <ClickAwayListener onClickAway={handleClickAway}>
            <div style={{
                position: 'relative',
                width: '100%',
                height: '100%',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center'
            }}>
                {!hideOrbit && (
                    <Orbit
                        open={_open}
                        orbitStyle={orbitStyle}
                        planetHeight={height}
                        planetWidth={width}
                        mass={mass}
                        friction={friction}
                        tension={tension}
                        orbitRadius={orbitRadius}
                    />
                )}
                {satellites}
                <div
                    style={{
                        position: 'absolute',
                        left: '50%',
                        top: '50%',
                        transform: 'translate(-50%, -50%)',
                        zIndex: 1
                    }}
                    onClick={handlePlanetClick}
                >
                    <DragableContainer
                        on={!!dragablePlanet || !!bounce || !!bounceOnOpen || !!bounceOnClose}
                        dragable={!!dragablePlanet}
                        dragRadius={dragRadiusPlanet}
                        open={_open}
                        bounceRadius={bounceRadius}
                        bounceOnOpen={(bounce && !bounceOnClose) || bounceOnOpen}
                        bounceOnClose={(bounce && !bounceOnOpen) || bounceOnClose}
                        bounceDirection={bounceDirection}
                    >
                        <div ref={ref}>{centerContent}</div>
                    </DragableContainer>
                </div>
            </div>
        </ClickAwayListener>
    );
}