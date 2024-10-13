from typing import Union
from sqlalchemy import select

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from models import Product
from database import get_session

app = FastAPI() 

templates = Jinja2Templates(directory='../templates')

@app.get("/items", response_class=HTMLResponse)
async def get_catalog(request: Request):
    session = get_session()
    products = await session.execute(select(Product))
    # print(list(products))
    goods = []
    for p in products:
        print(p[0])
        goods.append(p[0])
    print("goods", goods)

    return templates.TemplateResponse(request=request, name="catalog.html", context={"products": goods})

@app.get("/items/{id}", response_class=HTMLResponse)
async def get_item(request: Request, id: str):
    session = get_session()
    product = await session.execute(select(Product).where(Product.id==int(id)))
    product = product.first()[0]
    return templates.TemplateResponse(
        request=request, name="item.html", context={"product": product}
    )

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}