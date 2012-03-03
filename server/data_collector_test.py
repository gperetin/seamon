import unittest
from mock import patch, Mock
from hamcrest import *

from data_collector import DataCollector

SAMPLE_NODE_DATA = {
    "stat_name":"cpu_load",
    "data": {
        "load_1": 0.4,
        "load_5": 0.2,
        "load_15": 0.9
    }}

class DataCollectorTest(unittest.TestCase):
    @patch("data_collector.requests.get", return_value = SAMPLE_NODE_DATA)
    def test_gets_data_from_node(self, node_data):
        data = DataCollector.get_from_node(Mock())
        assert_that(data, is_(SAMPLE_NODE_DATA))

    @patch("data_collector.requests.get")
    def test_makes_get_request_to_node_fullpath(self, request):
        some_path = "http://localhost:1231"
        node = Mock(**{"full_path.return_value": some_path})
        data = DataCollector.get_from_node(node)
        request.assert_called_with(some_path)


if __name__ == "__main__":
    unittest.main()
