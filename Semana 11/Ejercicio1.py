#Se declara una matriz 3*3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Se declara una funcion que recibe una matriz y un valor para buscar en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
           #Se compara y la matriz es igual al valor que buscamos
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado"


valor = int(input("Ingresa el valor a buscar: "))
resultado = buscar_valor(matriz, valor)
print(resultado)
