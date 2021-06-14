from fastapi import FastAPI

from .api import post
from .api import event
from . import config_manager
from . import db


app = FastAPI()


@app.on_event('startup')
async def on_startup():
    await config_manager.config_manager.update()
    await db.create_indexes()


app.include_router(post.router)
app.include_router(event.router)
