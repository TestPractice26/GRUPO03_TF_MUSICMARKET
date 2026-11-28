class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, marca: str, precio: float, stock: int):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__marca = marca
        self.__precio = precio
        self.__stock = stock

    #Getters
    def get_codigo(self) -> str:
        return self.__codigo
    def get_nombre(self) -> str:
        return self.__nombre
    def get_categoria(self) -> str:
        return self.__categoria
    def get_marca(self) -> str:
        return self.__marca
    def get_precio(self) -> float:
        return self.__precio
    def get_stock(self) -> int: 
        return self.__stock

    #Setters 
    def set_precio(self, nuevo_precio: float): 
        self.__precio = nuevo_precio

    def set_stock(self, nuevo_stock: int):
        self.__stock = nuevo_stock
