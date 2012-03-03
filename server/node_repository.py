class NodeRepository(object):
    nodes = []

    @staticmethod
    def save(node):
        NodeRepository.nodes.append(node)

    @staticmethod
    def all():
        return NodeRepository.nodes

    @staticmethod
    def by_name(node_name):
        for node in NodeRepository.nodes:
            if node.name == node_name:
                return node
        
        return None
