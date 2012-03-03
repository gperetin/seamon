import unittest
from hamcrest import *

from node import Node

class NodeTest(unittest.TestCase):
    def test_node_has_ip_addres_and_port(self):
        node = Node("192.168.5.5", 2223)
        assert_that(node.ip_address, "192.168.5.5")
        assert_that(node.port, is_(2223))

if __name__ == "__main__":
    unittest.main()
