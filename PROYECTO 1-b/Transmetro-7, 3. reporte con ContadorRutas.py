estaciones = {
    51: "51 Estación Javier",
    61: "61 Estación Trébol",
    71: "71 Estación Don Bosco",
    82: "82 Estación Plaza Municipal"
}

rutas = {
    (51, 61): 39,
    (51, 71): 18,
    (71, 82): 23,
    (61, 51): 8,
    (82, 51): 42
}
ConteoDeRuta1 = 0
ConteoDeRuta2 = 0 
ConteoDeRuta3 = 0
ConteoDeRuta4 = 0 
ConteoDeRuta5 = 0

def calcular_precio(distancia, embarazada, edad):
    precio_base = 1.5
    costo_extra_por_km = 0.25
    precio_18a25 = 0.25
    costo_total = precio_base + (max(distancia - 8, 0) * costo_extra_por_km)
    if embarazada:
        return 0
    if 15 <= edad <= 25:
        costo_total *= (1 - precio_18a25)
    return costo_total

def comprar_boleto():
    global ConteoDeRuta1, ConteoDeRuta2, ConteoDeRuta3, ConteoDeRuta4, ConteoDeRuta5
    print("Ingrese en que estacion se encuentra:")
    estacion_partida = int(input())
    while estacion_partida not in estaciones:
        print("Estación de partida no válida. Por favor, ingrese un número de estación válido:")
        estacion_partida = int(input())
    print("Ingrese a que estacion quiere ir:")
    estacion_destino = int(input())
    while estacion_destino not in estaciones or (estacion_partida, estacion_destino) not in rutas:
        print("Ruta no válida. Por favor, ingrese un número de estación de destino válida:")
        estacion_destino = int(input())
    print("Cual es su nombre?")
    nombre = input()
    while True:
        print("¿Cuántos años tiene?")
        edad = input()
        if edad.isdigit():
            edad = int(edad)
            break
        else: 
            print("Por favor, ingrese solo números para la edad:")
    print("Indique si está embarazada con si o no:")
    embarazada = input().lower() == "si"
    distancia = rutas[(estacion_partida, estacion_destino)]
    precio = calcular_precio(distancia, embarazada, edad)
    tiempo_estimado = distancia / 20
    
    if (estacion_partida, estacion_destino) == (51, 61):
        ConteoDeRuta1 += 1
    elif (estacion_partida, estacion_destino) == (51, 71):
        ConteoDeRuta2 += 1
    elif (estacion_partida, estacion_destino) == (71, 82):
        ConteoDeRuta3 += 1
    elif (estacion_partida, estacion_destino) == (61, 51):
        ConteoDeRuta4 += 1
    elif (estacion_partida, estacion_destino) == (82, 51):
        ConteoDeRuta5 += 1

    print("\nInformacion sobre la compra de tu boleto:")
    print(f"Estación de partida: {estaciones[estacion_partida]}")
    print(f"Estación de destino: {estaciones[estacion_destino]}")
    print(f"El precio de tu boleto es: Q{precio:.2f}")
    print(f"Tu viaje tardará aproximadamente: {tiempo_estimado:.2f} horas")
    return precio

def generar_reporte(ventas):
    global ConteoDeRuta1, ConteoDeRuta2, ConteoDeRuta3, ConteoDeRuta4, ConteoDeRuta5
    total_boletos= sum(ventas.values())
    total_dinero = sum(ventas.keys())
    print("\nReporte de las ventas:")
    print(f"Total de boletos vendidos: {total_boletos }")
    print(f"Dinero ganado: Q{total_dinero:.2f}")
    print("\nCantidad de boletos vendidos por ruta:")
    print(f"Ruta de la estacion 51 a 61: {ConteoDeRuta1}")
    print(f"Ruta de la estacion 51 a 71: {ConteoDeRuta2}")
    print(f"Ruta de la estacion 71 a 82: {ConteoDeRuta3}")
    print(f"Ruta de la estacion 61 a 51: {ConteoDeRuta4}")
    print(f"Ruta de la estacion 82 a 51: {ConteoDeRuta5}")


def menuprincpal():
    ventas = {}
    while True:
        print("\nBienvenido al sistema de Boletos de Transmetro de la municipalidad de Guatemala")
        print("1. Estaciones y rutas disponibles")
        print("2. Comprar tu boleto")
        print("3. Reportes de venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ") 
        if opcion == "1":
            print("Estaciones y rutas disponibles:")   
            print("51 Estación Javier")
            print("Rutas disponibles desde esta estación:")
            print("  - 61 Estación Trébol: 39 km")
            print("  - 71 Estación Don Bosco: 18 km")
            print("61 Estación Trébol")
            print("Rutas disponibles desde esta estación:")
            print("  - 51 Estación Javier: 8 km")
            print("71 Estación Don Bosco")
            print("Rutas disponibles desde esta estación:")
            print("  - 82 Estación Plaza Municipal: 23 km")
            print("82 Estación Plaza Municipal")
            print("Rutas disponibles desde esta estación:")
            print("  - 51 Estación Javier: 42 km") 
        elif opcion == "2":
            precio = comprar_boleto()
            ventas[precio] = ventas.get(precio, 0) + 1
        elif opcion == "3":
            generar_reporte(ventas)
        elif opcion == "4":
            print("Gracias por usar nuestro sistema de Transmetro, buen viaje!")
            break
        else:
            print("Por favor seleccione un numero del 1 al 4.")

if __name__ == "__main__":
     menuprincpal()