from data_collector import DataCollector
from node import Node

class SeamonServer(object):
    def __init__(self):
        self.nodes = []

    def add_node(self, name, ip_address, port):
        self.nodes.append(Node(name, ip_address, port))

    def list_nodes(self):
        return self.nodes

    def get_node_info(self, node):
        return DataCollector.get_from_node(node)

    def node_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

        return None
