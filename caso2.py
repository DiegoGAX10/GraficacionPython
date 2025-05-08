import numpy as np
import math as m

# Función para mostrar matrices en consola
def despliega(c, m):
    rens = (m.shape)[0]
    cols = (m.shape)[1]
    print("** " + c + " **")
    for i in range(0, rens):
        for j in range(0, cols):
            print(f"{m[i, j]:8.4f}", end="")
        print("")
    print("--------------------------------")

# Funciones que crean matrices de transformación
def rotacionX(ang):
    ang = np.radians(ang)  # Convierte grados a radianes
    return np.matrix([
        [1, 0, 0, 0],
        [0, m.cos(ang), m.sin(ang), 0],
        [0, -m.sin(ang), m.cos(ang), 0],
        [0, 0, 0, 1]
    ])

def rotacionY(ang):
    ang = np.radians(ang)
    return np.matrix([
        [m.cos(ang), 0, -m.sin(ang), 0],
        [0, 1, 0, 0],
        [m.sin(ang), 0, m.cos(ang), 0],
        [0, 0, 0, 1]
    ])

def rotacionZ(ang):
    ang = np.radians(ang)
    return np.matrix([
        [m.cos(ang), m.sin(ang), 0, 0],
        [-m.sin(ang), m.cos(ang), 0, 0],
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

# --- Caso 2: Transformación de figura A a figura B ---

print("Caso 2 Punto fijo: C")

# Primera traslación: se mueve el punto fijo C al origen
mt1 = traslacion(1, -3, 0)
despliega("Primera matriz de traslacion", mt1)

# Escalación: se reduce el tamaño a la mitad en X y Y, y luego se duplica en Z
me = escalacion(1/2, 1/2, 2)
despliega("Matriz de escalacion", me)

# Rotación en Z 90°: se gira la figura 90 grados sobre el eje Z
mr = rotacionZ(90)
despliega("Matriz de rotación", mr)

# Rotación en Y -90°: luego se gira la figura -90 grados sobre el eje Y
mr2 = rotacionY(-90)
despliega("Matriz de rotación", mr2)

# Segunda traslación: se reposiciona la figura final
mt2 = traslacion(0, -2, 1)
despliega("Segunda matriz de traslación", mt2)

# Multiplicación de todas las matrices para obtener la matriz compuesta A -> B
mab = mt1 * me * mr * mr2 * mt2
despliega("Matriz de transformación compuesta", mab)

# Definición de los puntos de la figura A
puntosA = np.matrix([
    [-1, 7, -3, 1],
    [-1, 7, 0, 1],
    [-1, 3, 0, 1],
    [-1, 3, -3, 1],
    [-3, 3, 0, 1],
    [-3, 3, -3, 1]
])

# Comprobacion de los puntos B
puntosB = puntosA * mab
despliega("Puntos B", puntosB)

# --- Código del Caso 2: Transformación inversa de figura B a figura A ---

print("Transformamos de figura B a figura A usando el punto fijo C")

# Primera traslación: mueve el punto fijo C de B al origen
# Punto C de B es (0, -2, 1)
mt1B = traslacion(0, 2, -1)
despliega("Primer matriz de traslacion", mt1B)

# Rotación en Y 90°: deshace la rotación Y
mrB = rotacionY(90)
despliega("Matriz de rotación", mrB)

# Rotación en Z -90°: deshace la rotación Z
mr2B = rotacionZ(-90)
despliega("Matriz de rotación", mr2B)

# Escalación: restaura el tamaño original (el inverso de la escalación inicial)
meB = escalacion(2, 2, 1/2)
despliega("Matriz de escalacion", meB)

# Segunda traslación: reposiciona la figura A
# Punto C de A es (-1, 3, 0)
mt2B = traslacion(-1, 3, 0)
despliega("Segunda matriz de traslación", mt2B)

# Multiplicación de todas las matrices para obtener la transformación inversa B -> A
mba = mt1B * mrB * mr2B * meB * mt2B
despliega("Matriz de transformación compuesta", mba)

# Matriz figura b
puntosB2 = np.matrix([
    [6, -2, -1, 1],
    [0, -2, -1, 1],
    [0, -2, 1, 1],
    [6, -2, 1, 1],
    [0, -3, 1, 1],
    [6, -3, 1, 1]
])

# Comprobacion de los puntos A
puntos = puntosB2 * mba
despliega("Puntos A", puntos)
