def create_database():
    local("touch db/seamon.db")

def create_tables():
    from db.session import engine
    from tables import metadata
    metadata.create_all(engine)
