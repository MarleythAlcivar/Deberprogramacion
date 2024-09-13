def calcular_promedio_ciudades(temperaturas, ciudades):
    promedios_por_ciudad = {}

    # Iterar sobre las ciudades
    for i in range(len(temperaturas)):
        suma_total = 0
        dias_totales = 0

        # Iterar sobre las semanas de la ciudad i
        for j in range(len(temperaturas[i])):
            suma_total += sum(temperaturas[i][j])  # Sumar todas las temperaturas de la semana
            dias_totales += len(temperaturas[i][j])  # Contar los días de la semana

        # Calcular el promedio de la ciudad i
        promedio_ciudad = suma_total / dias_totales
        promedios_por_ciudad[ciudades[i]] = promedio_ciudad

    return promedios_por_ciudad


# Datos de ejemplo
temperaturas = [
    [
        [30, 31, 29, 32, 33, 31, 30],  # Ciudad 1, Semana 1
        [29, 30, 31, 30, 32, 29, 31]  # Ciudad 1, Semana 2
    ],
    [
        [25, 26, 27, 24, 28, 26, 27],  # Ciudad 2, Semana 1
        [26, 27, 25, 28, 27, 29, 26]  # Ciudad 2, Semana 2
    ],
    [
        [18, 19, 17, 20, 21, 18, 19],  # Ciudad 3, Semana 1
        [19, 20, 21, 20, 22, 19, 18]  # Ciudad 3, Semana 2
    ]
]

ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Llamar a la función y obtener el promedio de cada ciudad
promedios = calcular_promedio_ciudades(temperaturas, ciudades)

# Imprimir los resultados
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es {promedio:.2f}°C")
