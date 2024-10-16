from Validaciones.validacion import *

def cargar_plantilla(matriz) -> str:
  
  legajo = input("Ingrese el legajo del chofer: ")
  legajo = int(legajo)
  #valido el legajo
  while validar_legajo(legajo) == False:
    legajo = input("Legajo invalido, Ingrese el legajo del chofer valido: ")
    legajo = int(legajo)
    
  linea = input("Ingrese la linea (1 a 3): ")
  linea = int(linea)
  #valido la linea
  while validar_linea(linea) == False:
    linea = input("Invalido, Ingrese la linea (1 a 3): ")
    linea = int(linea)
    
  colectivo = input("Ingrese el colectivo (1 a 5): ")
  colectivo = int(colectivo)
  #valido el colectivo
  while not validar_colectivo(colectivo):
    colectivo = input("Invalido,Ingrese el colectivo (1 a 5): ")
    colectivo = int(colectivo)
  
  recaudacion = input("Ingrese la recaudacion del viaje: ")
  recaudacion = float(recaudacion)

  fila = linea - 1  # La línea ingresada por el usuario (1,2,3) corresponde a los índices (0,1,2)
  columna = colectivo - 1  # El colectivo ingresado por el usuario (1,2,3,4,5) corresponde a los índices (0,1,2,3,4)

    # Añado la recaudación a la posición correcta de la matriz
  for i in range(len(matriz)):
    if i == fila:
      for j in range(len(matriz[i])):
          if j == columna:
            matriz[i][j] += recaudacion
          
  print("El ingreso de la recaudacion fue exitoso.")
  
  return matriz
  

#LINEAS 3 = FILAS
#COLECTIVOS 5 = COLUMNAS

# vector_fila = [0] * len(lista)
# vector_columna = [0] * len(lista[0])

def muestra_recaudacion(matriz) -> list:
  # Mostrar la recaudación de cada colectivo y línea (mostrar la matriz).
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")  # Imprime los elementos en la misma fila
        print()  # Salto de línea al final de cada fila

def calcula_recaudacion_linea(matriz):
  vector_recaudacion = [0] * len(matriz)  # Por linea
    
  for i in range(len(matriz)):
      recaudacion_linea = 0
      for j in range(len(matriz[i])):
          recaudacion_linea += matriz[i][j]  
      vector_recaudacion[i] = recaudacion_linea  
  return vector_recaudacion
  
def calcula_recaudacion_colectivo(matriz):
  vector_colectivo = [0] * len(matriz[0])
  
  for j in range(len(matriz[0])):
    recaudacion_colectivo = 0
    for i in range(len(matriz)):
      recaudacion_colectivo += matriz[i][j]
    vector_colectivo[j] = recaudacion_colectivo
  return vector_colectivo

def muestra_recaudacion_total(matriz):
  recaudacion_total = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      recaudacion_total += matriz[i][j]
  
  return recaudacion_total

####

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

