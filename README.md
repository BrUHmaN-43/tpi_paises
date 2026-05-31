# 🌍 Gestión de Datos de Países en Python

Trabajo Práctico Integrador (TPI) — Programación 1  
Tecnicatura Universitaria en Programación — UTN

---

## Profesores

| Nombre completo |
|----------------|
| Ariel Enferrel |
| Martín A. Garcia |
| Cinthia Rigoni |

---

## Descripción

Aplicación de consola desarrollada en Python 3 que permite gestionar un dataset de países.
El sistema lee y escribe datos desde un archivo CSV, y ofrece funcionalidades de búsqueda,
filtrado, ordenamiento y estadísticas.

---

## Integrantes

| Nombre completo | Comisión | DNI |
|-----------------|----------|--------|
| Salcedo Scardino Julián | M26 C1-16 | 47975164 |
| Suarez Taboada Mateo Ezequiel | M26 C1-03 | 45243284 |

---

## Requisitos

- Python 3.x instalado
- No requiere librerías externas

---

## Estructura del proyecto

```
tpi_paises/
├── main.py            # Menú principal
├── carga.py           # Lectura y escritura del CSV
├── operaciones.py     # Agregar, actualizar, buscar y eliminar países
├── filtros.py         # Filtrar por continente, población y superficie
├── ordenamiento.py    # Ordenar por nombre, población o superficie
├── estadisticas.py    # Estadísticas del dataset
└── paises.csv         # Dataset base de países
```

---

## Cómo ejecutar

1. Clonar o descargar el repositorio
2. Abrir una terminal dentro de la carpeta `tpi_paises`
3. Ejecutar el siguiente comando:

```bash
python main.py
```

---

## Funcionalidades

- ➕ **Agregar** un país con nombre, población, superficie y continente
- ✏️ **Actualizar** población y superficie de un país existente
- 🔍 **Buscar** países por nombre (coincidencia parcial o exacta)
- 🗑️ **Eliminar** un país con confirmación
- 🔎 **Filtrar** por continente, rango de población o rango de superficie
- 📊 **Ordenar** por nombre, población o superficie (ascendente o descendente)
- 📈 **Estadísticas**: mayor/menor población, promedios y cantidad por continente

---

## Ejemplos de uso

### Agregar un país
```
--- AGREGAR PAÍS ---
Nombre del país: Paraguay
Población: 7353038
Superficie en km²: 406752
Continente: América
[OK] País 'Paraguay' agregado correctamente.
```

### Buscar un país
```
--- BUSCAR PAÍS ---
Ingresá el nombre o parte del nombre: arg
Se encontraron 1 resultado(s):
  Nombre:      Argentina
  Población:   45,376,763
  Superficie:  2,780,400 km²
  Continente:  América
```

### Ver estadísticas
```
── Población ──────────────────────────────────
  País más poblado:    China                  1,412,600,000 hab.
  País menos poblado:  Uruguay                    3,473,730 hab.
  Promedio:                                     166,666,666 hab.

── Países por continente ──────────────────────
  África           4 país/es
  América          7 país/es
  Asia             5 país/es
  Europa           7 país/es
  Oceanía          2 país/es
```

---

## Links

- 📹 Video demostración: (agregar link)
- 📄 Documentación PDF: (agregar link)

---

## Bibliografía

- Documentación oficial de Python 3: https://docs.python.org/3/
- Módulo csv de Python: https://docs.python.org/3/library/csv.html
