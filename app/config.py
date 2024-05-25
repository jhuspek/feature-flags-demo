class AppProperties:
    APP_NAME = "feature-flag-demo"
    APP_ENV = "development"

    ROUTE_PREFIX_V1 = "/v1"
    API_PREFIX = "/api"

    UNLEASH_URL = "http://localhost:4242/api"
    UNLEASH_CUSTOM_HEADERS = {"Authorization": "default:development.unleash-insecure-api-token"}
    UNLEASH_INSTANCE_ID = "unleash-client-python"

    def __init__(self):
        pass
