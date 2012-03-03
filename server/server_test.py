import unittest
from hamcrest import *
from mock import patch

from seamon_server import SeamonServer

class ServerTest(unittest.TestCase):
    def test_user_can_add_node_to_server(self):
        server = SeamonServer()
        server.add_node("node1")
        server.add_node("node2")
        nodes = server.list_nodes()
        assert_that(nodes, only_contains("node1", "node2"))


    @patch("data_collector.DataCollector.get_from_node")
    def test_server_can_get_data_from_nodes(self, data_collector):
        server = SeamonServer()
        server.add_node("node1")
        server.add_node("node2")

        server.get_data_from_nodes()
        data_collector.assert_any_call("node1")
        data_collector.assert_any_call("node2")


if __name__ == "__main__":
    unittest.main()
