from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from config import Base

class PlaneFrame(Base):
    __tablename__ ="frame"
    
    id = Column(Integer, primary_key = True, index=True)
    icao = Column(String(4))
    speed = Column(Float)
    lat = Column(Float)
    lon = Column(Float)
    alt = Column(Integer)
    timestamp = Column(DateTime, server_default = func.now())

    class Config:
        from_attributes = True 
