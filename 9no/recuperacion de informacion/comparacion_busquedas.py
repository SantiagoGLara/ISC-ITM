import random
import time
import os

def generar_alumnos(cantidad):
    carreras = ["Sistemas", "Electronica", "Industrial", "Mecatronica"]
    with open("alumnos10000.dat", "w", encoding="utf-8") as archivo:
        for i in range(cantidad):
            control = 20260000 + i
            nombre = f"Alumno_{i}"
            carrera = random.choice(carreras)
            promedio = round(random.uniform(60, 100), 2)
            archivo.write(f"{control}|{nombre}|{carrera}|{promedio}\n")

def crear_indice():
    with open("alumnos10000.dat", "r", encoding="utf-8") as datos, \
         open("alumnos10000.idx", "w", encoding="utf-8") as indice:
        while True:
            posicion = datos.tell()
            linea = datos.readline()
            if not linea:
                break
            numero_control = linea.split("|")[0]
            indice.write(f"{numero_control}|{posicion}\n")

def busqueda_secuencial(numero_control):
    with open("alumnos.dat", "r", encoding="utf-8") as archivo:
        comparaciones = 0
        for linea in archivo:
            comparaciones += 1
            datos = linea.strip().split("|")
            if datos[0] == numero_control:
                return datos, comparaciones
    return None, comparaciones

def cargar_indice():
    indice = {}
    with open("alumnos.idx", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            control, posicion = linea.strip().split("|")
            indice[control] = int(posicion)
    return indice

def busqueda_indexada(numero_control, indice):
    if numero_control not in indice:
        return None
    posicion = indice[numero_control]
    with open("alumnos.dat", "r", encoding="utf-8") as archivo:
        archivo.seek(posicion)
        linea = archivo.readline()
        return linea.strip().split("|")

def ejecutar_pruebas():
    print("Generando 10,000 registros... esto tomará unos segundos.")
    generar_alumnos(10000)
    
    print("Creando archivo índice .idx...")
    crear_indice()
    
    print("Cargando índice en memoria (Diccionario)...")
    indice = cargar_indice()

    casos_prueba = {
        "Inicio": "20260001",
        "Mitad": "20265000",
        "Final": "20269999",
        "Inexistente": "99999999"
    }

    print("\n" + "="*75)
    print(f"{'Caso':<15} | {'Clave':<10} | {'T. Secuencial (s)':<17} | {'Comp.':<8} | {'T. Indexado (s)':<15}")
    print("-" * 75)

    for caso, clave in casos_prueba.items():
        # Ejecutar y medir búsqueda secuencial
        inicio_sec = time.perf_counter()
        _, comparaciones = busqueda_secuencial(clave)
        fin_sec = time.perf_counter()
        tiempo_sec = fin_sec - inicio_sec

        # Ejecutar y medir búsqueda indexada
        inicio_idx = time.perf_counter()
        _ = busqueda_indexada(clave, indice)
        fin_idx = time.perf_counter()
        tiempo_idx = fin_idx - inicio_idx

        # Imprimir fila de la tabla
        print(f"{caso:<15} | {clave:<10} | {tiempo_sec:<17.6f} | {comparaciones:<8} | {tiempo_idx:<15.6f}")

    print("="*75)

if __name__ == '__main__':
    ejecutar_pruebas()