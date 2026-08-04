from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)
db = SessionLocal()

nodes_data = [
    {"id": 1,  "name": "Main Block",           "type": "junction", "x": 0,  "y": 0,  "floor": 1},
    {"id": 2,  "name": "Mechanical Block",     "type": "room",     "x": 10, "y": 0,  "floor": 1},
    {"id": 3,  "name": "Canteen",              "type": "room",     "x": 20, "y": 0,  "floor": 1},
    {"id": 4,  "name": "CSE Department",       "type": "room",     "x": 0,  "y": 10, "floor": 1},
    {"id": 5,  "name": "CSE AIML Department",  "type": "room",     "x": 10, "y": 10, "floor": 1},
    {"id": 6,  "name": "IS Department",        "type": "room",     "x": 20, "y": 10, "floor": 1},
    {"id": 7,  "name": "AI ML Lab 1",          "type": "room",     "x": 0,  "y": 20, "floor": 1},
    {"id": 8,  "name": "AI ML Lab 2",          "type": "room",     "x": 10, "y": 20, "floor": 1},
    {"id": 9,  "name": "AI ML Lab 3",          "type": "room",     "x": 20, "y": 20, "floor": 1},
    {"id": 10, "name": "2nd Year Classroom",   "type": "room",     "x": 0,  "y": 30, "floor": 1},
    {"id": 11, "name": "3rd Year Classroom",   "type": "room",     "x": 10, "y": 30, "floor": 1},
    {"id": 12, "name": "4th Year Classroom",   "type": "room",     "x": 20, "y": 30, "floor": 1},
]
for n in nodes_data:
    db.add(models.Node(**n))

edges_data = [
    {"from_node": 1, "to_node": 2, "weight": 10},
    {"from_node": 2, "to_node": 3, "weight": 10},
    {"from_node": 1, "to_node": 4, "weight": 10},
    {"from_node": 2, "to_node": 5, "weight": 10},
    {"from_node": 3, "to_node": 6, "weight": 10},
    {"from_node": 4, "to_node": 5, "weight": 10},
    {"from_node": 5, "to_node": 6, "weight": 10},
    {"from_node": 4, "to_node": 7, "weight": 10},
    {"from_node": 5, "to_node": 8, "weight": 10},
    {"from_node": 6, "to_node": 9, "weight": 10},
    {"from_node": 7, "to_node": 8, "weight": 10},
    {"from_node": 8, "to_node": 9, "weight": 10},
    {"from_node": 7, "to_node": 10, "weight": 10},
    {"from_node": 8, "to_node": 11, "weight": 10},
    {"from_node": 9, "to_node": 12, "weight": 10},
    {"from_node": 10, "to_node": 11, "weight": 10},
    {"from_node": 11, "to_node": 12, "weight": 10},
]
for e in edges_data:
    db.add(models.Edge(**e))

db.commit()
print("Database seeded successfully!")