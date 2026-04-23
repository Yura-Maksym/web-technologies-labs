from pydantic import BaseModel
from typing import List, Optional

# --- Інгредієнти ---
class IngredientBase(BaseModel):
    name: str

class IngredientCreate(IngredientBase):
    product_id: int

class IngredientResponse(IngredientBase):
    id: int
    class Config:
        from_attributes = True

# --- Продукти ---
class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    category_id: int

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    category_id: int
    ingredients: List[IngredientResponse] = []
    class Config:
        from_attributes = True

# --- Категорії ---
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    products: List[ProductResponse] = []
    class Config:
        from_attributes = True