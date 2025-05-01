def suma(nombre, *numeros):
    return f"{nombre}, la suma es: {sum(numeros)}"

resultado = suma("Steven", 5,10,15,20)
print(resultado)