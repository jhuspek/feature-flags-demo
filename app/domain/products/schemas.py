from typing import Optional

from pydantic import BaseModel


class Price(BaseModel):
    amount: int
    currency: str


class Product(BaseModel):
    id: str
    status: str
    price: Optional[Price] = None
