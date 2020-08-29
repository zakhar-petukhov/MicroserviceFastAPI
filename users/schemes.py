from typing import List

from pydantic import EmailStr

from common.schemes import BaseModel
from offers.schemes import Offer


class BaseUser(BaseModel):
    email: EmailStr
    username: str


class CreateUser(BaseUser):
    password: str


class DisplayUser(BaseUser):
    id: int
    offers: List[Offer]


class AuthUser(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    id: int
    access_token: str
    refresh_token: str
