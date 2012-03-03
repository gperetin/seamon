class Node(object):
    def __init__(self, name, ip_address, port):
        self.name = name
        self.ip_address = ip_address
        self.port = port

    def full_path(self):
        return "http://%s:%s" % (self.ip_address, self.port)
