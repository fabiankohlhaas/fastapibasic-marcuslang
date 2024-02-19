from pydantic import BaseModel, validator
from typing import Optional
from enum import Enum


class ProductCategory(Enum):
    FOOD = "food"
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"


class Product(BaseModel):
    id: int
    name: str = "defaultproduct"
    price: float
    tags: list[str] = []
    description: Optional[str] = None
    category: ProductCategory

    @validator("name")
    def name_be_best_titlecase(cls, v):
        if not v:
            raise ValueError("Name ist required")
        if not v[0].isupper():
            raise ValueError("Name muss titlecase sein")
        return v


product = Product(id=1, name="Apfel", price=1.99, category=ProductCategory.FOOD)
print(product)
product_dict = product.dict()


product2 = Product(**product_dict)
print(product2)
