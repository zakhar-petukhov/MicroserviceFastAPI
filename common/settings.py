from datetime import timedelta

from starlette.config import Config

config = Config(".env")

# In format postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
CONNECTION_URL = config("CONNECTION_URL", cast=str)

# JWT
SECRET_KEY = config("JWT_SECRET_KEY", cast=str)
ACCESS_TOKEN_EXPIRE_MINUTES = timedelta(
    minutes=config("JWT_EXPIRE", cast=int, default=15)
)
REFRESH_TOKEN_EXPIRE_MINUTES = timedelta(
    minutes=config("JWT_REFRESH_EXPIRE", cast=int, default=60 * 24 * 7)
)

ALGORITHM = config("JWT_ALGORITHM", cast=str, default="HS256")


# Apps

APPS = ["users", "offers"]
