#Patron de diseño: Comportamiento
#Observer

class Observer():
    def actualizar(self, evento):
        pass
    
class Subject():
    def __init__(self):
        self.observers = []
    
    def suscribe(self,obs):
        self.observers.append(obs)
    
    def unsuscribe(self,obs):
        self.observers.remove(obs)
        
    def notificar(self,evento):
        for obs in self.observers:
            obs.actualizar(evento)

# Ejemplo con grupo de WhatsApp y notificacion del celular:

class Grupo(Subject):
    def mensaje(self, contenido):
        print(f"Mensaje: {contenido}")
        self.notificar({'mensaje' : contenido})

class Notificaciones(Observer):
    def __init__(self, nombre_dispositivo):
        self.nombre_dispositivo = nombre_dispositivo
        
    def actualizar(self, evento):
        mensaje_recibido = evento['mensaje']
        print(f"[{self.nombre_dispositivo}] Nueva notificación: {mensaje_recibido}")
        
#Patron de diseño: Creacional
#Factory Method

from abc import ABC, abstractmethod
class Vehiculo(ABC):

    @abstractmethod
    def arrancar(self):
        pass

class Auto(Vehiculo):

    def arrancar(self):
        print("El auto ha arrancado")
class Moto(Vehiculo):

    def arrancar(self):
        print("La moto ha arrancado")
    

class VehiculoFactory:

    @staticmethod
    def crear_vehiculo(tipo):

        if tipo.lower() == "auto":
            return Auto()

        elif tipo.lower() == "moto":
            return Moto()

        else:
            print("Tipo no valido")
            

#Patron de diseño: Estructural
#Decorator

from abc import ABC, abstractmethod

#Clase abstracto
class Bebida(ABC):

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def costo(self):
        pass

#Clase Base
class Cafe(Bebida):

    def descripcion(self):
        return "Café"

    def costo(self):
        return 100

#Decorator
class DecoradorBebida(Bebida):

    def __init__(self, bebida):
        self.bebida = bebida
    
#Opciones para decorar la clase Base
class Leche(DecoradorBebida):

    def descripcion(self):
        return self.bebida.descripcion() + " + Leche"

    def costo(self):
        return self.bebida.costo() + 20