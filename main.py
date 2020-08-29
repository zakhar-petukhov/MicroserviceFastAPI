from common.app import get_app
from offers import router as offers_router
from users import router as users_router

app = get_app(
    "Web app",
    routers=[
        {"router": users_router, "prefix": "/user"},
        {"router": offers_router, "prefix": "/offer"},
    ],
)
