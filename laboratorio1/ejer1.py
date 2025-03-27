ejercicio n:1
#ejercicio1
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import numpy as np


def logarithms(n):
    i = 1
    while i <= n:
        i = i * 2  # Se duplica en cada iteración (O(log n))

# Lista de valores de n
n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
times = []  # Lista para almacenar los tiempos de ejecución

# Medición del tiempo de ejecución para cada n
for n in n_values:
    start = timer()
    logarithms(n)
    end = timer()
    
    proc_time = end - start
    times.append(proc_time)

# Graficar los resultados
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='b', label="Tiempo de procesamiento")
plt.xscale('log')  # Escala logarítmica en el eje X
plt.xlabel("Valor de n (escala logarítmica)")
plt.ylabel("Tiempo de procesamiento (segundos)")
plt.title("Tiempo de procesamiento para O(log n)")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
