class Cuota:
    def __init__(self, num_cuota: int, fecha_vencimiento: str, importe: float, estado: str = "Pendiente"):
        self.__num_cuota = num_cuota 
        self.__fecha_vencimiento = fecha_vencimiento
        self.__importe = importe
        self.__estado = estado # "Pendiente" o "Pagada"

#Getters
    def get_num_cuota(self) -> int:
        return self.__num_cuota
    def get_fecha_vencimiento(self) -> str:
        return self.__fecha_vencimiento
    def get_importe(self) -> float:
        return self.__importe 
    def get_estado(self) -> str:
        return self.__estado

#Setters    
    def pagar_cuota(self): 
        self.__estado = "Pagada"