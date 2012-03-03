from db.session import session
from db import tables
from node import Node

class NodeRepository(object):
    @staticmethod
    def save(node):
        session.add(node)
        session.commit()

    @staticmethod
    def all():
        return session.query(Node).all()

    @staticmethod
    def by_name(node_name):
        return session.query(Node).filter(Node.name == node_name).one()
