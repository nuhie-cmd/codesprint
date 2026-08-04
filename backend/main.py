import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "algorithms"))

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import Base, engine, get_db, get_nodes, get_edges
from dijikstra import build_graph, shortest_path
from astar import astar
from room_lookup import get_node

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is working!"}

@app.get("/nodes")
def list_nodes(db: Session = Depends(get_db)):
    nodes = db.query(models.Node).all()
    return [
        {"id": n.id, "name": n.name, "type": n.type,
         "x": n.x, "y": n.y, "floor": n.floor}
        for n in nodes
    ]

@app.get("/route")
def get_route(from_id: int, to_id: int, algo: str = "dijkstra", db: Session = Depends(get_db)):
    nodes = get_nodes()
    edges = get_edges()
    node_ids = [n["id"] for n in nodes]
    graph = build_graph(node_ids, edges)

    if algo == "astar":
        coordinates = {n["id"]: (n["x"], n["y"]) for n in nodes}
        path, cost = astar(graph, coordinates, from_id, to_id)
    else:
        path, cost = shortest_path(graph, from_id, to_id)

    db.add(models.RouteLog(from_node=from_id, to_node=to_id))
    db.commit()

    return {"path": path, "cost": cost, "algorithm": algo}

@app.get("/route-by-name")
def get_route_by_name(start: str, end: str, algo: str = "dijkstra", db: Session = Depends(get_db)):
    start_id = get_node(start)
    end_id = get_node(end)
    if start_id is None or end_id is None:
        return {"error": "Invalid room name(s)"}
    return get_route(from_id=start_id, to_id=end_id, algo=algo, db=db)
    