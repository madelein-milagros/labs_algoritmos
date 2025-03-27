##03
import matplotlib.pyplot as plt
import timeit

def if_then_else(n):
    for i in range(n):
        if i % 2 == 0:
            pass
        else:
            pass

n_values = [1, 10, 100, 1000, 10000, 100000]
times = [timeit.timeit(lambda: if_then_else(n), number=10) for n in n_values]


plt.plot(n_values, times, marker="o", label="O(n)")
plt.xlabel("n")
plt.ylabel("Tiempo (s)")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.title("Tiempo de ejecución para O(n) con if-then-else")
plt.show()
