// src/lib/components/Orbit.js
import React from 'react';
import { animated, useSpring } from 'react-spring';

const orbitDefaultStyle = {
    position: 'absolute',
    borderRadius: '100%',
    borderWidth: 2,
    borderStyle: 'dotted',
    borderColor: 'lightgrey',
    zIndex: 0,
};

export function Orbit(props) {
    const {
        orbitRadius,
        planetWidth,
        planetHeight,
        open,
        tension,
        friction,
        mass,
        orbitStyle
    } = props;

    const finalStyle = React.useMemo(() => {
        return orbitStyle ? orbitStyle(orbitDefaultStyle) : orbitDefaultStyle;
    }, [orbitStyle]);

    const position = useSpring({
        reverse: !open,
        from: {
            width: 0,
            height: 0,
            top: '50%',
            left: '50%',
            opacity: 0,
            transform: 'translate(-50%, -50%)',
        },
        to: {
            width: orbitRadius * 2 * 1.1,
            height: orbitRadius * 2 * 1.1,
            top: '50%',
            left: '50%',
            opacity: 1,
            transform: 'translate(-50%, -50%)',
        },
        config: { mass, tension, friction },
    });

    return <animated.div style={{ ...finalStyle, ...position }} />;
}