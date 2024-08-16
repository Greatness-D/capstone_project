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