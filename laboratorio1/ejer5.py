#05
import time
import matplotlib.pyplot as plt

# Función Consecutive Statements O(n + n²) ≈ O(n²)
def consecutive_statements(n):
    count = 0
    for _ in range(n):  # O(n)
        count += 1  # Simple incremento
    for i in range(n):  # O(n²)
        for j in range(n):
            count += (i * j) % 2  # Cambio en la operación para diferenciación
    return count

n_values = [100, 200, 400, 600, 800, 1000, 1100]
times = []

for n in n_values:
    start_time = time.perf_counter()
    consecutive_statements(n)
    end_time = time.perf_counter()
    times.append(end_time - start_time)

plt.figure(figsize=(8,5))
plt.plot(n_values, times, marker="o", color="blue", linestyle="-", linewidth=1.5, label="O(n²) execution time")
plt.xlabel("n (input size)")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs Input Size (O(n) + O(n²))")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
