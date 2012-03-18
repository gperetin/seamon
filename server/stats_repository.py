from pymongo import Connection
connection = Connection('127.0.0.1', 27017)
db = connection.seamon

class StatsRepository(object):
    @staticmethod
    def save_for_node(node_id, data, timestamp):
        data["node_id"] = node_id
        data["timestamp"] = timestamp
        db.nodes.data.insert(data)

    @staticmethod
    def get_for_node(node_id):
        return list(db.nodes.data.find({"node_id":node_id}, {"_id":0}))

    @staticmethod
    def get_cpu_stats():
        stats = db.nodes.data.find({"cpu":{"$exists":True}}, {
            "cpu":1, "timestamp":1, "node_id":1, "_id":0})
        return list(stats)
