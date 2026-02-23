# Se requiere un programa que, a partir de una cantidad de minutos, calcule cuántas horas completas contiene, calcule los minutos restantes y finalmente retorne el tiempo en formato de cadena "HH:MM". 
tiempo=int(input('ingrese minutos: '))
def convertir_tiempo(m):
    h, mins = m // 60, m % 60
    return f"{h:02d}:{mins:02d}"

print(convertir_tiempo(tiempo))