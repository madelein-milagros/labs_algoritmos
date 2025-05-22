# Definición de la clase Node que representa un nodo en el árbol de expresiones
class Node:
    def __init__(self, value):
        self.value = value      # Valor del nodo (número u operador)
        self.left = None        # Hijo izquierdo
        self.right = None       # Hijo derecho

# Función para evaluar un árbol de expresiones y devolver el resultado
def evaluate_expression_tree(root):
    """Evaluate an expression tree and return the result"""

    # Caso base: si el nodo no tiene hijos, es una hoja (número), se convierte a entero y se retorna
    if root.left is None and root.right is None:
        return int(root.value)  # Convertimos de string a entero

    # Llamadas recursivas para evaluar el subárbol izquierdo y derecho
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)

    # Se evalúa el nodo actual aplicando el operador correspondiente a los valores izquierdo y derecho
    if root.value == '+':
        return left_val + right_val  # Suma
    elif root.value == '-':
        return left_val - right_val  # Resta
    elif root.value == '*':
        return left_val * right_val  # Multiplicación
    elif root.value == '/':
        return left_val // right_val  # División entera
    else:
        raise ValueError(f"Operador desconocido: {root.value}")  # Error si el operador no es válido

# ----------------------------------------
# Casos de prueba para validar la función
# ----------------------------------------

# Test 1: Suma simple
# Árbol:    +
#          / \
#         2   3
# Resultado esperado: 5
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(evaluate_expression_tree(node1) == 5)  # ➕ Suma básica

# Test 2: Multiplicación
# Árbol:    *
#          / \
#         4   5
# Resultado esperado: 20
node2 = Node('*')
node2.left = Node('4')
node2.right = Node('5')
print(evaluate_expression_tree(node2) == 20)  # ✖️ Multiplicación

# Test 3: Operaciones combinadas
# Árbol:    +
#          / \
#         2   *
#            / \
#           3   4
# Resultado esperado: 14 (2 + (3 * 4))
node3 = Node('+')
node3.left = Node('2')
node3.right = Node('*')
node3.right.left = Node('3')
node3.right.right = Node('4')
print(evaluate_expression_tree(node3) == 14)  # 🔢 Operaciones combinadas

# Test 4: División
# Árbol:    /
#          / \
#         8   4
# Resultado esperado: 2
node4 = Node('/')
node4.left = Node('8')
node4.right = Node('4')
print(evaluate_expression_tree(node4) == 2)  # ➗ División entera

# Test 5: Árbol complejo con múltiples operaciones
# Árbol:        *
#             /   \
#            +     -
#           / \   / \
#          1   2 8   3
# Resultado esperado: (1 + 2) * (8 - 3) = 3 * 5 = 15
node5 = Node('*')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('1')
node5.left.right = Node('2')
node5.right.left = Node('8')
node5.right.right = Node('3')
print(evaluate_expression_tree(node5) == 15)  # 🧮 Cálculo complejo
