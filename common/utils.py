import importlib
from contextlib import contextmanager
from datetime import datetime, timezone

import asyncpg
from fastapi import HTTPException

from . import settings


def now():
    return datetime.now(timezone.utc)


def get_target_metadata():
    # Load all apps models
    for app in settings.APPS:
        module = importlib.import_module(f"{app}.models")
    # Any module's db object will contain all models
    return module.db


@contextmanager
def insert_model():
    try:
        yield
    except asyncpg.exceptions.IntegrityConstraintViolationError as e:
        raise HTTPException(422, e.message)


async def get_model(model, model_id):
    model_obj = await model.get(model_id)
    if model_obj is None:
        raise HTTPException(404, detail="Not found")
    return model_obj
