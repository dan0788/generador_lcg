from src.lcg import lcg

def main():
    print("Generador Congruencial Lineal (LCG)")
    print("Ingrese los siguientes parámetros:")

    X0_input = input("Semilla inicial (X0): ")
    k_input = input("Coeficiente (k): ")
    g_input = input("Exponente del módulo (g): ")
    c_input = input("Constante aditiva (c): ")
    N_input = input("Número de iteraciones (N): ")

    try:
        a, m, sequence = lcg(X0_input, k_input, g_input, c_input, N_input)

        print("\nResultados:")
        print(f"Multiplicador (a): {a}")
        print(f"Módulo (m): {m}")
        print("Secuencia generada:")
        for i, val in enumerate(sequence):
            print(f"{i+1:>4} → {val}")

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()