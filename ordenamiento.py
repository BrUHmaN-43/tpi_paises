"""
ordenamiento.py
Módulo responsable de ordenar la lista de países según distintos criterios.
"""


def ordenar_paises(paises):
    """
    Muestra un submenú para elegir el criterio y dirección de ordenamiento,
    luego imprime la lista ordenada.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- ORDENAR PAÍSES ---")

    if not paises:
        print("[INFO] No hay países cargados.")
        return

    # Elegir criterio
    print("\nOrdenar por:")
    print("  1. Nombre")
    print("  2. Población")
    print("  3. Superficie")

    criterio = input("\nElegí una opción (1-3): ").strip()

    if criterio == "1":
        clave = "nombre"
        etiqueta = "nombre"
    elif criterio == "2":
        clave = "poblacion"
        etiqueta = "población"
    elif criterio == "3":
        clave = "superficie"
        etiqueta = "superficie"
    else:
        print("[ERROR] Opción inválida.")
        return

    # Elegir dirección
    print("\nDirección:")
    print("  1. Ascendente")
    print("  2. Descendente")

    direccion = input("\nElegí una opción (1-2): ").strip()

    if direccion == "1":
        descendente = False
        etiqueta_dir = "ascendente"
    elif direccion == "2":
        descendente = True
        etiqueta_dir = "descendente"
    else:
        print("[ERROR] Opción inválida.")
        return

    # Ordenar (no modifica la lista original)
    ordenados = sorted(paises, key=lambda p: p[clave], reverse=descendente)

    # Mostrar resultado
    print(f"\nPaíses ordenados por {etiqueta} ({etiqueta_dir}):")
    print("-" * 50)
    for i, pais in enumerate(ordenados, start=1):
        print(f"  {i:>2}. {pais['nombre']:<20} "
              f"Pob: {pais['poblacion']:>15,}   "
              f"Sup: {pais['superficie']:>10,} km²   "
              f"{pais['continente']}")
    print("-" * 50)
