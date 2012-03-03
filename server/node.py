class Node(object):
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def full_path(self):
        return "http://%s:%s" % (self.ip_address, self.port)
