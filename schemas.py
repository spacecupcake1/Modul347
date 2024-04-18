from datetime import datetime
from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    director: str
    year: int
    description: str = None

class MovieCreate(MovieBase):
    pass

class MovieUpdate(MovieBase):
    pass

class MovieInDBBase(MovieBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class Movie(MovieInDBBase):
    pass
