from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schema, auth
from router import auth, movies, comments,ratings
from database import SessionLocal, engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(ratings.router, prefix="/ratings", tags=["ratings"])

