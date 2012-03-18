import unittest, datetime

from stats_repository import StatsRepository
from node import Node

from pymongo import Connection
connection = Connection('127.0.0.1', 27017)
db = connection.seamon

class StatsRepositoryTest(unittest.TestCase):
    def setUp(self):
        db.nodes.remove()
        db.nodes.data.remove()

    def test_saves_data_for_node(self):
        data = {
            "disk": [
                {
                    "available": 4028460,
                    "used": 0,
                    "name": "/dev",
                    "mount": "/dev",
                    "percent": "0%",
                    "size": 4028460
                },
            ],
            "uptime": 46748.41,
            "hostname": "haxbox"
        }

        node = Node(name="prvi", ip_address="1231123", port=1232)
        # TODO: fix this, implement IDs in mongo or use name as key
        StatsRepository.save_for_node(1, data, datetime.datetime.now())

        stats = StatsRepository.get_for_node(1)
        self.assertEquals(4028460, stats[0]["disk"][0]["available"])
        self.assertEquals("haxbox", stats[0]["hostname"])

    def test_get_cpu_stats_returns_cpu_data_for_all_nodes(self):
        n1_data = {"cpu":{"load_1":0.12, "load_5":0.16, "load_15":0.2}}
        n2_data = {"cpu":{"load_1":0.12, "load_5":0.16, "load_15":0.2}}
        StatsRepository.save_for_node(1, n1_data, datetime.datetime.now())
        StatsRepository.save_for_node(2, n2_data, datetime.datetime.now())

        data = StatsRepository.get_cpu_stats()
        self.assertEquals(data[0]["cpu"], n1_data["cpu"])
        self.assertEquals(data[1]["cpu"], n2_data["cpu"])
