from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Food(Base):
    __tablename__ = "foods"

    id         = Column(Integer, primary_key=True, index=True)
    food_name  = Column(String(200), index=True)
    category   = Column(String(100))
    serving_size = Column(String(50))
    calories   = Column(Float)
    carbs      = Column(Float)
    protein    = Column(Float)
    fat        = Column(Float)
    sodium     = Column(Float)
    sugar      = Column(Float)
    fiber      = Column(Float)


class Record(Base):
    __tablename__ = "records"

    id        = Column(Integer, primary_key=True, index=True)
    food_name = Column(String(200))
    calories  = Column(Float)
    carbs     = Column(Float)
    protein   = Column(Float)
    fat       = Column(Float)
    sodium    = Column(Float)
    sugar     = Column(Float)
    fiber     = Column(Float)
    date      = Column(DateTime, server_default=func.now())