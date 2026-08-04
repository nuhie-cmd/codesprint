from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./nav.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_nodes():
    import models
    db = SessionLocal()
    result = [
        {"id": n.id, "name": n.name, "type": n.type,
         "x": n.x, "y": n.y, "floor": n.floor}
        for n in db.query(models.Node).all()
    ]
    db.close()
    return result

def get_edges():
    import models
    db = SessionLocal()
    result = [
        {"id": e.id, "from_node": e.from_node,
         "to_node": e.to_node, "weight": e.weight}
        for e in db.query(models.Edge).all()
    ]
    db.close()
    return result