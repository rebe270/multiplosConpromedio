from datetime import datetime

def multiplos_cuatro_cifras(dia):
    # Encontrar los primeros tres múltiplos de 4 cifras del día
    multiplos = []
    num = 1000  # Inicia con el primer número de 4 cifras
    while len(multiplos) < 3:
        if num % dia == 0:
            multiplos.append(num)
        num += 1
    return multiplos

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Obtener el día actual
dia_actual = datetime.now().day

# Encontrar los múltiplos y calcular el promedio
multiplos = multiplos_cuatro_cifras(dia_actual)
promedio = calcular_promedio(multiplos)

# Imprimir resultados
print(f"El primer múltiplo de 4 cifras del día {dia_actual} es: {multiplos[0]}")
print(f"El segundo múltiplo de 4 cifras del día {dia_actual} es: {multiplos[1]}")
print(f"El tercer múltiplo de 4 cifras del día {dia_actual} es: {multiplos[2]}")
print(f"El promedio de los tres múltiplos es: {promedio}")
