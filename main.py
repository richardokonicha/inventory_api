# CRUD OPERATIONS
from typing import List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prisma import Prisma
from contextlib import asynccontextmanager

# Create an async context manager for handling Prisma connections


@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()

# Create a FastAPI application and attach the lifespan context manager
app = FastAPI(
    title="Inventory Management System",
    version="1.0.0",
    lifespan=lifespan,
    summary="This Inventory Management System, powered by FastAPI and Prisma, streamlines product management for e-commerce. I",
    description="This application, built on FastAPI, empowers e-commerce platforms with a dynamic inventory management system. Leveraging Prisma for database interactions, it facilitates seamless product handling."
)

# Initialize Prisma
prisma = Prisma()

# Define the Product model


class Product(BaseModel):
    name: str = "example product"
    description: str = "example description"
    price: float = 0.0
    sku: Optional[int] = None
    image: Optional[str] = "https://i1.wp.com/gelatologia.com/wp-content/uploads/2020/07/placeholder.png"
    quantity: Optional[int] = None


class Cart(BaseModel):
    item_id: str = None
    customer_id: str = "customer_id"
    product_id: str = "product_id"
    quantity: Optional[int] = 0

# Define the home route


@app.get("/")
def home():
    """
    Redirects to the API documentation.
    """
    return "Goto http://0.0.0.0:8000/docs to see the API documentation"

# Define the route to get all products


@app.get("/products/")
async def get_products():
    """
    Retrieves a list of all products.
    """
    products = await prisma.product.find_many()
    return products

# Define the route to create a product


@app.post("/products/")
async def create_product(product: Product):
    """
    Creates a new product.
    """
    new_product = await prisma.product.create(product.model_dump())
    return new_product

# Define the route to read a product by ID


@app.get("/products/{product_id}")
async def read_product(product_id: int, q: Union[str, None] = None):
    """
    Retrieves information about a product based on its ID.
    """
    product = await prisma.product.find_unique(where={"id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Define the route to update a product by ID


@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    """
    Updates an existing product.
    """
    existing_product = await prisma.product.find_unique(where={"id": product_id})
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = await prisma.product.update(
        where={"id": product_id}, data=product.dict(exclude_unset=True)
    )
    return updated_product

# Define the route to delete a product by ID


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """
    Deletes a product based on its ID.
    """
    existing_product = await prisma.product.find_unique(where={"id": product_id})
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    deleted_product = await prisma.product.delete(where={"id": product_id})
    return deleted_product

#


@app.get("/cart/")
async def get_cart():
    """
    Retrieves a list of all cart.
    """
    cart = await prisma.cart.find_many()
    return cart

# Define the route to create a cart


@app.post("/cart/")
async def create_cart(cart: Cart):
    """
    Creates a new cart.
    """
    new_cart = await prisma.cart.create(cart.model_dump())
    return new_cart

# Define the route to read a cart by ID


@app.get("/cart/{cart_id}")
async def read_cart(cart_id: int, q: Union[str, None] = None):
    """
    Retrieves information about a cart based on its ID.
    """
    cart = await prisma.cart.find_unique(where={"id": cart_id})
    if not cart:
        raise HTTPException(status_code=404, detail="Product not found")
    return cart

# Define the route to update a cart by ID


@app.put("/cart/{cart_id}")
async def update_cart(cart_id: int, cart: Cart):
    """
    Updates an existing cart.
    """
    existing_cart = await prisma.cart.find_unique(where={"id": cart_id})
    if not existing_cart:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_cart = await prisma.cart.update(
        where={"id": cart_id}, data=cart.dict(exclude_unset=True)
    )
    return updated_cart

# Define the route to delete a cart by ID


@app.delete("/cart/{cart_id}")
async def delete_cart(cart_id: int):
    """
    Deletes a cart based on its ID.
    """
    existing_cart = await prisma.cart.find_unique(where={"id": cart_id})
    if not existing_cart:
        raise HTTPException(status_code=404, detail="cart not found")

    deleted_cart = await prisma.cart.delete(where={"id": cart_id})
    return deleted_cart
