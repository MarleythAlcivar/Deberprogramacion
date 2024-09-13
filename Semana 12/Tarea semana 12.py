


def calcular_promedio_ciudades(temperaturas, ciudades):
    promedios_por_ciudad = {}  # Diccionario donde se almacenarán los promedios por ciudad.

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
        promedios_por_ciudad[ciudades[i]] = promedio_ciudad  # Almacenamos el promedio en el diccionario con la ciudad como clave.

    return promedios_por_ciudad  # Devolvemos el diccionario con los promedios de todas las ciudades.

# Datos de ejemplo:
# 'temperaturas' es una lista que contiene, para cada ciudad, otra lista con las temperaturas registradas semana por semana.
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

# 'ciudades' es una lista que contiene los nombres de las ciudades correspondientes a las temperaturas.
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Llamamos a la función para obtener el promedio de temperatura de cada ciudad
promedios = calcular_promedio_ciudades(temperaturas, ciudades)

# Imprimimos los promedios de cada ciudad
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es {promedio:.2f}°C")  # Formateamos el promedio a 2 decimales.
