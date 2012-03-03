import unittest
from hamcrest import *

from seamon_server import SeamonServer

class ServerTest(unittest.TestCase):
    def test_user_can_add_node_to_server(self):
        server = SeamonServer()
        server.add_node("node1")
        server.add_node("node2")
        nodes = server.list_nodes()
        assert_that(nodes, only_contains("node1", "node2"))

if __name__ == "__main__":
    unittest.main()
