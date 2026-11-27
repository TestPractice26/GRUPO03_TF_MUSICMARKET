class Cliente:
    def __init__(self, dni: str, nombres: str, telefono: str, correo: str, direccion: str = ""):
        self.__dni = dni
        self._nombres = nombres
        self.__telefono = telefono 
        self.__correo = correo
        self.__direccion = direccion 
        
#Getters
def get_dni(self) -> str:
    return self.__dni 
def get_nombres(self) -> str:
    return self.__nombres
def get_telefono(self) -> str:
    return self.__telefono
def get_correo(self) -> str:
    return self.__correo
def get_direccion(self) -> str:
    return self.__direccion 

#Setters 
def set_telefono(self, telefono: str):
    self.__telefono = telefono
def set_correo(self, correo: str):
    self.__correo = correo