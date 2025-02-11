import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from vitalik_ai import VitalikAI

class TestVitalikAI(unittest.TestCase):

    def setUp(self):
        """Setup method to create a VitalikAI instance for testing."""
        with patch('os.getenv', return_value='dummy_api_key'):
            self.ai = VitalikAI()

    @patch('openai.chat.completions.create')
    def test_generate_tweet(self, mock_openai_chat):
        """Test the generate_tweet method with a mocked OpenAI API."""

        # Mock the response from the OpenAI API
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Ethereum is the future of decentralized applications."
        mock_openai_chat.return_value = mock_response

        prompt = "What do you think about Ethereum?"
        tweet = self.ai.generate_tweet(prompt)

        # Assert that the tweet is what we expect (from the mocked API)
        self.assertEqual(tweet, "Ethereum is the future of decentralized applications.")
        mock_openai_chat.assert_called_once()

    @patch('openai.chat.completions.create')
    def test_generate_tweet_error(self, mock_openai_chat):
        """Test error handling in generate_tweet."""
        mock_openai_chat.side_effect = Exception("API Error")
        prompt = "What do you think about Ethereum?"
        tweet = self.ai.generate_tweet(prompt)
        self.assertEqual(tweet, "Error generating tweet: API Error")

if __name__ == '__main__':
    unittest.main()
