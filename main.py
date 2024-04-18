from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from repository import get_movies, create_movie, get_movie, update_movie, delete_movie
from schemas import MovieCreate, MovieUpdate
from dotenv import load_dotenv
import os

load_dotenv()

# Configure SQLAlchemy engine and session
engine = create_engine(os.getenv('DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False)
SessionLocal.configure(bind=engine)

# Create tables if not exists
Base.metadata.create_all(bind=engine)

# Example usage of repository functions
def example_usage():
    # Get all movies
    movies = get_movies(SessionLocal())
    print(movies)

    # Create a new movie
    movie_data = {"title": "New Movie", "director": "Director", "year": 2022}
    new_movie = create_movie(SessionLocal(), MovieCreate(**movie_data))
    print(new_movie)

    # Update an existing movie
    movie_id = 1
    update_data = {"title": "Updated Title", "director": "Director", "year": 2022}
    updated_movie = update_movie(SessionLocal(), movie_id, MovieUpdate(**update_data))
    print(updated_movie)

    # Delete a movie
    """ delete_movie_id = 2
    deleted_movie = delete_movie(SessionLocal(), delete_movie_id)
    print(deleted_movie) """

# Example usage of repository functions
example_usage()
