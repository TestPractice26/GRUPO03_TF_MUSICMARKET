class PrecioInvalidoException(Exception): 
    """Se dispara si el precio ingresado es menor o igual a cero (HU01).""" 
    def __init__(self, mensaje="El precio del instrumento debe ser mayor a S/. 0.00"):
        super().__init__(mensaje)

class StockInsuficienteException(Exception):
    """Se dispara si se intenta vender más unidades de las disponibles en inventario (HU04)."""
    def __init__(self, mensaje="No hay stock suficiente en almacén para completar la venta."):
        super().__init__(mensaje)
        
class DniDuplicadoException(Exception):
    """Se dispara si se intenta registrar un cliente con un DNI ya existente (HU03)."""
    def __init__(self, mensaje="Ya existe un cliente registrado con el mismo DNI."):
        super().__init__(mensaje)