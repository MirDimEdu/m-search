from fastapi import APIRouter
from fastapi import responses

from .. import models
from .. import storage
from .. import db


router = APIRouter(prefix='/api/post')


def get_storage() -> storage.Storage:
    return storage.Storage(db.get_post_collection())


@router.get(
    '/{id:int}',
    response_model=models.SearchItem,
    responses={
        404: {
            'model': models.StatusResponse
        }
    }
)
async def get(id: int):
    try:
        storage = get_storage()
        item = await storage.get(id)
        if item:
            return item
    except Exception as e:
        print(f'Failed to get post {id}: {repr(e)}')
    not_found = models.StatusResponse(
        status='NOT_FOUND',
        details=f'No item with id = {id}',
    )
    return responses.JSONResponse(status_code=404, content=not_found.dict())


@router.get('/search', response_model=models.SearchItems)
async def search(text: str):
    try:
        storage = get_storage()
        items = await storage.search(text)
        return models.SearchItems(items=items)
    except Exception as e:
        print(f'Failed to search posts: {repr(e)}')
    return models.SearchItems(items=[])


@router.put('', response_model=models.StatusResponse)
async def put(item: models.SearchItem):
    try:
        storage = get_storage()
        await storage.put(item)
        return models.StatusResponse(
            status='OK'
        )
    except Exception as e:
        print(f'Failed to put item {item.id}: {repr(e)}')
    return models.StatusResponse(
        status='ERROR'
    )


@router.delete('/{id:int}', response_model=models.StatusResponse)
async def delete(id: int):
    try:
        storage = get_storage()
        await storage.delete(id)
        return models.StatusResponse(
            status='OK'
        )
    except Exception as e:
        print(f'Failed to delete item {id}: {repr(e)}')
    return models.StatusResponse(
        status='ERROR'
    )
