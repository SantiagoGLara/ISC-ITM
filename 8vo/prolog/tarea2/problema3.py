#  Se requiere un programa que calcule si un número es positivo, negativo o cero, retornando solamente la cadena: Positivo, Negativo o Cero. 

numero=float(input('numero: '))

mayor = "cero" if numero == 0 else "negativo" if numero < 0 else "positivo"
print(mayor)