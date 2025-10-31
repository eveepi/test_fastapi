"""The main FastAPI application."""

# pylint: disable=missing-function-docstring

import logging
from typing import Annotated

from fastapi import FastAPI, HTTPException, Header, Path, Query
from pydantic import BaseModel
import uvicorn

from models.house import House, my_houses

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def root():
    """hello world"""
    return {"message": "Hello World"}


@app.get("/houses")
def list_houses() -> list[House]:
    return []


@app.get("/houses/{house_id}")
def get_house(
    house_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
) -> House:
    try:
        return my_houses[house_id]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Item not found") from exc


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
