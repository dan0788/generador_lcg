def lcg(X0, k, g, c, N):
    """
    Genera una secuencia de números pseudoaleatorios utilizando el Generador Congruencial Lineal (LCG).

    Args:
        X0: Semilla inicial (entero, 0 <= X0 < m).
        k: Coeficiente (entero >= 0).
        g: Exponente del módulo (entero >= 1).
        c: Constante aditiva (entero, 0 <= c < m).
        N: Número de iteraciones (entero, 1 <= N <= 10000).

    Returns:
        tuple: Una tupla conteniendo:
            - a: El valor del multiplicador.
            - m: El valor del módulo.
            - sequence: Una lista de los N números generados.
    """
    try:
        X0 = int(X0)
        k = int(k)
        g = int(g)
        c = int(c)
        N = int(N)
    except ValueError:
        raise ValueError("Error: Todas las entradas deben ser enteros.")

    m = 2**g
    a = 1 + 4 * k

    if not (0 <= X0 < m):
        raise ValueError(f"Error: La semilla X0 ({X0}) debe estar en el rango [0, {m-1}].")
    if k < 0:
        raise ValueError(f"Error: El coeficiente k ({k}) debe ser mayor o igual a 0.")
    if g < 1:
        raise ValueError(f"Error: El exponente del módulo g ({g}) debe ser mayor o igual a 1.")
    if not (0 <= c < m):
        raise ValueError(f"Error: La constante aditiva c ({c}) debe estar en el rango [0, {m-1}].")
    if not (1 <= N <= 10000):
        raise ValueError(f"Error: El número de iteraciones N ({N}) debe estar en el rango [1, 10000].")

    sequence = []
    x = X0
    for i in range(N):
        x = (a * x + c) % m
        sequence.append(x)

    return a, m, sequence

if __name__ == "__main__":
    # Ejemplo de uso (para probar la función directamente)
    try:
        a_val, m_val, result_sequence = lcg(X0=5, k=3, g=4, c=1, N=10)
        print(f"Multiplicador (a): {a_val}")
        print(f"Módulo (m): {m_val}")
        print("Secuencia generada:")
        for i, val in enumerate(result_sequence):
            print(f"{i+1:>4} → {val}")
    except ValueError as e:
        print(e)