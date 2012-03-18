import unittest
from hamcrest import *

from node import Node

class NodeTest(unittest.TestCase):
    def test_node_has_name_ip_addres_and_port(self):
        node = Node(name="node1", ip_address="192.168.5.5", port=2223)
        assert_that(node.name, is_("node1"))
        assert_that(node.ip_address, is_("192.168.5.5"))
        assert_that(node.port, is_(2223))

    def test_node_full_path(self):
        node = Node(name="node1", ip_address="192.168.5.5", port=2223)
        full_path = "http://192.168.5.5:2223"
        assert_that(node.full_path(), is_(full_path))


if __name__ == "__main__":
    unittest.main()
