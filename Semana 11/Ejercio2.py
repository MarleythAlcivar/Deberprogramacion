# Definimos una matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [9, 8, 7],   # Primera fila
    [6, 5, 4],   # Segunda fila
    [3, 2, 1]    # Tercera fila
]

# Función para ordenar una fila específica de la matriz en orden ascendente
def ordenar_fila(matriz, fila):
    # Utilizamos el método sort() para ordenar la fila seleccionada
    matriz[fila].sort()
    # Retornamos la matriz con la fila ordenada
    return matriz

# Mostramos la matriz original antes de la ordenación
print("Matriz original:")
for fila in matriz:
    print(fila)

# Solicitamos al usuario que ingrese el número de la fila que desea ordenar
fila_a_ordenar = int(input("Ingresa el número de la fila a ordenar (0-2): "))

# Llamamos a la función para ordenar la fila seleccionada
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz después de ordenar la fila seleccionada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)


