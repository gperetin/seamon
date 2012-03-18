from fabric.api import local

def test():
    local("nosetests --rednose")


