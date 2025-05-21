def infix_to_postfix(tokens):
    """Convertir una expresión infija a notación postfix"""
    
    # Diccionario que define la precedencia de los operadores
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    output = []  # Donde almacenamos la salida en formato postfix
    stack = []   # Pila temporal para operadores y paréntesis

    for token in tokens:
        # Caso 1: Si el token es un operando (número o variable)
        if token.isalnum():
            output.append(token)

        # Caso 2: Si el token es un paréntesis abierto '('
        elif token == '(':
            stack.append(token)

        # Caso 3: Si el token es un paréntesis cerrado ')'
        elif token == ')':
            # Sacar elementos hasta encontrar el '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Eliminar el '(' de la pila (no se agrega al output)

        # Caso 4: Si el token es un operador (+, -, *, /)
        else:
            # Desapilar operadores con mayor o igual precedencia
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                output.append(stack.pop())
            stack.append(token)

    # Al final, desapilamos todos los operadores restantes
    while stack:
        output.append(stack.pop())

    return output
# Test 1: Suma simple
# Infix: 2 + 3 → Postfix: ['2', '3', '+']
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # True

# Test 2: Prioridad de operadores
# Infix: 2 + 3 * 4 → Postfix: ['2', '3', '4', '*', '+']
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # True

# Test 3: Paréntesis cambia prioridad
# Infix: (2 + 3) * 4 → Postfix: ['2', '3', '+', '4', '*']
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # True

# Test 4: Expresión compleja con paréntesis
# Infix: (1 + 2) * (3 - 4) → Postfix: ['1', '2', '+', '3', '4', '-', '*']
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # True

# Test 5: Variables con operadores
# Infix: a + b * c / d → Postfix: ['a', 'b', 'c', '*', 'd', '/', '+']
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # True
