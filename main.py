def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return f"Valor {valor_buscado} encontrado en la posición ({i}, {j})"
    return f"Valor {valor_buscado} no encontrado"

# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor = 5
resultado = buscar_valor(matriz, valor)
print(resultado)
