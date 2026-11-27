from typing import List
from models.cliente import Cliente
from models.producto import Producto
from models.cuota import Cuota

class Venta:
    def __init__(self, id_venta: str, cliente: Cliente, fecha: str):
        self._id_venta = id_venta
        self._cliente = cliente 
        self._fecha = fecha
        self._detalles: List[dict] = []
        self._monto_total: float = 0.0
        
    def agregar_producto(self, producto: Producto, cantidad: int):
        subtotal = producto.get_precio() * cantidad
        self._detalles.append({"producto": producto, "cantidad": cantidad, "subtotal": subtotal})
        self._monto_total += subtotal
    
    def get_id_venta(self) -> str:
        return self._id_venta
    def get_cliente(self) -> Cliente:
        return self._cliente
    def get_monto_total(self) -> float:
        return self._monto_total
    def get_detalles(self) -> List[dict]:
        return self._detalles
    
    # Aplicación de HERENCIA y COMPOSICIÓN
class VentaFinanciada(Venta):
    def __init__(self, id_venta: str, cliente: Cliente, fecha: str, cuota_inicial: float, num_cuotas: int):
        super().__init__(id_venta, cliente, fecha)
        self.__cuota_inicial = cuota_inicial
        self.__num_cuotas = num_cuotas
        self.__monto_financiado:float = 0.0
        self.__cronograma_cuotas: List[Cuota] = []
    def generar_financiamiento(self):
        self.__monto_financiado = self._monto_total - self.__cuota_inicial
        monto_por_cuota = self.__monto_financiado / self.__num_cuotas
            
        for i in range(1, self.__num_cuotas + 1):
            fecha_venc = f"2026-12-{i:02d}"
            self.__cronograma_cuotas.append(Cuota(i, fecha_venc, monto_por_cuota))
        
    def get_cronograma(self) -> List[Cuota]:
        return self.__cronograma_cuotas
    def get_monto_financiado(self) -> float:
        return self.__monto_financiado