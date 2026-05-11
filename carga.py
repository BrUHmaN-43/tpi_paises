"""
carga.py
Módulo responsable de leer y guardar el dataset de países desde/hacia un archivo CSV.
"""

import csv
import os

ARCHIVO_CSV = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises(ruta=ARCHIVO_CSV):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un país con sus datos.

    Retorna:
        list[dict]: lista de países, o lista vacía si hay error.
    """
    paises = []

    if not os.path.exists(ruta):
        print(f"[AVISO] No se encontró el archivo '{ruta}'. Se iniciará con lista vacía.")
        return paises

    try:
        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Validar que el CSV tenga los campos esperados
            if lector.fieldnames is None or not all(c in lector.fieldnames for c in CAMPOS):
                print(f"[ERROR] El archivo '{ruta}' no tiene el formato correcto.")
                print(f"        Se esperan las columnas: {', '.join(CAMPOS)}")
                return paises

            for numero_fila, fila in enumerate(lector, start=2):
                pais = _parsear_fila(fila, numero_fila)
                if pais is not None:
                    paises.append(pais)

    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo: {e}")

    print(f"[OK] Se cargaron {len(paises)} países desde '{ruta}'.")
    return paises


def guardar_paises(paises, ruta=ARCHIVO_CSV):
    """
    Guarda la lista de países en el archivo CSV.

    Args:
        paises (list[dict]): lista de países a guardar.
        ruta (str): ruta del archivo CSV.
    """
    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        print(f"[OK] Datos guardados correctamente en '{ruta}'.")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")


def _parsear_fila(fila, numero_fila):
    """
    Convierte una fila del CSV en un diccionario con los tipos correctos.
    Devuelve None si la fila tiene errores de formato.

    Args:
        fila (dict): fila leída por csv.DictReader.
        numero_fila (int): número de fila (para mensajes de error).

    Retorna:
        dict | None: país parseado, o None si hay error.
    """
    try:
        nombre = fila["nombre"].strip()
        continente = fila["continente"].strip()

        if not nombre or not continente:
            raise ValueError("Nombre o continente vacío.")

        poblacion = int(fila["poblacion"].strip())
        superficie = int(fila["superficie"].strip())

        if poblacion < 0 or superficie < 0:
            raise ValueError("Población y superficie deben ser valores positivos.")

        return {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }

    except (ValueError, KeyError) as e:
        print(f"[AVISO] Fila {numero_fila} ignorada por error de formato: {e}")
        return None
