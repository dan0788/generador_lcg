from src.lcg import lcg
import tkinter as tk

def calcular_lcg():
    try:
        x0 = int(entry_X0_input.get())
        k = int(entry_k_input.get())
        c = int(entry_c_input.get())
        N = int(entry_N_input.get())
        
        a, m, sequence = lcg(x0,k,c,N)
        
        
        resultado_texto="Resultados:\n"
        resultado_texto+=f"Multiplicador (a): {a}\n"
        resultado_texto+=f"Módulo (m): {m}\n"
        resultado_texto+="Secuencia generada:\n"
        
        for i, val in enumerate(sequence):
            resultado_texto+=f"{i+1:>4} → {val}\n"
        
        label_resultado.config(text=resultado_texto)
    except ValueError as e:
        label_resultado.config(text=f"\nError: {e}")


def main():
    ventana=tk.Tk()
    ventana.title("Generador Congruencial Lineal (LCG)")
    # print("Generador Congruencial Lineal (LCG)")

    label_instruccion=tk.Label(ventana, text="Ingrese los siguientes parámetros:")
    label_instruccion.pack(pady=10)
    # print("Ingrese los siguientes parámetros:")

    label_X0_input=tk.Label(ventana, text="Semilla inicial (X0): ")
    label_X0_input.pack(pady=10)
    global entry_X0_input
    entry_X0_input=tk.Entry(ventana)
    entry_X0_input.pack(pady=10)
    #X0_input = input("Semilla inicial (X0): ")

    label_k_input=tk.Label(ventana, text="Coeficiente (k): ")
    label_k_input.pack(pady=10)
    global entry_k_input
    entry_k_input=tk.Entry(ventana)
    entry_k_input.pack(pady=10)
    #k_input = input("Coeficiente (k): ")

    label_c_input=tk.Label(ventana, text="Constante aditiva (c): ")
    label_c_input.pack(pady=10)
    global entry_c_input
    entry_c_input=tk.Entry(ventana)
    entry_c_input.pack(pady=10)
    #c_input = input("Constante aditiva (c): ")

    label_N_input=tk.Label(ventana, text="Número de iteraciones (N): ")
    label_N_input.pack(pady=10)
    global entry_N_input
    entry_N_input=tk.Entry(ventana)
    entry_N_input.pack(pady=10)
    #N_input = input("Número de iteraciones (N): ")

    # x0=int(entry_X0_input.get())
    # k=int(entry_k_input.get())
    # c=int(entry_c_input.get())
    # N=int(entry_N_input.get())

    button=tk.Button(ventana, text="Calcular", command=calcular_lcg)
    button.pack(pady=10)

    global label_resultado
    label_resultado=tk.Label(ventana, text="")
    label_resultado.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()