def infix_to_postfix(tokens):
    """Convertir una expresión infija a notación postfix"""

    # Diccionario que define la precedencia de cada operador
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    output = []  # Lista donde almacenaremos la expresión en postfix
    stack = []   # Pila para guardar operadores temporalmente

    for token in tokens:
        if token.isalnum():  
            # Si el token es un operando (número o variable), agregarlo directamente al output
            output.append(token)
        elif token == '(':
            # Si es un paréntesis abierto, simplemente apilarlo
            stack.append(token)
        elif token == ')':
            # Si es un paréntesis cerrado, sacar operadores hasta encontrar el '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())  # Sacar operadores y agregarlos al output
            stack.pop()  # Remover el '(' de la pila sin agregarlo al output
        else:
            # Si es un operador (+, -, *, /)
            # Mientras haya operadores en la pila con mayor o igual precedencia,
            # sacarlos y ponerlos en output antes de apilar el nuevo operador
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                output.append(stack.pop())
            stack.append(token)  # Apilar el operador actual

    # Una vez procesados todos los tokens, sacar los operadores restantes de la pila
    while stack:
        output.append(stack.pop())

    return output


# Pruebas para verificar que la función funciona correctamente
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # True - Suma simple
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # True - Prioridad multiplicación
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # True - Paréntesis cambia prioridad
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # True - Expresión compleja con paréntesis
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # True - Variables con operadores

