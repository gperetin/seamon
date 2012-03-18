class Node(object):
    def __init__(self, **kwargs):
        for k,v in kwargs.iteritems():
            setattr(self,k,v)

    def full_path(self):
        return "http://%s:%s" % (self.ip_address, self.port)
