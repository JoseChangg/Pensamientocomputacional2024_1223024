import time
import threading

class Zona:
    def __init__(self, nombre, temperatura_deseada=22):
        self.nombre = nombre
        self.temperatura_deseada = temperatura_deseada
        self.temperatura_actual = 22  # Valor inicial de la temperatura
        self.horarios = {}

    def ajustar_temperatura(self):
        # Ajusta la temperatura actual para acercarse a la deseada
        if self.temperatura_actual < self.temperatura_deseada:
            self.temperatura_actual += 1
        elif self.temperatura_actual > self.temperatura_deseada:
            self.temperatura_actual -= 1

    def actualizar_temperatura_actual(self, nueva_temperatura):
        self.temperatura_actual = nueva_temperatura

class SistemaAutomatizacion:
    def __init__(self):
        self.zonas = {}
        self.corriendo = True

    def agregar_zona(self, nombre):
        self.zonas[nombre] = Zona(nombre)

    def establecer_temperatura(self, nombre, temperatura):
        if nombre in self.zonas:
            self.zonas[nombre].temperatura_deseada = temperatura

    def programar_horario(self, nombre, hora, temperatura):
        if nombre in self.zonas:
            self.zonas[nombre].horarios[hora] = temperatura

    def mostrar_temperaturas(self):
        for nombre, zona in self.zonas.items():
            print(f"{nombre}: Actual {zona.temperatura_actual}°C, Deseada {zona.temperatura_deseada}°C")

    def ajustar_temperaturas(self):
        while self.corriendo:
            for zona in self.zonas.values():
                zona.ajustar_temperatura()
                hora_actual = time.strftime("%H:%M")
                if hora_actual in zona.horarios:
                    zona.temperatura_deseada = zona.horarios[hora_actual]
            time.sleep(10)  # Ajusta cada 10 segundos

    def detener(self):
        self.corriendo = False

    def iniciar(self):
        hilo = threading.Thread(target=self.ajustar_temperaturas)
        hilo.start()

def menu():
    sistema = SistemaAutomatizacion()
    sistema.iniciar()

    while True:
        print("\n--Menú de opciones--")
        print("1. Configurar Zonas")
        print("2. Ajustar Temperaturas")
        print("3. Programar Horarios")
        print("4. Mostrar Temperaturas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_zona = input("Ingrese el nombre de la zona: ")
            sistema.agregar_zona(nombre_zona)
        elif opcion == "2":
            nombre_zona = input("Ingrese el nombre de la zona: ")
            temperatura = int(input("Ingrese la temperatura deseada: "))
            sistema.establecer_temperatura(nombre_zona, temperatura)
        elif opcion == "3":
            nombre_zona = input("Ingrese el nombre de la zona: ")
            hora = input("Ingrese la hora (HH:MM): ")
            temperatura = int(input("Ingrese la temperatura deseada para ese horario: "))
            sistema.programar_horario(nombre_zona, hora, temperatura)
        elif opcion == "4":
            sistema.mostrar_temperaturas()
        elif opcion == "5":
            print("Gracias por utilizar nuestro sistema, pase buen dia.")
            sistema.detener()
            break
        else:
            print("Opción no válida. Por favor, elija un numero del 1 al 5 por favor.")

if __name__ == "__main__":
    menu()