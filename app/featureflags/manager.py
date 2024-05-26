import logging
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
        self.connected = False

    def initialize(self):
        try:
            self.unleash.initialize_client()
            self.connected = True
            logging.info("Connected to Unleash server successfully.")
        except Exception as e:
            self.connected = False
            logging.error(f"Failed to connect to Unleash server. Error: {e}")

    def is_enabled(self, feature_name):
        if not self.connected:
            logging.warning(f"Unleash server is not connected.")
            return False
        try:
            return self.unleash.is_enabled(feature_name)
        except Exception as e:
            logging.error(f"Error checking feature flag '{feature_name}': {e}")
            return False


unleash_manager = UnleashClientManager()
