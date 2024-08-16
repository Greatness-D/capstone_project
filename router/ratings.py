
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schema, crud, auth, database
from typing import List

router = APIRouter()

@router.post("/movies/{movie_id}/ratings/", response_model=schema.Rating)
def rate_movie(movie_id: int, rating: schema.RatingCreate, db: Session = Depends(database.get_db), current_user: schema.User = Depends(auth.get_current_user)):
    db_movie = crud.get_movie(db=db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return crud.create_rating(db=db, rating=rating, movie_id=movie_id, user_id=current_user.id)

@router.get("/movies/{movie_id}/ratings/", response_model=List[schema.Rating])
def read_ratings(movie_id: int, db: Session = Depends(database.get_db)):
    return crud.get_ratings(db=db, movie_id=movie_id)
