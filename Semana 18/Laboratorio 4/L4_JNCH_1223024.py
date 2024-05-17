#Ejercicio 1

# precios = [50, 75, 46, 22, 80, 65, 8]

# def elmenor(precios):
#     menor = precios[0]
#     for precio in precios:
#         if precio < menor:
#             menor = precio
#     return menor

# def preciomayor(precios):
#     mayor = precios[0]
#     for precio in precios:
#         if precio > mayor:
#             mayor = precio
#     return mayor

#Ejercicio 2

# menor_precio = elmenor(precios)
# mayor_precio = preciomayor(precios)

# print("El menor precio es:", menor_precio)
# print("El mayor precio es:", mayor_precio)


# abecedario = list("abcdefghijklmnopqrstuvwxyz")

# abecedario_sin3 = [letra for indice, letra in enumerate(abecedario, start=1) if indice % 3 != 0]

# print("Lista que nos queda después de eliminar letras enque sean multiplo de tres es:")
# print(abecedario_sin3)

#Ejercicio 3

import random

vector = [random.randint(1, 100) for _ in range(100)]

pares = [num for num in vector if num % 2 == 0]
impares = [num for num in vector if num % 2 != 0]

print("Números pares:")
print(pares)

print("\nNúmeros impares:")
print(impares)