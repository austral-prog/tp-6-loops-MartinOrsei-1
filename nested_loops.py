# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []

    for sublista in matrix:
        for elemento in sublista:
            lista.append(elemento)
    return lista


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lista = []

    for sublista in matrix:
        elemento2 = 0
        for elemento in sublista:
            elemento2 += elemento
        lista.append(elemento2)
    return lista





def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    num_columnas = len(matrix[0])
    num_filas = len(matrix)
    lista = []
    for j in range(num_columnas):
        sum= 0
        for i in range(num_filas):
            sum += matrix[i][j]
        lista.append(sum)
    return lista

