from typing import List
from typing import Optional
from pydantic import BaseModel


class SearchItem(BaseModel):
    id: int
    title: str
    description: Optional[str]


class SearchItems(BaseModel):
    items: List[SearchItem]


class StatusResponse(BaseModel):
    status: str
    details: Optional[str]


class Config(BaseModel):
    mongodb_login: str
    mongodb_password: str
    mongodb_host: str
    mongodb_port: int
    mongodb_db: str
    mongodb_post_collection: str
    mongodb_event_collection: str
