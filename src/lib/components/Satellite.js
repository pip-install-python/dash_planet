// src/lib/components/Satellite.js
import React from 'react';
import { animated, useSpring } from 'react-spring';
import useResizeObserver from 'use-resize-observer';
import { DragableContainer } from './DragableContainer';

const DEG_TO_RAD = 0.0174533;
const toRadians = (degrees) => degrees * DEG_TO_RAD;

function getFinalDeltaPositions(index, satelliteCount, orbitRadius, rotation) {
    const SEPARATION_ANGLE = 360 / satelliteCount;
    // Group satellites in the top half by adjusting their positioning
    const HALF_MENU_OFFSET = 180;  // This centers them in the top half
    const TARGET_ANGLE = rotation + (index * SEPARATION_ANGLE) - HALF_MENU_OFFSET;

    return {
        deltaX: orbitRadius * Math.sin(toRadians(TARGET_ANGLE)),
        deltaY: orbitRadius * Math.cos(toRadians(TARGET_ANGLE)),
        angle: TARGET_ANGLE,
    };
}

export function Satellite(props) {
    const {
        children,
        index,
        satelliteCount,
        open,
        tension,
        friction,
        mass,
        orbitRadius,
        rotation,
        dragable,
        dragRadius,
        orientation,
    } = props;

    const { ref, height = 0, width = 0 } = useResizeObserver();

    const [springs, api] = useSpring(() => ({
        from: {
            transform: 'translate(-50%, -50%) translate(0px, 0px) rotate(0deg)',
            top: '50%',
            left: '50%',
            opacity: 0,
        },
        config: {
            mass,
            tension,
            friction,
            clamp: true // Prevent animation overshooting
        }
    }));

    React.useEffect(() => {
        const { deltaX, deltaY, angle } = getFinalDeltaPositions(
            index,
            satelliteCount,
            orbitRadius,
            rotation
        );

        let rotateAngle = 0;
        switch (orientation) {
            case 'OUTSIDE':
                rotateAngle = angle;
                break;
            case 'INSIDE':
                rotateAngle = angle + 180;
                break;
            case 'READABLE':
                rotateAngle = angle > 90 && angle < 270 ? angle + 180 : angle;
                break;
        }

        if (open) {
            api.start({
                to: {
                    transform: `translate(-50%, -50%) translate(${deltaX}px, ${-deltaY}px) rotate(${rotateAngle}deg)`,
                    top: '50%',
                    left: '50%',
                    opacity: 1,
                },
                config: {
                    mass,
                    tension,
                    friction,
                    clamp: true
                }
            });
        } else {
            api.start({
                to: {
                    transform: 'translate(-50%, -50%) translate(0px, 0px) rotate(0deg)',
                    top: '50%',
                    left: '50%',
                    opacity: 0,
                },
                config: {
                    mass,
                    tension,
                    friction,
                    clamp: true
                }
            });
        }
    }, [open, index, satelliteCount, orbitRadius, rotation, orientation, api, mass, tension, friction]);

    return (
        <animated.div
            style={{
                position: 'absolute',
                zIndex: open ? 2 : 0,
                pointerEvents: open ? 'auto' : 'none',
                ...springs
            }}
        >
            <DragableContainer
                on={dragable}
                dragRadius={dragRadius}
                dragable={dragable}
            >
                <div ref={ref}>{children}</div>
            </DragableContainer>
        </animated.div>
    );
}