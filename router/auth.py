
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import crud, schema, models, auth, database
from database import SessionLocal, engine, Base, get_db


from auth import pwd_context, oauth2_scheme, verify_password, create_access_token, get_current_user,authenticate_user

from typing import Optional

router = APIRouter()


@router.post("/signup", response_model=schema.User)
def signup(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    hashed_password = pwd_context.hash(user.password)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    return crud.create_user(db=db, username=user.username, hashed_password=hashed_password)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# @router.get("/current_user")
# def get_current_user(token: str = Depends(auth.oauth2_scheme)):
#     user = auth.get_current_user(token)  # Retrieve the user based on the token
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user


# def authenticate_user(db: Session, username: str, password: str):
#   user = crud.get_user_by_username(db, username)
#   if not user or not verify_password(password, user.hashed_password):
#     return False
#   return user