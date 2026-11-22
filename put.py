
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

cart = {}


class CartItem(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int


# 1. Add product to cart
@app.post("/cart/items")
def add_item(item: CartItem):

    cart[item.product_id] = item.model_dump()

    return {
        "message": "Product added to cart",
        "item": cart[item.product_id]
    }


# 2. Get all cart items
@app.get("/cart")
def get_cart():

    return cart


# 3. Replace complete cart item
@app.put("/cart/items/{product_id}")
def update_item(product_id: int, item: CartItem):

    if product_id not in cart:
        raise HTTPException(404, "Product not found")

    cart[product_id] = item.model_dump()

    return {
        "message": "Cart item replaced",
        "item": cart[product_id]
    }


# 4. Update only quantity
class QuantityUpdate(BaseModel):
    quantity: int


@app.patch("/cart/items/{product_id}")
def update_quantity(product_id: int, data: QuantityUpdate):

    if product_id not in cart:
        raise HTTPException(404, "Product not found")

    cart[product_id]["quantity"] = data.quantity

    return {
        "message": "Quantity updated",
        "item": cart[product_id]
    }


# 5. Delete product from cart
@app.delete("/cart/items/{product_id}")
def delete_item(product_id: int):

    if product_id not in cart:
        raise HTTPException(404, "Product not found")

    del cart[product_id]

    return {
        "message": "Product removed from cart"
    }
