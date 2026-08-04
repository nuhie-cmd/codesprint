from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))              # e.g. "Junction A", "Lab 3 Door"
    type = Column(String(20))               # room / junction / stairs / lift
    x = Column(Float)
    y = Column(Float)
    floor = Column(Integer, default=0)

    room = relationship("Room", back_populates="node", uselist=False)

class Edge(Base):
    __tablename__ = "edges"
    id = Column(Integer, primary_key=True, index=True)
    from_node = Column(Integer, ForeignKey("nodes.id"), index=True)
    to_node = Column(Integer, ForeignKey("nodes.id"), index=True)
    weight = Column(Float)   # distance in meters

class Faculty(Base):
    __tablename__ = "faculty"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    department = Column(String(100))

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    node_id = Column(Integer, ForeignKey("nodes.id"), unique=True, index=True)
    room_number = Column(String(20))
    faculty_id = Column(Integer, ForeignKey("faculty.id"), nullable=True)
    timings = Column(String(50), nullable=True)

    node = relationship("Node", back_populates="room")
    faculty = relationship("Faculty")

class RouteLog(Base):
    __tablename__ = "route_logs"
    id = Column(Integer, primary_key=True, index=True)
    from_node = Column(Integer, ForeignKey("nodes.id"))
    to_node = Column(Integer, ForeignKey("nodes.id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())