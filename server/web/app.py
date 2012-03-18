from flask import Flask
app = Flask(__name__)

import json

from server.seamon_server import SeamonServer
from server.stats_repository import StatsRepository

@app.route("/")
def index():
    return "list of all registered nodes"

@app.route("/nodes", methods=['POST'])
def add_node():
    node_data = json.loads(request.data)
    SeamonServer.add_node(node_data)

@app.route("/stats/cpu", methods=['GET'])
def cpu_stats():
    stats = StatsRepository.get_cpu_stats()
    for s in stats:
        s["timestamp"] = s["timestamp"].isoformat()
    return json.dumps(stats)

@app.route("/stats/memory", methods=['GET'])
def memory_stats():
    stats = StatsRepository.get_memory_stats()
    for s in stats:
        s["timestamp"] = s["timestamp"].isoformat()
    return json.dumps(stats)

if __name__ == "__main__":
    app.run(debug=True)
