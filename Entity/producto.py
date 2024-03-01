from pydantic import BaseModel

class Producto(BaseModel):  # class notas(BaseModel)
    id_cliente: int
    nombre: str
    valor: float

class ProductoResponse(BaseModel):
    id_cliente: int
    nombre: str = None
    valor: float
