from data_collector import DataCollector
from node import Node
from node_repository import NodeRepository

class SeamonServer(object):
    def add_node(self, name, ip_address, port):
        NodeRepository.save(Node(name, ip_address, port))

    def list_nodes(self):
        return NodeRepository.nodes

    def get_node_info(self, node_name):
        node = NodeRepository.by_name(node_name)
        return DataCollector.get_node_info(node)

    def node_by_name(self, name):
        return NodeRepository.by_name(name)
