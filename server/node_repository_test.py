import unittest
from hamcrest import *

from node import Node
from node_repository import NodeRepository

from db.session import engine
from db.tables import metadata

class NodeRepositoryTest(unittest.TestCase):
    def setUp(self):
        metadata.create_all(engine)

    def tearDown(self):
        metadata.drop_all(engine)

    def test_can_store_a_node(self):
        node = Node("node1", "192.123.3.3", 2312)
        NodeRepository.save(node)
        assert_that(NodeRepository.all()[0], is_(node))

    def test_can_find_node_by_name(self):
        node = Node("node2", "192.123.3.3", 2312)
        NodeRepository.save(node)
        node_by_name = NodeRepository.by_name("node2")
        assert_that(node_by_name, is_(node))
