from pydantic import BaseModel
from typing import List, Optional, Union


class UserBase(BaseModel):
  username: str
  

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int

  class Config:
    orm_mode = True

class MovieBase(BaseModel):
  title: str
  description: str

class MovieCreate(MovieBase):
  pass
 

class MovieUpdate(MovieBase):
  title: Optional[str] = None  # Allow updating only title if provided
  description: Optional[str] = None 

class MovieDelete(MovieBase):
  pass

class Movie(MovieBase):
  id: int
  user_id: int

  class Config:
    orm_mode = True


class RatingBase(BaseModel):
  movie_id: int
  user_id: int
  rating: float


class RatingCreate(RatingBase):
  pass

class Rating(RatingBase):
  id: int
  user_id: int
  

  class Config:
    orm_mode = True

class CommentBase(BaseModel):
  content: str


class CommentCreate(CommentBase):
  movie_id: int
  parent_comment_id: Optional[int] = None

class Comment(CommentBase):
  id: int
  movie_id: int
  user_id: int
  parent_comment_id: Optional[int] = None
  replies: List["Comment"] = []

  class Config:
    orm_mode = True

class Token(BaseModel):
  access_token: str
  token_type: str


class TokenData(BaseModel):
  username: Union[str, None] = None
   
class UserInDB(User):
  hashed_password: str