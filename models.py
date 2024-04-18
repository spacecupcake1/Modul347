from sqlalchemy import Column, Integer, String
from database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    director = Column(String(50))
    year = Column(Integer)
    description = Column(String(500), server_default=None, nullable=True)
