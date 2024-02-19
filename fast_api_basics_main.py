from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

products = []


class BaseProduct(BaseModel):
    name: str
    price: float


class Product(BaseProduct):
    id: int


class ResponseProduct(BaseProduct):
    pass


@app.get("/", response_model=list[ResponseProduct], status_code=200)
async def get_products():
    return products


@app.get("/products/{product_id}", status_code=200)
async def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Produkt wurde nicht gefunden")


@app.put("/products/{product_id}", status_code=200)
async def update_product(product_id: int, product: Product):
    for index, p in enumerate(products):
        if p.id == product_id:
            products[index] = product
            return {"success": "Produkt geupdated"}
    raise HTTPException(status_code=404, detail="Produkt wurde nicht gefunden")


@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int):
    for index, p in enumerate(products):
        if p.id == product_id:
            products.pop(index)
            return {"success": "Produkt gelöscht"}
    raise HTTPException(status_code=404, detail="Produkt wurde nicht gefunden")


@app.post("/products", status_code=201)
async def create_product(product: Product):
    products.append(product)
    return {"success": "Produkt erstellt"}
