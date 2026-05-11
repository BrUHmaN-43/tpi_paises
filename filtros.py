"""
filtros.py
Módulo responsable de filtrar países según distintos criterios.
"""


def filtrar_por_continente(paises):
    """
    Filtra y muestra los países que pertenecen a un continente dado.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- FILTRAR POR CONTINENTE ---")

    # Mostrar los continentes disponibles
    continentes = sorted(set(p["continente"] for p in paises))
    print("Continentes disponibles:", ", ".join(continentes))

    continente = input("Ingresá el continente: ").strip()
    if not continente:
        print("[ERROR] Debés ingresar un continente.")
        return

    resultados = [
        p for p in paises
        if p["continente"].lower() == continente.lower()
    ]

    _mostrar_resultados(resultados, f"continente '{continente}'")


def filtrar_por_poblacion(paises):
    """
    Filtra y muestra los países cuya población está dentro de un rango dado.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")

    minimo = _pedir_entero_no_negativo("Población mínima: ")
    maximo = _pedir_entero_no_negativo("Población máxima: ")

    if minimo > maximo:
        print("[ERROR] El mínimo no puede ser mayor que el máximo.")
        return

    resultados = [
        p for p in paises
        if minimo <= p["poblacion"] <= maximo
    ]

    _mostrar_resultados(resultados, f"población entre {minimo:,} y {maximo:,}")


def filtrar_por_superficie(paises):
    """
    Filtra y muestra los países cuya superficie está dentro de un rango dado.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    minimo = _pedir_entero_no_negativo("Superficie mínima (km²): ")
    maximo = _pedir_entero_no_negativo("Superficie máxima (km²): ")

    if minimo > maximo:
        print("[ERROR] El mínimo no puede ser mayor que el máximo.")
        return

    resultados = [
        p for p in paises
        if minimo <= p["superficie"] <= maximo
    ]

    _mostrar_resultados(resultados, f"superficie entre {minimo:,} y {maximo:,} km²")


# ── Funciones auxiliares (internas) ──────────────────────────────────────────

def _mostrar_resultados(resultados, criterio):
    """Muestra los países encontrados o un mensaje si no hay resultados."""
    if not resultados:
        print(f"[INFO] No se encontraron países con {criterio}.")
        return

    print(f"\nSe encontraron {len(resultados)} país/es con {criterio}:")
    print("-" * 50)
    for pais in resultados:
        _mostrar_pais(pais)
        print("-" * 50)


def _mostrar_pais(pais):
    """Imprime los datos de un país en formato legible."""
    print(f"  Nombre:      {pais['nombre']}")
    print(f"  Población:   {pais['poblacion']:,}")
    print(f"  Superficie:  {pais['superficie']:,} km²")
    print(f"  Continente:  {pais['continente']}")


def _pedir_entero_no_negativo(mensaje):
    """
    Solicita un número entero no negativo en un bucle
    hasta que el usuario ingrese un valor válido.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("[ERROR] Ingresá un número entero válido (0 o mayor).")
