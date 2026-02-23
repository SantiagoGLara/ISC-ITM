# problema 1: Precio, descuento e IVA

def calcular_iva(precio):
    return precio * 1.16

def calcular_descuento(cantidad, porcentaje):
    return cantidad * (porcentaje / 100)

def precio_total(precio, porcentaje_descuento):
    con_iva = calcular_iva(precio)
    descuento_aplicado = calcular_descuento(con_iva, porcentaje_descuento)
    return con_iva - descuento_aplicado

def main():
    precio = float(input('Precio: '))
    porcentaje = float(input('Descuento: '))
    
    resultado = precio_total(precio, porcentaje)
    print(f"El precio total es: {resultado:.2f}")

main()