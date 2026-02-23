# Se requiere un programa que, a partir de una cantidad en dólares, calcule su conversión a pesos mexicanos utilizando un tipo de cambio fijo, calcule el redondeo del resultado a dos decimales y finalmente retorne el valor convertido como una cadena formateada. 
moneda=int(input('ingrese cantidad en dolares: '))
def convertir_moneda(usd):
    res = usd * 18.50
    return f"${res:.2f}"

print(convertir_moneda(moneda))