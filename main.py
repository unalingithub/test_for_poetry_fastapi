from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/district/{type}")
def district(type: str):
    return {"district的type是 ": type}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True) 