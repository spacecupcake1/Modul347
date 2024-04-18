from sqlalchemy.orm import Session
from models import Movie
from datetime import datetime
from schemas import MovieCreate, MovieUpdate

def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, movie: MovieUpdate):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    for var, value in vars(movie).items():
        if value is not None:
            setattr(db_movie, var, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    db.delete(db_movie)
    db.commit()
    return db_movie
