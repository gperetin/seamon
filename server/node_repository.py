from node import Node

from pymongo import Connection
# TODO: extract to config
connection = Connection('127.0.0.1', 27017)
db = connection.seamon

class NodeRepository(object):
    @staticmethod
    def save(node):
        db.nodes.insert({
            "name":node.name,
            "ip_address":node.ip_address,
            "port":node.port
        })

    @staticmethod
    def all():
        res = db.nodes.find({}, {"_id":0})
        node_list = [ Node(**vals) for vals in res ]
        return node_list

    @staticmethod
    def by_name(node_name):
        res = db.nodes.find_one({"name":node_name})
        return Node(**res)
