from common.app import get_app

from .views import router

app = get_app("Users", routers=[router])
