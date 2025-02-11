import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from rag.rag import VitalikKAG

class TestVitalikKAG(unittest.TestCase):

    def setUp(self):
        """Setup method to create a sample knowledge graph for testing."""
        self.sample_knowledge_graph = {
            "nodes": [
                {"id": "ethereum", "label": "Ethereum"},
                {"id": "layer2", "label": "Layer 2 Scaling"},
                {"id": "optimism", "label": "Optimism"},
                {"id": "zkrollups", "label": "ZK-rollups"},
                {"id": "decentralization", "label": "Decentralization"},
                {"id": "account_abstraction", "label": "Account Abstraction"}
            ],
            "edges": [
                {"source": "ethereum", "target": "layer2", "relation": "uses"},
                {"source": "layer2", "target": "optimism", "relation": "is_a"},
                {"source": "layer2", "target": "zkrollups", "relation": "is_a"},
                {"source": "ethereum", "target": "decentralization", "relation": "promotes"},
                {"source": "ethereum", "target": "account_abstraction", "relation": "benefits"}
            ]
        }
        # Mock os.getenv to return a dummy API key during testing
        with patch('os.getenv', return_value='dummy_api_key'):
            self.kag = VitalikKAG(knowledge_graph=self.sample_knowledge_graph)

    def test_retrieve_context(self):
        """Test the retrieve_context method."""
        query = "Tell me about Layer 2"
        context = self.kag.retrieve_context(query)

        # Assert that the relevant nodes are present
        self.assertIn("layer2", [node['id'] for node in context['nodes']])
        self.assertIn("optimism", [node['id'] for node in context['nodes']])
        self.assertIn("zkrollups", [node['id'] for node in context['nodes']])

        # Assert that edges are correctly retrieved
        self.assertEqual(len(context['edges']), 5)

        query2 = "ethereum decentralization"
        context2 = self.kag.retrieve_context(query2)
        self.assertIn("ethereum", [node['id'] for node in context2['nodes']])
        self.assertIn("decentralization", [node['id'] for node in context2['nodes']])
        self.assertEqual(len(context2['edges']), 5)

        query3 = "blah blah"
        context3 = self.kag.retrieve_context(query3)
        self.assertEqual(len(context3['nodes']), 0)
        self.assertEqual(len(context3['edges']), 0)


    @patch('openai.chat.completions.create')
    def test_generate_tweet_response(self, mock_openai_chat):
        """Test the generate_tweet_response method with a mocked OpenAI API."""

        # Mock the response from the OpenAI API
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Layer 2 scaling is crucial for Ethereum's future."
        mock_openai_chat.return_value = mock_response

        query = "Tell me about Layer 2"
        context = self.kag.retrieve_context(query)
        response = self.kag.generate_tweet_response(query, context)

        # Assert that the response is what we expect (from the mocked API)
        self.assertEqual(response, "Layer 2 scaling is crucial for Ethereum's future.")
        mock_openai_chat.assert_called_once()

    @patch('openai.chat.completions.create')
    def test_generate_tweet_response_error(self, mock_openai_chat):
        """Test error handling in generate_tweet_response."""
        mock_openai_chat.side_effect = Exception("API Error")
        query = "Tell me about Layer 2"
        context = {"nodes": [], "edges": []}
        response = self.kag.generate_tweet_response(query, context)
        self.assertEqual(response, "Error generating response: API Error")

if __name__ == '__main__':
    unittest.main()
