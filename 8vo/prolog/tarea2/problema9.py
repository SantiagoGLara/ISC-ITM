# Se requiere un programa que, a partir del peso y la estatura de una persona, calcule el índice de masa corporal (IMC), determine la categoría correspondiente (Bajo peso, Normal, Sobrepeso u Obesidad) y finalmente retorne la clasificación obtenida. 

peso=int(input('ingrese peso: '))
estatura=float(input('ingrese estatura: '))

def categoria_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return "Bajo peso" if imc < 18.5 else \
           "Normal" if imc < 25 else \
           "Sobrepeso" if imc < 30 else "Obesidad"

print(categoria_imc(peso, estatura))