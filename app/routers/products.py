from fastapi import APIRouter
from fastapi import HTTPException
from ..domain.products import schemas, service

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("/", response_model=list[schemas.Product], status_code=200)
async def list_products():
    products = await service.list_products()
    if products is None:
        raise HTTPException(status_code=404, detail="Products not found.")
    return products
