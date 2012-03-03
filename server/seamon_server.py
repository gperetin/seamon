from data_collector import DataCollector

class SeamonServer(object):
    nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def list_nodes(self):
        return self.nodes

    def get_data_from_nodes(self):
        for node in self.nodes:
            DataCollector.get_from_node(node)
