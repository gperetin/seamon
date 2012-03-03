import unittest
from hamcrest import *
from mock import patch, Mock

from seamon_server import SeamonServer

class ServerTest(unittest.TestCase):
    def setUp(self):
        self.server = SeamonServer()

    def test_has_list_of_nodes(self):
        self.server.add_node("node1", "192.168.5.2", 2222)
        self.server.add_node("node2", "194.123.23.3", 2221)
        nodes = self.server.list_nodes()
        assert_that(nodes[0].name, is_("node1"))
        assert_that(nodes[1].name, is_("node2"))

    def test_can_identify_node_by_name(self):
        self.server.add_node("node1", "192.168.5.5", 22312)
        node = self.server.node_by_name("node1")
        assert_that(node.name, is_("node1"))
        assert_that(node.ip_address, is_("192.168.5.5"))
        assert_that(node.port, is_(22312))

#     def test_gets_node_info_from_data_collector(self):
#         server = SeamonServer()
#         data = server.get_node_info("node1")



    # def test_returns_none_for_nonexistent_node(self):
    #     pass


# if __name__ == "__main__":
#     unittest.main()
