from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schema, crud, auth
from auth import get_current_user
from typing import List
from database import get_db

router = APIRouter()


@router.post("/movies/{movie_id}/comments", response_model=schema.Comment)
def add_comment(movie_id: int, comment: schema.CommentCreate, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    comment.movie_id = movie_id
    return crud.create_comment(db=db, comment=comment, user_id=current_user.id)


@router.get("/movies/{movie_id}/comments", response_model=List[schema.Comment])
def view_comments(movie_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_by_movie(db=db, movie_id=movie_id)


@router.post("/comments/{comment_id}/replies", response_model=schema.Comment)
def add_reply(comment_id: int, comment: schema.CommentCreate, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    comment.parent_comment_id = comment_id
    return crud.create_comment(db=db, comment=comment, user_id=current_user.id)


