import random

def generar_legajos():
    legajos = [0] * 15  #  lista con espacio para 15 legajos
    indice = 0  

    while indice < 15:
        legajo = random.randint(10000, 99999)  # Legajo de 5 dígitos
        # Verificar si el legajo ya está en la lista
        encontrado = False
        for l in legajos:
            if l == legajo:
                encontrado = True
                break
        if not encontrado:
            legajos[indice] = legajo
            indice += 1  
    
    return legajos

def validar_legajo(legajo) -> bool:
  legajos_choferes = [10000,10001,10002,100003]
  esta_legajo = False
  
  for i in range(len(legajos_choferes)):
    if legajos_choferes[i] == legajo :
      esta_legajo = True
      break

  return esta_legajo

def validar_linea(linea):
  hay_linea = linea >= 1 and linea <= 3
  
  return hay_linea

def validar_colectivo(colectivo):
  hay_colectivo = colectivo >= 1 and colectivo <= 5
  
  return hay_colectivo
