import requests

class DataCollector(object):
    @staticmethod
    def get_from_node(node):
        return requests.get(node.full_path())
