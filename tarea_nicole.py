from datetime import datetime

class Vehiculo:
    def __init__(self, marca, modelo, anio, motor):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._motor = motor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        self._anio = value

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    def encender(self):
        return f"{self._marca} {self._modelo} encendido."

    def apagar(self):
        return f"{self._marca} {self._modelo} apagado."

    def _str_(self):
        return f"Vehiculo({self._marca}, {self._modelo}, {self._anio}, {self._motor})"
    

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, num_puertas):
        super().__init__(marca, modelo, anio, motor)
        self._num_puertas = num_puertas

    @property
    def num_puertas(self):
        return self._num_puertas

    @num_puertas.setter
    def num_puertas(self, value):
        self._num_puertas = value

    def abrir_maletero(self):
        return "Maletero abierto."

    def tocar_claxon(self):
        return "¡BEEP BEEP!"

    def _str_(self):
        return f"Automovil -> {super()._str_()}, Puertas={self._num_puertas}"
    


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, cilindraje):
        super().__init__(marca, modelo, anio, motor)
        self._cilindraje = cilindraje

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, value):
        self._cilindraje = value

    def hacer_caballito(self):
        return "La moto está haciendo un caballito."

    def usar_patada_arranque(self):
        return "Arranque con patada realizado."

    def _str_(self):
        return f"Motocicleta -> {super()._str_()}, Cilindraje={self._cilindraje}cc"
    

class Motor:
    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, value):
        self._potencia = value

    def encender_motor(self):
        return "El motor está encendido."

    def detener_motor(self):
        return "El motor está apagado."

    def __str__(self):
        return f"Motor(tipo={self._tipo}, potencia={self._potencia} HP)"
    



# Crear motores
motor1 = Motor("Gasolina", 150)
motor2 = Motor("Diésel", 200)
motor3 = Motor("Gasolina", 50)
motor4 = Motor("Eléctrico", 70)

# Crear vehículos
auto1 = Automovil("Toyota", "Corolla", 2022, motor1, 4)
auto2 = Automovil("Chevrolet", "Spark", 2021, motor2, 5)

moto1 = Motocicleta("Yamaha", "FZ", 2020, motor3, 150)
moto2 = Motocicleta("Honda", "CBR", 2023, motor4, 250)

# Ejecutar métodos
print(auto1.encender())
print(auto1.abrir_maletero())
print(auto2.tocar_claxon())

print(moto1.hacer_caballito())
print(moto2.usar_patada_arranque())

# Mostrar objetos
print("\n--- OBJETOS ---")
print(auto1)
print(auto2)
print(moto1)
print(moto2)

# Fecha y hora (para captura)
print("\nFecha y hora de ejecución:", datetime.now())