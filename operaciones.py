"""
operaciones.py
Módulo responsable de agregar, actualizar y buscar países en la lista.
"""


def agregar_pais(paises):
    """
    Solicita los datos de un nuevo país al usuario y lo agrega a la lista.
    No se permiten campos vacíos ni nombres duplicados.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- AGREGAR PAÍS ---")

    # Nombre
    while True:
        nombre = input("Nombre del país: ").strip()
        if not nombre:
            print("[ERROR] El nombre no puede estar vacío.")
        elif _buscar_exacto(paises, nombre) is not None:
            print(f"[ERROR] Ya existe un país con el nombre '{nombre}'.")
        else:
            break

    # Población
    poblacion = _pedir_entero_positivo("Población: ")

    # Superficie
    superficie = _pedir_entero_positivo("Superficie en km²: ")

    # Continente
    while True:
        continente = input("Continente: ").strip()
        if not continente:
            print("[ERROR] El continente no puede estar vacío.")
        else:
            break

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print(f"[OK] País '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    """
    Busca un país por nombre exacto y permite actualizar
    su población y/o superficie.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- ACTUALIZAR PAÍS ---")

    nombre = input("Ingresá el nombre exacto del país a actualizar: ").strip()
    if not nombre:
        print("[ERROR] Debés ingresar un nombre.")
        return

    pais = _buscar_exacto(paises, nombre)
    if pais is None:
        print(f"[ERROR] No se encontró ningún país con el nombre '{nombre}'.")
        return

    print(f"\nDatos actuales de {pais['nombre']}:")
    _mostrar_pais(pais)

    print("\nIngresá los nuevos valores (Enter para mantener el actual):")

    # Actualizar población
    entrada = input(f"Nueva población [{pais['poblacion']}]: ").strip()
    if entrada:
        nueva_poblacion = _validar_entero_positivo(entrada, "población")
        if nueva_poblacion is not None:
            pais["poblacion"] = nueva_poblacion

    # Actualizar superficie
    entrada = input(f"Nueva superficie [{pais['superficie']}]: ").strip()
    if entrada:
        nueva_superficie = _validar_entero_positivo(entrada, "superficie")
        if nueva_superficie is not None:
            pais["superficie"] = nueva_superficie

    print(f"[OK] Datos de '{pais['nombre']}' actualizados correctamente.")


def buscar_pais(paises):
    """
    Busca países por nombre con coincidencia parcial o exacta
    y muestra los resultados.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- BUSCAR PAÍS ---")

    termino = input("Ingresá el nombre o parte del nombre: ").strip()
    if not termino:
        print("[ERROR] Debés ingresar un término de búsqueda.")
        return

    resultados = [
        p for p in paises
        if termino.lower() in p["nombre"].lower()
    ]

    if not resultados:
        print(f"[INFO] No se encontraron países que coincidan con '{termino}'.")
        return

    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    print("-" * 50)
    for pais in resultados:
        _mostrar_pais(pais)
        print("-" * 50)


def eliminar_pais(paises):
    """
    Busca un país por nombre exacto y lo elimina de la lista
    tras pedir confirmación al usuario.

    Args:
        paises (list[dict]): lista actual de países.
    """
    print("\n--- ELIMINAR PAÍS ---")

    nombre = input("Ingresá el nombre exacto del país a eliminar: ").strip()
    if not nombre:
        print("[ERROR] Debés ingresar un nombre.")
        return

    pais = _buscar_exacto(paises, nombre)
    if pais is None:
        print(f"[ERROR] No se encontró ningún país con el nombre '{nombre}'.")
        return

    print(f"\nSe va a eliminar:")
    _mostrar_pais(pais)

    confirmacion = input("\n¿Confirmás la eliminación? (s/n): ").strip().lower()
    if confirmacion == "s":
        paises.remove(pais)
        print(f"[OK] País '{nombre}' eliminado correctamente.")
    else:
        print("[INFO] Eliminación cancelada.")


# ── Funciones auxiliares (internas) ──────────────────────────────────────────

def _buscar_exacto(paises, nombre):
    """
    Devuelve el diccionario del país si el nombre coincide exactamente
    (sin distinguir mayúsculas), o None si no existe.
    """
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return pais
    return None


def _mostrar_pais(pais):
    """Imprime los datos de un país en formato legible."""
    print(f"  Nombre:      {pais['nombre']}")
    print(f"  Población:   {pais['poblacion']:,}")
    print(f"  Superficie:  {pais['superficie']:,} km²")
    print(f"  Continente:  {pais['continente']}")


def _pedir_entero_positivo(mensaje):
    """
    Solicita al usuario un número entero positivo en un bucle
    hasta que ingrese un valor válido.
    """
    while True:
        entrada = input(mensaje).strip()
        resultado = _validar_entero_positivo(entrada, mensaje)
        if resultado is not None:
            return resultado


def _validar_entero_positivo(entrada, campo):
    """
    Valida que una cadena sea un entero positivo.
    Devuelve el entero si es válido, o None si no lo es.
    """
    try:
        valor = int(entrada)
        if valor <= 0:
            raise ValueError
        return valor
    except ValueError:
        print(f"[ERROR] El valor de '{campo}' debe ser un número entero positivo.")
        return None
