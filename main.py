"""
main.py
Punto de entrada del programa. Muestra el menú principal y coordina
las llamadas a los distintos módulos del sistema.
"""

from carga import cargar_paises, guardar_paises
from operaciones import agregar_pais, actualizar_pais, buscar_pais, eliminar_pais
from filtros import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenamiento import ordenar_paises
from estadisticas import mostrar_estadisticas

ARCHIVO_CSV = "paises.csv"


def menu_filtros(paises):
    """Submenú de filtros."""
    while True:
        print("\n--- FILTRAR PAÍSES ---")
        print("  1. Por continente")
        print("  2. Por rango de población")
        print("  3. Por rango de superficie")
        print("  0. Volver al menú principal")

        opcion = input("\nElegí una opción: ").strip()

        if opcion == "1":
            filtrar_por_continente(paises)
        elif opcion == "2":
            filtrar_por_poblacion(paises)
        elif opcion == "3":
            filtrar_por_superficie(paises)
        elif opcion == "0":
            break
        else:
            print("[ERROR] Opción inválida. Intentá de nuevo.")


def menu_principal():
    """
    Carga los datos, muestra el menú principal en un bucle
    y guarda los cambios al salir.
    """
    print("=" * 50)
    print("   GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 50)

    # Cargar datos al iniciar
    paises = cargar_paises(ARCHIVO_CSV)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("  1. Agregar país")
        print("  2. Actualizar país")
        print("  3. Buscar país")
        print("  4. Eliminar país")
        print("  5. Filtrar países")
        print("  6. Ordenar países")
        print("  7. Ver estadísticas")
        print("  0. Guardar y salir")

        opcion = input("\nElegí una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
            guardar_paises(paises, ARCHIVO_CSV)
        elif opcion == "2":
            actualizar_pais(paises)
            guardar_paises(paises, ARCHIVO_CSV)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            eliminar_pais(paises)
            guardar_paises(paises, ARCHIVO_CSV)
        elif opcion == "5":
            menu_filtros(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            guardar_paises(paises, ARCHIVO_CSV)
            print("\n¡Hasta luego!")
            break
        else:
            print("[ERROR] Opción inválida. Intentá de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()
