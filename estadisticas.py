"""
estadisticas.py
Módulo responsable de calcular y mostrar estadísticas del dataset de países.
"""


def mostrar_estadisticas(paises):
    """
    Calcula y muestra las estadísticas principales del dataset:
    - País con mayor y menor población
    - Promedio de población
    - Promedio de superficie
    - Cantidad de países por continente

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- ESTADÍSTICAS ---")

    if not paises:
        print("[INFO] No hay países cargados para calcular estadísticas.")
        return

    _estadisticas_poblacion(paises)
    _estadisticas_superficie(paises)
    _paises_por_continente(paises)


# ── Funciones auxiliares (internas) ──────────────────────────────────────────

def _estadisticas_poblacion(paises):
    """Muestra estadísticas relacionadas con la población."""
    poblaciones = [p["poblacion"] for p in paises]

    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])
    promedio = sum(poblaciones) / len(poblaciones)

    print("\n── Población ──────────────────────────────────")
    print(f"  País más poblado:    {mayor['nombre']:<20} {mayor['poblacion']:>15,} hab.")
    print(f"  País menos poblado:  {menor['nombre']:<20} {menor['poblacion']:>15,} hab.")
    print(f"  Promedio:            {promedio:>36,.0f} hab.")


def _estadisticas_superficie(paises):
    """Muestra estadísticas relacionadas con la superficie."""
    superficies = [p["superficie"] for p in paises]

    mayor = max(paises, key=lambda p: p["superficie"])
    menor = min(paises, key=lambda p: p["superficie"])
    promedio = sum(superficies) / len(superficies)

    print("\n── Superficie ─────────────────────────────────")
    print(f"  País más grande:     {mayor['nombre']:<20} {mayor['superficie']:>15,} km²")
    print(f"  País más pequeño:    {menor['nombre']:<20} {menor['superficie']:>15,} km²")
    print(f"  Promedio:            {promedio:>36,.0f} km²")


def _paises_por_continente(paises):
    """Muestra la cantidad de países agrupados por continente."""
    conteo = {}

    for pais in paises:
        continente = pais["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1

    print("\n── Países por continente ──────────────────────")
    for continente, cantidad in sorted(conteo.items()):
        print(f"  {continente:<15} {cantidad:>3} país/es")

    print(f"\n  Total de países en el dataset: {len(paises)}")
    print("-" * 50)
