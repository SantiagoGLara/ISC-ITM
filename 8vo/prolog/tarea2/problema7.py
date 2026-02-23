# Se requiere un programa que, a partir de una cantidad en dólares, calcule su conversión a pesos mexicanos utilizando un tipo de cambio fijo, calcule el redondeo del resultado a dos decimales y finalmente retorne el valor convertido como una cadena formateada. 

calificacion=int(input('ingrese calificacion: '))

def calificar(n):
    if n < 70: return "F"
    return "A" if n >= 90 else ("B" if n >= 80 else "C")

print(calificar(calificacion))