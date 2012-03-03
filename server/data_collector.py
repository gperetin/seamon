import requests

class DataCollector(object):
    @staticmethod
    def get_node_info(node):
        return requests.get(node.full_path())
