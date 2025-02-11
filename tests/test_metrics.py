import unittest
import sys
import os

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from observability.metrics import Metrics

class TestMetrics(unittest.TestCase):

    def setUp(self):
        """Setup method to create a Metrics instance for testing."""
        self.metrics = Metrics()

    def test_initial_query_count(self):
        """Test that the initial query count is 0."""
        self.assertEqual(self.metrics.get_query_count(), 0)

    def test_increment_query_count(self):
        """Test incrementing the query count."""
        self.metrics.increment_query_count()
        self.assertEqual(self.metrics.get_query_count(), 1)

        self.metrics.increment_query_count()
        self.assertEqual(self.metrics.get_query_count(), 2)

    def test_get_query_count(self):
        """Test getting the query count."""
        self.assertEqual(self.metrics.get_query_count(), 0)

        self.metrics.increment_query_count()
        self.assertEqual(self.metrics.get_query_count(), 1)

if __name__ == '__main__':
    unittest.main()
