import numpy as np


def calcular_proyeccion_camara():

    # Datos de entrada
    R = np.array([250, 300, -250])  # Posición de la cámara
    O = np.array([0, 0, 0])  # Punto a observar
    D = 300  # Distancia del plano de visión

    # Coordenadas de los 8 vértices del cubo
    vertices = np.array([
        [-100, -100, -100],  # 0
        [100, -100, -100],  # 1
        [100, 100, -100],  # 2
        [-100, 100, -100],  # 3
        [-100, -100, 100],  # 4
        [100, -100, 100],  # 5
        [100, 100, 100],  # 6
        [-100, 100, 100]  # 7
    ])

    print("=" * 60)
    print("CÁLCULO DE PROYECCIÓN DE CÁMARA SINTÉTICA")
    print("=" * 60)
    print(f"Posición de la cámara (R): {R}")
    print(f"Posición a observar (O): {O}")
    print(f"Posición plano de vision (D): {D}")
    print()

    # Calcular vector N
    O_menos_R = O - R
    magnitud_O_menos_R = np.linalg.norm(O_menos_R)
    N = O_menos_R / magnitud_O_menos_R

    print("Cálculo del vector N")
    print(f"O - R = {O_menos_R}")
    print(f"|O - R| = {magnitud_O_menos_R:.6f}")
    print(f"N = {N}")
    print()

    # Calcular vector V
    UP = np.array([0, 1, 0])
    UP_por_N = np.dot(UP, N)
    UPP = UP - UP_por_N * N
    magnitud_UPP = np.linalg.norm(UPP)
    V = UPP / magnitud_UPP

    print("Cálculo del vector V")
    print(f"UP = {UP}")
    print(f"UP · N = {UP_por_N:.6f}")
    print(f"UPP = UP - (UP · N) * N = {UPP}")
    print(f"|UPP| = {magnitud_UPP:.6f}")
    print(f"V = {V}")
    print()

    # Calcular vector U
    U = np.cross(V, N)
    magnitud_U = np.linalg.norm(U)
    U = U / magnitud_U  # Normalizar por si acaso

    print("Cálculo del vector U")
    print(f"U = V × N = {U}")
    print(f"|U| = {magnitud_U:.6f}")
    print()

    # TABLA DE PROYECCIÓN
    print("Tabla de Proyecciones ")
    print("=" * 120)
    print(f"{'Vértice':<8} {'P':<20} {'P-R':<20} {'Pvx':<8} {'Pvy':<8} {'Pvz':<8} {'Sin Perspectiva':<20} {'Con Perspectiva':<20}")
    print(f"{'':>8} {'':>20} {'':>20} {'':>8} {'':>8} {'':>8} {'X':<10} {'Y':<10} {'X':<10} {'Y':<10}")
    print("-" * 120)

    proyecciones_sin_perspectiva = []
    proyecciones_con_perspectiva = []

    for i, P in enumerate(vertices):
        # Calcular P - R
        P_menos_R = P - R

        # Calcular coordenadas en el sistema de visión
        Pvx = np.dot(P_menos_R, U)
        Pvy = np.dot(P_menos_R, V)
        Pvz = np.dot(P_menos_R, N)

        # Coordenadas sin perspectiva
        x_sp = Pvx
        y_sp = Pvy

        # Coordenadas con perspectiva
        x_cp = (Pvx / Pvz) * D if Pvz != 0 else 0
        y_cp = (Pvy / Pvz) * D if Pvz != 0 else 0

        proyecciones_sin_perspectiva.append([x_sp, y_sp])
        proyecciones_con_perspectiva.append([x_cp, y_cp])

        # Formatear vectores para la tabla
        P_str = f"[{P[0]:>4} {P[1]:>4} {P[2]:>4}]"
        P_R_str = f"[{P_menos_R[0]:>4.0f} {P_menos_R[1]:>4.0f} {P_menos_R[2]:>4.0f}]"

        print(f"{i:<8} {P_str:<20} {P_R_str:<20} {Pvx:<8.2f} {Pvy:<8.2f} {Pvz:<8.2f} {x_sp:<10.0f} {y_sp:<10.0f} {x_cp:<10.0f} {y_cp:<10.0f}")

    return proyecciones_sin_perspectiva, proyecciones_con_perspectiva


def main():
    calcular_proyeccion_camara()


if __name__ == "__main__":
    main()