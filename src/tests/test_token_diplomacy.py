import unittest
from wuai.token_diplomacy import TokenDiplomat
from wuai.post2api import post_data

class TestTokenDiplomatIntegration(unittest.TestCase):
    def setUp(self):
        self.token_diplomat = TokenDiplomat()


    def test_refresh_token_integration(self):
        # This will perform an actual request to get a token
        try:
            token = self.token_diplomat.refresh_token()
            self.assertIsNotNone(token, "Token should not be None")
            print("Access token obtained:", token)
        except RuntimeError as e:
            self.fail(f"Failed to obtain token: {e}")

    def test_post_data_integration(self):
        # This will perform an actual request to post data
        try:
            token = self.token_diplomat.refresh_token()
            hello_message = {
                "messages": [{"role": "user", "content": "What is the first letter of the alphabet?"}]
            }
            result = post_data(self.token_diplomat.api.gpt4o, token, hello_message)
            self.assertIn("choices", result, "Response should contain 'choices'")
            message_content = result["choices"][0]["message"]["content"]
            print("Message Response:", message_content)
        except RuntimeError as e:
            self.fail(f"Failed to post data: {e}")

if __name__ == '__main__':
    unittest.main()
