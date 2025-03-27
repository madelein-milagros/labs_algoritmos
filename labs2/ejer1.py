#Problem 1 FACTORIAL
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# using
if __name__ == "__main__":
    print(factorial(8))  # Salida esperada: 40320

