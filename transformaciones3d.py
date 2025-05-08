import numpy as np
import math as m

# Función para mostrar matrices
def mostrar(titulo, matriz):
    filas = (matriz.shape)[0]
    columnas = (matriz.shape)[1]
    print("** " + titulo + " **")
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz[i,j]:8.4f}", end="")
        print("")
    print("--------------------------------")

# Funciones de matrices de transformación
def rotacionX(angulo):
    angulo = np.radians(angulo)
    return np.matrix([
        [1, 0, 0, 0],
        [0, m.cos(angulo), m.sin(angulo), 0],
        [0, -m.sin(angulo), m.cos(angulo), 0],
        [0, 0, 0, 1]
    ])

def rotacionY(angulo):
    angulo = np.radians(angulo)
    return np.matrix([
        [m.cos(angulo), 0, -m.sin(angulo), 0],
        [0, 1, 0, 0],
        [m.sin(angulo), 0, m.cos(angulo), 0],
        [0, 0, 0, 1]
    ])

def rotacionZ(angulo):
    angulo = np.radians(angulo)
    return np.matrix([
        [m.cos(angulo), m.sin(angulo), 0, 0],
        [-m.sin(angulo), m.cos(angulo), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def escalacion(sx, sy, sz):
    return np.matrix([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def traslacion(tx, ty, tz):
    return np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])

def reflexionXY():
    return np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]
    ])

def reflexionXZ():
    return np.matrix([
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def reflexionYZ():
    return np.matrix([
        [-1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def identidad():
    return np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def inversa(matriz):
    return np.linalg.inv(matriz)

def vector(x, y, z):
    return np.matrix([x, y, z, 1])

# ------------------------------------------------------
# EJERCICIO 1 - Transformar Figura A a Figura B
# ------------------------------------------------------

print("Punto fijo: e")

#Primera traslación
traslacion1 = traslacion(10, -2, 7)
mostrar("Primera matriz de traslación", traslacion1)

#Escalación
escala = escalacion(1/2, 1/3, 1/2)
mostrar("Matriz de escalación", escala)

#Rotación
rotacion = rotacionY(90)
mostrar("Matriz de rotación", rotacion)

#Segunda traslación
traslacion2 = traslacion(2, 1, 6)
mostrar("Segunda matriz de traslación", traslacion2)

#Matriz de transformación compuesta A → B
matriz_AaB = traslacion1 * escala * rotacion * traslacion2
mostrar("Matriz de transformación compuesta (A a B)", matriz_AaB)

# Puntos de la Figura A
puntosA = np.matrix([
    [0, 2, -7, 1],
    [0, 11, -7, 1],
    [0, 11, -3, 1],
    [0, 2, -3, 1],
    [-8, 2, -7, 1],
    [-8, 2, -3, 1]
])

# Aplicar la transformación a los puntos de A
puntosB = puntosA * matriz_AaB
mostrar("Puntos B obtenidos", puntosB)

# ------------------------------------------------------
# EJERCICIO 2 - Transformar Figura B a Figura A
# ------------------------------------------------------

print("Transformando de Figura B a Figura A usando el punto fijo: a")

#Primera traslación
traslacion1B = traslacion(-2, -1, -1)
mostrar("Primera matriz de traslación", traslacion1B)

#Escalación inversa
escalaB = escalacion(2, 3, 2)
mostrar("Matriz de escalación", escalaB)

#Rotación inversa
rotacionB = rotacionY(-90)
mostrar("Matriz de rotación", rotacionB)

#Segunda traslación
traslacion2B = traslacion(0, 2, -7)
mostrar("Segunda matriz de traslación", traslacion2B)

#Matriz de transformación compuesta B → A
matriz_BaA = traslacion1B * escalaB * rotacionB * traslacion2B
mostrar("Matriz de transformación compuesta (B a A)", matriz_BaA)

# Puntos de la Figura B
puntosB2 = np.matrix([
    [2, 1, 1, 1],
    [2, 4, 1, 1],
    [4, 4, 1, 1],
    [4, 1, 1, 1],
    [2, 1, 5, 1],
    [4, 1, 5, 1]
])

# Aplicar la transformación inversa a los puntos de B
puntosA2 = puntosB2 * matriz_BaA
mostrar("Puntos A recuperados", puntosA2)

# ------------------------------------------------------
# EJERCICIO 3 - Comprobación de Inversas
# ------------------------------------------------------

print("Comprobación de matrices inversas:")

# Multiplicar la matriz A→B por la matriz B→A
matriz_identidad = matriz_AaB * matriz_BaA
mostrar("Matriz Identidad", matriz_identidad)
