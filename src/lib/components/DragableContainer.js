// src/lib/components/DragableContainer.js
import React from 'react';
import { animated, useSpring } from 'react-spring';
import { useDrag } from 'react-use-gesture';

const DEFAULT_DRAG_RADIUS = 12;
const DEFAULT_BOUNCE_RADIUS = 3;

export function DragableContainer(props) {
    const {
        children,
        on,
        dragable,
        dragRadius,
        bounceRadius,
        open,
        bounceOnOpen,
        bounceOnClose,
        bounceDirection,
    } = props;

    if (!on) {
        return <>{children}</>;
    }

    const [springs, api] = useSpring(() => ({
        x: 0,
        y: 0,
        cursor: 'pointer',
        config: { tension: 400, friction: 7, precision: 0.1 },
    }));

    React.useEffect(() => {
        if ((open && bounceOnOpen) || (!open && bounceOnClose)) {
            const bRadius = bounceRadius || DEFAULT_BOUNCE_RADIUS;
            let x = bRadius;
            let y = bRadius;

            switch (bounceDirection) {
                case 'LEFT':
                    x = -bRadius;
                    y = 0;
                    break;
                case 'RIGHT':
                    x = bRadius;
                    y = 0;
                    break;
                case 'TOP':
                    x = 0;
                    y = -bRadius;
                    break;
                case 'BOTTOM':
                    x = 0;
                    y = bRadius;
                    break;
                default:
                    break;
            }

            api.start({ x, y });
            setTimeout(() => api.start({ x: 0, y: 0 }), 100);
        }
    }, [open, bounceOnOpen, bounceOnClose, bounceDirection, bounceRadius, api]);

    const bind = useDrag(({ down, movement: [dX, dY], tap }) => {
        if (tap) {
            return;
        }

        if (dragable) {
            const rMax = dragRadius || DEFAULT_DRAG_RADIUS;
            const r = Math.sqrt(dX ** 2 + dY ** 2);

            if (r > rMax) {
                dX *= rMax / r;
                dY *= rMax / r;
            }

            api.start({
                x: down ? dX : 0,
                y: down ? dY : 0,
                immediate: down,
                cursor: down ? 'grabbing' : 'pointer',
            });
        }
    }, { filterTaps: true });

    return (
        <div style={{
            position: 'absolute',
            left: '50%',
            top: '50%',
            transform: 'translate(-50%, -50%)',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center'
        }}>
            <animated.div
                {...bind()}
                style={{
                    ...springs,
                    transform: springs.x.to((x, y) => `translate3d(${x}px,${y}px,0)`),
                }}
            >
                {children}
            </animated.div>
        </div>
    );
}