/**
 * Utility functions to support both Dash 2 and Dash 3 components
 */

import React from "react";
import { DashBaseProps } from "../types/dash";

export const isDash3 = (): boolean => {
    return !!(window as any).dash_component_api;
};

export const setPersistence = (Component: any, props: string[] = ["value"]): void => {
    const persistence = { persisted_props: props, persistence_type: "local" };

    parseFloat(React.version) < 18.3
        ? (Component.defaultProps = persistence)
        : (Component.dashPersistence = persistence);
};

export const getLoadingState = (loading_state?: DashBaseProps["loading_state"]): boolean =>
    isDash3()
        ? (window as any).dash_component_api.useDashContext().useLoading()
        : loading_state?.is_loading ?? false;

export const getChildLayout = (child: any): { type: any; props: any } => {
    if (isDash3()) {
        return (window as any).dash_component_api.getLayout(child.props.componentPath);
    }

    return {
        type: child.props?._dashprivate_layout?.type,
        props: child.props?._dashprivate_layout?.props,
    };
};

export const getChildProps = (child: any): any => {
    return getChildLayout(child).props;
};

export const setProps = (componentPath: string, props: Record<string, any>): void => {
    if (isDash3()) {
        (window as any).dash_clientside.set_props(componentPath, props);
    }
};

export const useStore = () => {
    if (isDash3()) {
        return (window as any).dash_component_api.useDashContext().useStore();
    }
    return null;
};

export const useDispatch = () => {
    if (isDash3()) {
        return (window as any).dash_component_api.useDashContext().useDispatch();
    }
    return null;
};