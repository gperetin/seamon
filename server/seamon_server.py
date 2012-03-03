class SeamonServer(object):
    nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def list_nodes(self):
        return self.nodes
