import unittest
from hamcrest import *

from pymongo import Connection
# TODO: extract to config
connection = Connection('127.0.0.1', 27017)
db = connection.seamon

from node import Node
from node_repository import NodeRepository

class NodeRepositoryTest(unittest.TestCase):
    def setUp(self):
        db.nodes.remove()

    def test_can_store_a_node(self):
        node = Node(name="node1", ip_address="192.123.3.3", port=2312)
        NodeRepository.save(node)
        assert_that(NodeRepository.all()[0].name, is_("node1"))
        assert_that(NodeRepository.all()[0].ip_address, is_("192.123.3.3"))

    def test_can_find_node_by_name(self):
        node = Node(name="node2", ip_address="192.123.3.3", port=2312)
        NodeRepository.save(node)
        node_by_name = NodeRepository.by_name("node2")
        assert_that(node_by_name.name, is_("node2"))
        assert_that(node_by_name.ip_address, is_("192.123.3.3"))
