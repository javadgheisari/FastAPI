from typing import Union
from fastapi import FastAPI, Query, status
from pydantic import BaseModel, EmailStr
app = FastAPI()

class Item(BaseModel):
    name: str
    price: int
    is_offer: Union[bool, None] = None

class UserIn(BaseModel):
    username : str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    username: str
    email: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = Query(None, max_length=32)):
    return {"item_id": item_id, "name": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.post("items/create", status_code=status.HTTP_201_CREATED)
def post_item(item: Item):
    return f'{item.name} is {item.price} $'

@app.post('/user', response_model=UserOut)
def user(user: UserIn):
    return user