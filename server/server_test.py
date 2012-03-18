import unittest
from hamcrest import *
from mock import patch, Mock

from seamon_server import SeamonServer

class ServerTest(unittest.TestCase):
    @patch("server.seamon_server.NodeRepository")
    def test_can_list_all_nodes(self, node_repository):
        SeamonServer.list_nodes()
        node_repository.all.assert_called_once_with()

    @patch("server.seamon_server.NodeRepository")
    def test_can_add_node(self, node_repository):
        SeamonServer.add_node("somename", "192.168.1.1", 2222)
        self.assertTrue(node_repository.save.called)

    @patch("server.seamon_server.NodeRepository")
    @patch("server.seamon_server.DataCollector")
    @patch("server.seamon_server.StatsRepository")
    def test_gets_node_info_from_data_collector(self, 
                                                stats_repository,
                                                data_collector, 
                                                node_repository):
        node = Mock()
        node_repository.by_name.return_value = node
        SeamonServer.get_node_stats("node1")
        data_collector.get_node_info.assert_called_with(node)

    @patch("server.seamon_server.DataCollector")
    @patch("server.seamon_server.NodeRepository")
    @patch("server.seamon_server.StatsRepository")
    def test_stores_data_it_gets_from_node(self, 
                                           stats_repository, 
                                           node_repository, 
                                           data_collector):
        data = Mock()
        node = Mock()
        node_repository.by_name.return_value = node
        data_collector.get_node_info.return_value = data
        SeamonServer.get_node_stats("asd")
        stats_repository.save_for_node.assert_called_once_with(node, data)
