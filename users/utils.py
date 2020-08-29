from datetime import timedelta

import jwt
from passlib.context import CryptContext

from common import settings
from common import utils as common_utils

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_jwt_token(
    data, token_type="access", expires_delta: timedelta = timedelta(minutes=15)
):
    to_encode = data.copy()
    expire = common_utils.now() + expires_delta
    to_encode.update({"exp": expire, "token_type": token_type})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def user_add_related(user):
    from offers import models

    user.offers = await models.Offer.query.where(
        models.Offer.user_id == user.id
    ).gino.all()
    return user
