#!/usr/bin/python3
"""defines the state class and base used by SQLAlchemy models"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.dec,arative import declarative_base

Base = declarative_base()

class State(Base):
    """Maps to the MYSQL table states"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=Flase)
