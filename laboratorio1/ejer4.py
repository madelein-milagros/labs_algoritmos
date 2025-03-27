#04
import time
import matplotlib.pyplot as plt

# Función para analizar la complejidad O(n^2) con bucles anidados
def nested_loops(n):
    count = 0
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            count += (i + j) % 3  # Variación en la operación matemática
    return count

n_values = [100, 200, 400, 600, 800, 1000, 1100]
times = []

for n in n_values:
    start_time = time.perf_counter()
    nested_loops(n)
    end_time = time.perf_counter()
    times.append(end_time - start_time)

plt.figure(figsize=(8,5))
plt.plot(n_values, times, marker="o", color="green", linestyle="-", linewidth=1.5, label="O(n²) execution time")
plt.xlabel("n (input size)")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs Input Size (O(n²) Complexity)")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
