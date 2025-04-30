from typing import Union

from fastapi import HTTPException, Depends

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from typing_extensions import Annotated

from app.schemas.item import Item

app = APIRouter(prefix="/item", tags=["item"])

items = {"foo":"the foo wrestlers"}


fake_items_db =[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

class CommonQueryParams:
    def __init__(self, q:Union[str,None] =None,skip:int =0,limit:int =100):
        self.q = q
        self.skip = skip
        self.limit = limit



@app.get("/items")
async def read_items(commons:Annotated[CommonQueryParams,Depends(CommonQueryParams)]):
    response ={}
    if commons.q:
        response.update({"q":commons.q})

    items = fake_items_db[commons.skip:commons.skip + commons.limit]
    response.update({"items":items})
    return response







@app.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id":items[item_id]}


@app.put("/{item_id}")
async def update_item(item_id: str, item: Item):
    json_compatible_item_data= jsonable_encoder(item)
    print(json_compatible_item_data)
