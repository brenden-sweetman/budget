import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

#create declarative_base instance
Base = declarative_base()
engine = create_engine('sqlite:///test.db')
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Add table classes
class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(255), nullable = False)
    category = Column(String(255))
    cost = Column(Float())
    notes = Column(String(1024))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, onupdate=datetime.datetime.utcnow)

class NetBudget(Base):
    __tablename__ = 'net_budget'
    category = Column(String(255),primary_key=True)
    net_value = Column(Float())
    created = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, onupdate=datetime.datetime.utcnow)

Base.metadata.create_all(engine)
