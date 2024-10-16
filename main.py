# Una empresa de colectivos tiene 3 líneas de 5 coches cada una. 
# En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
# Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
# Menú:

# 1 )
# Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos).
# Si el chofer existe cargará la recaudación del viaje indicando línea y coche 
# (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados.
# Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches).
# Cada coche de cada línea puede tener varias recaudaciones diarias.
# 
# 2- Mostrar la recaudación de cada coche y línea (mostrar la matriz).
# 3- Calcular y mostrar recaudación por línea.
# 4- Calcular y mostrar recaudación por coche.
# 5- Calcular y mostrar la recaudación total.
# 6- Salir.
# Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y
# verificación de existencia de legajo, cálculos, etc.
from Datos.datos import *

# def menu_principal():
  
print("Bienvenido al menú")
print("1- Cargar plantilla")
print("2- Mostrar la recaudación de los colectivos y las líneas")
print("3- Mostrar la recaudación por línea")
print("4- Mostrar recaudación por coche")
print("5- Mostrar la recaudación total")
print("6- Salir")

plantilla = crear_matriz(3, 5, 0)  # Inicializar la plantilla fuera del bucle

while True:
    opcion = input("Ingrese una opción: ")
    
    match opcion:
        case "1":
            plantilla = cargar_plantilla(plantilla)  # Ejecutar y asignar el resultado a plantilla
        case "2":
            muestra_recaudacion(plantilla)  # Asumimos que "muestra_recaudacion" es "mostrar_matriz"
        case "3":
            recaudacion_por_linea = calcula_recaudacion_linea(plantilla)
            print(recaudacion_por_linea)
        case "4":
            recaudacion_por_colectivo = calcula_recaudacion_colectivo(plantilla)
            print(recaudacion_por_colectivo)
        case "5":
            total_recaudacion = muestra_recaudacion_total(plantilla)
            print(f"Recaudación total: {total_recaudacion}")
        case "6":
            print("Saliste del programa :)")
            break
        case _:
            print("No eligió la opción correcta")


# resultado = menu_principal()