def calcular_promedio_ciudades(temperaturas, ciudades):
    promedios = []  # Lista para almacenar los promedios de cada ciudad.

    # Iterar sobre las ciudades
    for i in range(len(temperaturas)):  # 'i' representa el índice de la ciudad.
        suma_total = 0  # Inicializamos la suma de las temperaturas para cada ciudad.
        dias_totales = 0  # Inicializamos el contador de días totales de esa ciudad.

        # Iterar sobre las semanas de la ciudad 'i'
        for j in range(len(temperaturas[i])):  # 'j' representa el índice de la semana dentro de la ciudad 'i'.
            suma_total += sum(temperaturas[i][j])  # Suma todas las temperaturas de la semana 'j' para la ciudad 'i'.
            dias_totales += len(temperaturas[i][j])  # Cuenta cuántos días tiene la semana 'j'.

        # Calcular el promedio de temperatura de la ciudad 'i'
        promedio_ciudad = suma_total / dias_totales  # Promedio = Suma total de temperaturas / Total de días
        promedios.append(promedio_ciudad)  # Almacenamos el promedio en la lista.

    return promedios  # Devolvemos la lista con los promedios de todas las ciudades.

# Datos de ejemplo:
# 'temperaturas' es una lista que contiene, para cada ciudad, otra lista con las temperaturas registradas semana por semana.
temperaturas = [
    [
        [30, 31, 29, 32, 33, 31, 30],  # Quito, Semana 1
        [29, 30, 31, 30, 32, 29, 31],  # Quito, Semana 2
        [28, 29, 30, 32, 31, 30, 29]   # Quito, Semana 3
    ],
    [
        [25, 26, 27, 24, 28, 26, 27],  # Manta , Semana 1
        [26, 27, 25, 28, 27, 29, 26],  # Manta, Semana 2
        [27, 28, 26, 25, 29, 28, 27]   # Manta, Semana 3
    ],
    [
        [18, 19, 17, 20, 21, 18, 19],  # Santo domingo , Semana 1
        [19, 20, 21, 20, 22, 19, 18],  # Santo domingo, Semana 2
        [20, 21, 19, 22, 21, 20, 21]   # Santo domingo, Semana 3
    ]
]

# 'ciudades' es una lista que contiene los nombres de las ciudades correspondientes a las temperaturas.
ciudades = ["Quito", "Manta", "Santo domingo"]

# Llamamos a la función para obtener el promedio de temperatura de cada ciudad
promedios = calcular_promedio_ciudades(temperaturas, ciudades)

# Imprimimos los promedios de cada ciudad
for i in range(len(ciudades)):
    print(f"El promedio de temperatura en {ciudades[i]} es {promedios[i]:.2f}°C")  # Formateamos el promedio a 2 decimales.
