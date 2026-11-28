from models.producto import Producto
from utils.excepciones import PrecioInvalidoException

class GestionInventario:
    def __init__(self):
        self.__productos: list[Producto] = []
    def registrar_producto(self, codigo: str, nombre: str, categoria: str, marca: str, precio: float, stock: int):
        if precio <= 0:
            raise PrecioInvalidoException() 
        nuevo_prod = Producto(codigo, nombre, categoria, marca, precio, stock)
        self.__productos.append(nuevo_prod)
        
    def buscar_por_codigo(self, codigo: str) -> Producto | None:
        for p in self.__productos:
            if p.get_codigo() == codigo:
                return p 
        return None
    
    def obtener_todos(self) -> list[Producto]:
        return self.__productos