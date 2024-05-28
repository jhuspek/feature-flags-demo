import os


class AppProperties:
    APP_NAME = os.getenv("APP_NAME", "feature-flag-demo")
    APP_ENV = os.getenv("APP_ENV", "development")

    ROUTE_PREFIX_V1 = os.getenv("ROUTE_PREFIX_V1", "/v1")
    API_PREFIX = os.getenv("API_PREFIX", "/api")

    UNLEASH_URL = os.getenv("UNLEASH_URL", "http://localhost:4242/api")
    UNLEASH_CUSTOM_HEADERS = {
        "Authorization": os.getenv("UNLEASH_CUSTOM_HEADERS", "default:development.unleash-insecure-api-token")
    }
    UNLEASH_INSTANCE_ID = os.getenv("UNLEASH_INSTANCE_ID", "unleash-client-python")

    def __init__(self):
        pass
