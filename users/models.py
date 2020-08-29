from common.models import Column, Integer, String, db
from users.utils import get_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String)
    hashed_password = Column(String)

    @classmethod
    async def create(cls, **kwargs):
        kwargs["hashed_password"] = get_password_hash(kwargs.pop("password", None))
        return await super().create(**kwargs)
