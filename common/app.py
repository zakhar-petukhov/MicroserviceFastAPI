import functools
import io

import yaml
from fastapi import FastAPI, Response

from common import settings
from common.db import db


def get_app(title, routers=[], mounts={}):
    main_app = FastAPI(title=title, version="1.0", docs_url="/", redoc_url="/redoc")

    @main_app.get("/openapi.yaml", include_in_schema=False)
    @functools.lru_cache()
    def read_openapi_yaml():
        openapi_json = main_app.openapi()
        yaml_s = io.StringIO()
        yaml.dump(openapi_json, yaml_s, sort_keys=False, allow_unicode=True)
        return Response(yaml_s.getvalue(), media_type="text/yaml")

    for router in routers:
        prefix = ""
        router_to_include = router
        if isinstance(router, dict):
            router_to_include = router["router"]
            prefix = router["prefix"]
        main_app.include_router(router_to_include, prefix=prefix)

    for path, app in mounts.items():
        main_app.mount(path, app)

    @main_app.on_event("startup")
    async def startup():
        await db.set_bind(settings.CONNECTION_URL)

    return main_app
