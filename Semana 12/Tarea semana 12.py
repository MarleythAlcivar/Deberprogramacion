# Matriz 3D con las temperaturas diarias
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

# Iterar sobre las ciudades
for i in range(len(temperaturas)):
    print(f"\nPromedios de temperatura para {ciudades[i]}:")

    # Iterar sobre las semanas de la ciudad i
    for j in range(len(temperaturas[i])):
        suma_temperaturas = 0

        # Iterar sobre los días de la semana j de la ciudad i
        for k in range(len(temperaturas[i][j])):
            suma_temperaturas += temperaturas[i][j][k]  # Sumar las temperaturas del día k

        # Calcular el promedio de la semana j de la ciudad i
        promedio_semana = suma_temperaturas / len(temperaturas[i][j])
        print(f"  Semana {j + 1}: {promedio_semana:.2f}°C")
