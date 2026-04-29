# Replace the "ANSWER HERE" for your answer

def collatz_steps(n):
    """
    Retorna la cantidad de pasos necesarios para llegar a 1
    siguiendo la conjetura de Collatz:
      - Si n es par: n = n // 2
      - Si n es impar: n = 3 * n + 1

    n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

    Ejemplo: collatz_steps(6) -> 8
      6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
    """
    count = 0
    if n == 1 :
        return count
    else:
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            elif n % 2 != 0:
                n = 3 * n + 1
                count += 1
        return count



def collatz_sequence(n):
    """
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    list = [n]
    if n == 1:
        return list
    else:
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                list.append(n)
            elif n % 2 != 0:
                n = 3 * n + 1
                list.append(n)
        return list
