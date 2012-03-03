from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapper

from server.node import Node

metadata = MetaData()

nodes = Table('nodes', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(100)),
              Column('ip_address', String(15)),
              Column('port', Integer)
             )

mapper(Node, nodes)
