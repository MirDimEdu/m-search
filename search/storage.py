from typing import Optional
from typing import List

from . import models


class Storage:
    def __init__(self, collection):
        self._collection = collection

    async def get(self, id: int) -> Optional[models.SearchItem]:
        data: dict = await self._collection.find_one({
            'id': id,
        })
        if not data:
            return None
        data.pop('_id')
        return models.SearchItem(**data)

    async def put(self, item: models.SearchItem):
        await self._collection.find_one_and_update(
            {'id': item.id},
            {'$setOnInsert': item.dict()},
            new=True,
            upsert=True,
        )

    async def delete(self, id: int):
        await self._collection.delete_many({
            'id': id
        })

    async def search(self, text: str) -> List[models.SearchItem]:
        cursor = self._collection.find(
            {
                '$text': {
                    '$search': text
                }
            }
        )
        result = []
        async for item in cursor:
            item.pop('_id')
            result.append(models.SearchItem(**item))
        return result
