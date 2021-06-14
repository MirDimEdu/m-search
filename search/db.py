from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import TEXT

from . import models
from . import config_manager


def get_client(config: models.Config):
    client = AsyncIOMotorClient(
        'mongodb://{}:{}@{}:{}/{}'.format(
            config.mongodb_login,
            config.mongodb_password,
            config.mongodb_host,
            config.mongodb_port,
            config.mongodb_db
        )
    )
    return client


async def create_indexes():
    config = config_manager.config_manager.get()
    client = get_client(config)
    db = client[config.mongodb_db]
    collections = (
        config.mongodb_post_collection,
        config.mongodb_event_collection,
    )
    for collection_name in collections:
        collection = db[collection_name]
        await collection.create_index([
            ('title', TEXT),
            ('description', TEXT),
        ])
        await collection.create_index('id', unique=True)


def get_post_collection():
    config = config_manager.config_manager.get()
    client = get_client(config)
    db = client[config.mongodb_db]
    return db[config.mongodb_post_collection]


def get_even_collection():
    config = config_manager.config_manager.get()
    client = get_client(config)
    db = client[config.mongodb_db]
    return db[config.mongodb_event_collection]
