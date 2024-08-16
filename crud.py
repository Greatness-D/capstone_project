from fastapi import Depends, HTTPException


from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


import models, schema, auth
from database import get_db

def create_user(db: Session, username: str, hashed_password: str):
    db_user = models.User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_movie(db: Session, id: int):
    return db.query(models.Movie).filter(models.Movie.id == id).first()

def get_movies(db: Session, user_id: int = None, offset: int = 0, limit: int = 10):
    return db.query(models.Movie).filter(models.Movie.id == user_id).offset(offset).limit(limit).all()

def create_movie(db: Session, movie: schema.MovieCreate, user_id: int = None):
    db_movie = models.Movie(**movie.model_dump())
    user_id=user_id
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie( db: Session, movie: schema.MovieUpdate, user_id: int = None):
    db_movie = db.query(models.Movie).filter(models.Movie.id == user_id).first()
    user_id=user_id
    if db_movie is None :
      return None
    movie_dict = movie.dict(exclude_unset=True)
    for k, v in movie_dict.items():
      setattr(db_movie, k, v)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie







