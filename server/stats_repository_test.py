import unittest

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

        node = Node("prvi", "1231123", 1232)
        StatsRepository.save_for_node(1, data)

        stats = StatsRepository.get_for_node(1)
        self.assertEquals(4028460, stats[0]["disk"][0]["available"])
        self.assertEquals("haxbox", stats[0]["hostname"])
