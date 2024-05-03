# EJercicio 1
#print("Ingrese las dimensiones de los lados del triángulo:")
#print("Ingrese lado 1:")
#lado1 = input ()
#print("Ingrese lado 2:")
#lado2 = input ()
#print("Ingrese lado 3:")
#lado3 = input ()
#
#def tipo_triangulo(lado1, lado2, lado3):
#    if lado1 == lado2 == lado3:
#        return "Equilátero"
#    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#        return "Isósceles"
#    else:
#        return "Escaleno"
#    
#print(tipo_triangulo(lado1, lado2, lado3))


# EJercicio 2
import math
print("Ingrese el radio")
radio = int(input())

def Obtenerperimetro(r):
    perimetro = float(2*r)*math.pi
    return perimetro

def ObtenerArea(r):
    area = math.pi * (r *pow(r,2))
    return area

def ObtenerVolumen(r):
    volumen = (4 / 3) * math.pi * (r *pow(r,3))
    return volumen

print("Perímetro: " + str(Obtenerperimetro(radio)))
print("Área: " + str(ObtenerArea(radio)))
print("Volumen: " + str(ObtenerVolumen(radio)))

#Ejercicio 3

#def imprimir_nombre_mes(numero):
#    mes = {
#        1: "Enero",
#        2: "Febrero",
#        3: "Marzo",
#        4: "Abril",
#        5: "Mayo",
#        6: "Junio",
#        7: "Julio",
#        8: "Agosto",
#        9: "Septiembre",
#        10: "Octubre",
#        11: "Noviembre",
#        12: "Diciembre"
#    }
#    if numero in mes:
#        print(mes[numero])
#    else:
#        print("Ponga un numero de mes valido.")
#print("Ingrese un número del 1 al 12:")
#numero_mes = int(input())
#imprimir_nombre_mes(numero_mes)
#