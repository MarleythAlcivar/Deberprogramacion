"""Tarea: Iteración de arreglos multidimensionales con bucles anidados

1 Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
2 Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
3 Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
4 Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla."""

# 1.- Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
# Matriz tridimencional con temperatudas de ciudades
# La temperatura esta en °C

# 2.- Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
temperatura_ciudades = [
    [
        # L   M   M   J   V   S   D
        [30, 31, 29, 32, 33, 31, 30],  # Quito, Semana 1
        [29, 30, 31, 30, 32, 29, 31],  # Quito, Semana 2
        [28, 29, 30, 32, 31, 30, 29]  # Quito, Semana 3
    ],
    [
        [25, 26, 27, 24, 28, 26, 27],  # Manta, Semana 1
        [26, 27, 25, 28, 27, 29, 26],  # Manta, Semana 2
        [27, 28, 26, 25, 29, 28, 27]  # Manta, Semana 3
    ],
    [
        [18, 19, 17, 20, 21, 18, 19],  # Santo domingo, Semana 1
        [19, 20, 21, 20, 22, 19, 18],  # Santo domingo, Semana 2
        [20, 21, 19, 22, 21, 20, 21]  # Santo domingo, Semana 3
    ]
]

# 3.- Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
# Calcular y mostrar promedios para Quito
print('Promedios de temperatura para Quito:')
for semana in range(len(temperatura_ciudades[0])):
    suma_temperatura = 0
    for dia in temperatura_ciudades[0][semana]:
        suma_temperatura += dia
    promedio = suma_temperatura / len(temperatura_ciudades[0][semana])
    print(f'  Semana {semana + 1}: {promedio:.2f}°C')

# Calcular y mostrar promedios para Manta
print('Promedios de temperatura para Manta:')
for semana in range(len(temperatura_ciudades[1])):
    suma_temperatura = 0
    for dia in temperatura_ciudades[1][semana]:
        suma_temperatura += dia
    promedio = suma_temperatura / len(temperatura_ciudades[1][semana])
    print(f'  Semana {semana + 1}: {promedio:.2f}°C')

# Calcular y mostrar promedios para Santo Domingo
print('Promedios de temperatura para Santo Domingo:')
for semana in range(len(temperatura_ciudades[2])):
    suma_temperatura = 0
    for dia in temperatura_ciudades[2][semana]:
        suma_temperatura += dia
    promedio = suma_temperatura / len(temperatura_ciudades[2][semana])
    print(f'  Semana {semana + 1}: {promedio:.2f}°C')

