import matplotlib.pyplot as plt
from camara import calcular_proyeccion_camara


# Función para mostrar matrices en consola
def dibujar_proyecciones(proj_sin_persp, proj_con_persp, aristas):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Proyección sin perspectiva
    ax1.set_title('Proyección Sin Perspectiva', fontsize=14, fontweight='bold')

    for i, (x, y) in enumerate(proj_sin_persp):
        ax1.plot(x, y, 'ro', markersize=8)
        ax1.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points',
                     fontsize=10, fontweight='bold')

    for inicio, fin in aristas:
        x_val = [proj_sin_persp[inicio][0], proj_sin_persp[fin][0]]
        y_val = [proj_sin_persp[inicio][1], proj_sin_persp[fin][1]]
        if inicio >= 4 and fin >= 4:
            ax1.plot(x_val, y_val, 'b--', linewidth=1.5, alpha=0.7)
        else:
            ax1.plot(x_val, y_val, 'b-', linewidth=2)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')

    # Proyección con perspectiva
    ax2.set_title('Proyección Con Perspectiva', fontsize=14, fontweight='bold')

    for i, (x, y) in enumerate(proj_con_persp):
        ax2.plot(x, y, 'ro', markersize=8)
        ax2.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points',
                     fontsize=10, fontweight='bold')

    for inicio, fin in aristas:
        x_val = [proj_con_persp[inicio][0], proj_con_persp[fin][0]]
        y_val = [proj_con_persp[inicio][1], proj_con_persp[fin][1]]
        if inicio >= 4 and fin >= 4:
            ax2.plot(x_val, y_val, 'b--', linewidth=1.5, alpha=0.7)
        else:
            ax2.plot(x_val, y_val, 'b-', linewidth=2)

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')

    plt.tight_layout()
    plt.show()



# Ejemplo de uso
proj_sin_persp, proj_con_persp = calcular_proyeccion_camara()
aristas = [
    (0, 1), (1, 2), (2, 3), (0, 3),
    (4, 5), (5, 6), (6, 7), (4, 7),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

dibujar_proyecciones(proj_sin_persp, proj_con_persp, aristas)