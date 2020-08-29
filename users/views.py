from fastapi import APIRouter, HTTPException

from common import settings
from common import utils as common_utils

from . import models, schemes, utils

router = APIRouter()


@router.post("/registry", status_code=201, response_model=schemes.DisplayUser)
async def register_user(user: schemes.CreateUser):
    with common_utils.insert_model():
        return await utils.user_add_related(await models.User.create(**user.dict()))


@router.post("/auth", response_model=schemes.AuthResponse)
async def authenticate_user(user_scheme: schemes.AuthUser):
    user = await models.User.query.where(
        models.User.username == user_scheme.username
    ).gino.first()
    if not user or not utils.verify_password(
        user_scheme.password, user.hashed_password
    ):
        raise HTTPException(401, detail="Unauthorized")
    token_data = {"sub": user.username}
    return {
        "id": user.id,
        "access_token": utils.get_jwt_token(
            data=token_data,
            token_type="access",
            expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
        "refresh_token": utils.get_jwt_token(
            data=token_data,
            token_type="refresh",
            expires_delta=settings.REFRESH_TOKEN_EXPIRE_MINUTES,
        ),
    }


@router.get("/{user_id}", response_model=schemes.DisplayUser)
async def get_user_data(user_id: int):
    return await utils.user_add_related(
        await common_utils.get_model(models.User, user_id)
    )
