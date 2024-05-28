from fastapi import APIRouter
from ..config import AppProperties

from . import root, products

router = APIRouter()
config = AppProperties()


def effective_routes():
    router.include_router(root.router, prefix=config.ROUTE_PREFIX_V1)
    router.include_router(products.router, prefix=config.ROUTE_PREFIX_V1)


effective_routes()
