from fastapi import FastAPI, HTTPException, Path, Query
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    firstname = Column('FirstName', String)

    def __init__(self, id, firstname):
        self.firstname = firstname
        self.id = id

    def __repr__(self):
        return f"{self.firstname}"

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(1, 'Bill')

session.add(p1)

session.commit()


