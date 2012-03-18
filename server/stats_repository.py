import datetime

from pymongo import Connection
connection = Connection('127.0.0.1', 27017)
db = connection.seamon

class StatsRepository(object):
    @staticmethod
    def save_for_node(node_id, data):
        data["node_id"] = node_id
        data["timestamp"] = datetime.datetime.now()
        db.nodes.data.insert(data)

    @staticmethod
    def get_for_node(node_id):
        return list(db.nodes.data.find({"node_id":node_id}, {"_id":0}))
