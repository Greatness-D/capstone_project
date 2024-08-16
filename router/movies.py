from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schema, crud, auth
from auth import get_current_user
from typing import List
from database import get_db

router = APIRouter()

@router.get("/movies/{movie_id}")
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.get("/movies/")
def read_movies( db: Session = Depends(get_db), user: schema.User = Depends(get_current_user), offset: int = 0, limit: int = 10):
    db_movies = crud.get_movies(db, user_id=user.id, offset=offset, limit=limit)
    return {'message': 'success', 'data': db_movies}

@router.post("/movies")
def create_movie(payload: schema.MovieCreate, user: schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_movies = crud.create_movie(db, payload, user_id=user.id)
    return{'message': 'success'}


@router.put("/movies/")
def update_movie(movie: schema.MovieUpdate, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    db_movie = crud.update_movie(db=db,movie=movie, user_id=current_user.id)
    
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {'message': 'success', 'data': db_movie}
