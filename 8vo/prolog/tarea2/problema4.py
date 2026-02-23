# Se requiere un programa que calcule el salario neto de un empleado tomando en cuenta las horas trabajadas y el pago por hora, aplique un impuesto del 13% al salario y descuente una quinta parte para el fondo de ahorro del empleado, y finalmente retorne su sueldo neto (después de impuestos y descuentos).

def calcular_neto(horas, pago_hora):
    bruto = horas * pago_hora
    despues_iva = bruto * 0.87 
    ahorro = despues_iva / 5    
    return despues_iva - ahorro

h = float(input("Horas trabajadas: "))
p = float(input("Pago por hora: "))
print(f"Sueldo neto: ${calcular_neto(h, p):.2f}")