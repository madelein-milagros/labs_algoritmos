#ejercicio 02
#correcto

import timeit
import matplotlib.pyplot as plt

def simple_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

n_values = [10**2, 10**3, 10**4, 10**5, 10**6]
times = []

for n in n_values:
    start_time = timeit.default_timer()
    simple_loop(n)
    end_time = timeit.default_timer()
    times.append(end_time - start_time)

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'ro-')
plt.xscale('log')
plt.xlabel('n (log scale)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Complejidad O(n)')
plt.grid(True)
plt.show()
