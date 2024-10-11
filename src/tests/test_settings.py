import unittest
from wuai.settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        # Initialize settings
        self.settings = Settings()

    def test_settings_keys(self):
        # Check if all expected keys are present
        self.assertIsNotNone(self.settings.token_url, "token_url should not be None")
        self.assertIsNotNone(self.settings.client_id, "client_id should not be None")
        self.assertIsNotNone(self.settings.client_secret, "client_secret should not be None")
        self.assertIsNotNone(self.settings.scope, "scope should not be None")
        self.assertIsNotNone(self.settings.gpt4, "gpt4 should not be None")
        self.assertIsNotNone(self.settings.gpt4o, "gpt4o should not be None")
        self.assertIsNotNone(self.settings.payload, "payload should not be None")
        self.assertIsNotNone(self.settings.api, "api should not be None")

if __name__ == '__main__':
    unittest.main()