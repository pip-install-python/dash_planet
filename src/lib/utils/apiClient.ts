const DEFAULT_API_URL = 'https://geomapindex.com/api/api-keys/validate';

interface ValidationResponse {
    valid: boolean;
    message: string;
    usage_count?: number;
}

export async function validateApiKey(
    apiKey: string | undefined,
    componentName: 'DashPlanet',
    itemsCount: number,
    apiUrl?: string
): Promise<ValidationResponse> {
    if (!apiKey) {
        return { valid: false, message: "No API key provided" };
    }

    try {
        const url = new URL(apiUrl || DEFAULT_API_URL);
        const fullUrl = `${url.origin}${url.pathname}?key=${apiKey}`;

        const response = await fetch(fullUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                component_name: componentName,
                items_count: itemsCount
            })
        });

        const data = await response.json();

        if (!response.ok) {
            console.error('API validation failed:', data);
            return {
                valid: false,
                message: data.message || "API validation failed"
            };
        }

        return {
            valid: data.valid,
            message: data.message,
            usage_count: data.usage_count
        };
    } catch (error) {
        console.error('API key validation error:', error);
        return { valid: false, message: "API validation error" };
    }
}