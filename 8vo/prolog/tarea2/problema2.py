# Se requiere un programa que, a partir de la edad del usuario, retorne un valor falso si es menor de edad y, si es mayor de edad, calcule su año de nacimiento. 

from datetime import datetime

validar_edad = lambda edad: (datetime.now().year - edad) if edad >= 18 else False

edad = int(input("Ingrese su edad: "))
print(f"Resultado: {validar_edad(edad)}")