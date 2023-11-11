from typing import List
from pydantic import TypeAdapter

from app.featureflags.manager import unleash_manager
from . import schemas

product_data = [
    {"id": "P-123", "status": "Active"},
    {"id": "P-456", "status": "Inactive"}
]

product_data_with_price = [
    {"id": "P-123", "status": "Active", "price": {"amount": 100, "currency": "CZK"}},
    {"id": "P-456", "status": "Inactive", "price": {"amount": 120, "currency": "CZK"}}
]


async def list_products():
    if unleash_manager.unleash.is_enabled("product_with_price"):
        return TypeAdapter(List[schemas.Product]).validate_python(product_data_with_price)
    else:
        return TypeAdapter(List[schemas.Product]).validate_python(product_data)
