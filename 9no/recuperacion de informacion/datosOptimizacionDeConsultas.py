import sqlite3
import time
import pandas as pd

conn = sqlite3.connect('biblioteca_optimizacion.sqlite')
cursor = conn.cursor()

queries = {
    "JOIN explicito": """
        SELECT p.id_prestamo, u.nombre AS usuario, l.titulo
        FROM prestamos AS p
        JOIN usuarios AS u ON u.id_usuario = p.id_usuario
        JOIN libros AS l ON l.id_libro = p.id_libro
        JOIN categorias AS c ON c.id_categoria = l.id_categoria
        WHERE c.nombre = 'Inteligencia Artificial'
          AND p.fecha_prestamo >= '2025-01-01';
    """,
    "Producto cartesiano": """
        SELECT p.id_prestamo, u.nombre AS usuario, l.titulo
        FROM prestamos AS p, usuarios AS u, libros AS l, categorias AS c
        WHERE u.id_usuario = p.id_usuario
          AND l.id_libro = p.id_libro
          AND c.id_categoria = l.id_categoria
          AND c.nombre = 'Inteligencia Artificial'
          AND p.fecha_prestamo >= '2025-01-01';
    """,
    "Subconsulta IN": """
        SELECT p.id_prestamo, u.nombre AS usuario, l.titulo
        FROM prestamos AS p
        JOIN usuarios AS u ON u.id_usuario = p.id_usuario
        JOIN libros AS l ON l.id_libro = p.id_libro
        WHERE l.id_categoria IN (
            SELECT id_categoria FROM categorias
            WHERE nombre = 'Inteligencia Artificial'
        )
        AND p.fecha_prestamo >= '2025-01-01';
    """
}

resultados = []


for nombre, sql in queries.items():
    tiempos = []
    filas = 0
    for _ in range(10):
        inicio = time.perf_counter()
        cursor.execute(sql)
        filas = len(cursor.fetchall()) # Contar registros
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000) 
    
    
    df_tiempos = pd.DataFrame(tiempos, columns=['ms'])
    
    resultados.append({
        'Consulta': nombre,
        'Filas': filas,
        'Promedio (ms)': df_tiempos['ms'].mean(),
        'Mediana (ms)': df_tiempos['ms'].median()
    })

df_final = pd.DataFrame(resultados)
print(df_final.to_markdown(index=False))

conn.close()