from models.venta import Venta
from models.producto import Producto
from utils.excepciones import StockInsuficienteException

class GestionVentas:
    def __init__(self):
        self.__ventas: list[Venta] = []

    def procesar_venta(self, venta: Venta):
        # 1. Validar stock disponible
        for item in venta.get_detalles():
            prod: Producto = item["producto"]
            cant: int = item["cantidad"]
            if prod.get_stock() < cant:
                raise StockInsuficienteException( f"Stock insuficiente para '{prod.get_nombre()}'. Disponible: {prod.get_stock()}, solicitado: {cant}" )
            
        # 2. Descontar stock automáticamente
        for item in venta.get_detalles():
            prod: Producto = item["producto"]
            cant: int = item["cantidad"]
            prod.set_stock(prod.get_stock() - cant)
            
        # 3. Registrar venta
        self.__ventas.append(venta)

    def obtener_ventas(self) -> list[Venta]:
        return self.__ventas