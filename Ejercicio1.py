import numpy as np
import math as m

def despliega(c, m):
    rens = (m.shape)[0]
    cols = (m.shape)[1]
    print("** " + c + " **")
    for i in range(0, rens):
        for j in range(0, cols):
            print(f"{m[i, j]:8.4f}", end="")
        print("")
    print("--------------------------------")

def rotacionX(ang):
    ang = np.radians(ang)
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

def inversa(m):
    return np.linalg.inv(m)

def vector(x, y, z):
    return np.matrix([x, y, z, 1])

## Escribir código a partir de aquí en Python online.

mt1 = traslacion(0, -2, 3)
despliega("Primer traslacion", mt1)
me = escalacion(1 / 2, 1 / 3, 1 / 2)
despliega("Escalacion", me)
mr = rotacionY(90)
despliega("Rotacion Y 90", mr)
mt2 = traslacion(4, 1, 1)
despliega("Segunda traslacion", mt2)
Mab = mt1 * me * mr * mt2
despliega("Matrix de transformacion compuesta A B", Mab)
puntosA=np.matrix([
    [0, 2, -7, 1],
    [0, 11, -7, 1],
    [0, 11, -3, 1],
    [0, -1, 1, 1],
    [-8, 2, -7, 1],
    [-8, 2, -3, 1]
])  ## Como no podemos multiplicar una matriz 6x3 4x4, ponemos un 1 al final de cada matriz
despliega("Puntos A", puntosA)
puntosB=puntosA *Mab
despliega("Puntos B", puntosB)


##hacer el ejercicio de b a a y de a a b


## soy el f 