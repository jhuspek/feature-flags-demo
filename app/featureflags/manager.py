from UnleashClient import UnleashClient

from app.config import AppProperties


class UnleashClientManager:
    def __init__(self):
        self.config = AppProperties()
        self.unleash = UnleashClient(
            url=self.config.UNLEASH_URL,
            environment=self.config.APP_NAME,
            app_name=self.config.APP_NAME,
            custom_headers=self.config.UNLEASH_CUSTOM_HEADERS,
            instance_id=self.config.UNLEASH_INSTANCE_ID
        )

    def is_enabled(self, feature_name):
        return self.unleash.is_enabled(feature_name)


unleash_manager = UnleashClientManager()
