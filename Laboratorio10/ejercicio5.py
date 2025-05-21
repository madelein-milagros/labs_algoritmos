# ----------------------------------
# Definición de la estructura del árbol
# ----------------------------------
class Node:
    """
    Clase que representa un nodo en el árbol de expresiones matemáticas.
    Cada nodo puede ser un operador (+, -, *, /), un número o una variable.
    """
    def __init__(self, value):
        self.value = value      # Valor del nodo (operador, número o variable)
        self.left = None        # Referencia al hijo izquierdo
        self.right = None       # Referencia al hijo derecho
# ----------------------------------
# Función para verificar si un string es un número
# ----------------------------------
def is_number(s):
    """
    Función que determina si el string `s` es un número válido.
    Devuelve True si puede convertirse a float, de lo contrario False.
    """
    try:
        float(s)  # Intentamos convertir el valor a float
        return True  # Si la conversión es exitosa, `s` es un número
    except ValueError:
        return False  # Si ocurre un error, `s` no es un número
# ----------------------------------
# Función para evaluar una operación matemática
# ----------------------------------

def evaluate(op, left, right):
    """
    Recibe un operador (`op`) y dos operandos (`left` y `right`), los evalúa y retorna el resultado.
    """
    left = float(left)  # Convertimos el operando izquierdo a float
    right = float(right)  # Convertimos el operando derecho a float

    # Realizamos la operación según el operador
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right
    else:
        raise ValueError("Operador no soportado: " + op)

    # Si el resultado es entero, lo convertimos a int para evitar ".0"
    return str(int(result)) if result.is_integer() else str(result)
# ----------------------------------
# Función para simplificar el árbol de expresión matemática
# ----------------------------------

def simplify_expression_tree(root):
    """
    Simplifica un árbol de expresión matemática evaluando operaciones en nodos con valores numéricos.
    Si el nodo contiene operadores con hijos numéricos, evalúa la expresión y retorna un nodo simplificado.
    """
    if root is None:
        return None  # Si el nodo es None, se retorna None

    # Simplificamos recursivamente el subárbol izquierdo
    root.left = simplify_expression_tree(root.left)
    # Simplificamos recursivamente el subárbol derecho
    root.right = simplify_expression_tree(root.right)

    # Si ambos hijos son números, evaluamos la operación y retornamos un nodo nuevo con el resultado
    if root.left and root.right and is_number(root.left.value) and is_number(root.right.value):
        return Node(evaluate(root.value, root.left.value, root.right.value))

    # Si no se puede simplificar, devolvemos el nodo tal cual
    return root
# ----------------------------------
# Función para imprimir el árbol en formato visual
# ----------------------------------

def print_tree(node, indent=""):
    """
    Imprime el árbol de manera visual para una mejor comprensión de la estructura.
    """
    if node is not None:
        print_tree(node.right, indent + "   ")  # Primero imprimimos el subárbol derecho con indentación
        print(indent + node.value)  # Imprimimos el valor del nodo actual
        print_tree(node.left, indent + "   ")  # Luego imprimimos el subárbol izquierdo
# ----------------------------------
# TESTS: Validamos la funcionalidad de la simplificación
# ----------------------------------

# Test 1: Suma de constantes, debería simplificarse a '5'
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)  # True

# Test 2: Mezcla de variable y constante, no debe simplificarse
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')  # True

# Test 3: Árbol con solo constantes, debería simplificarse completamente a '11'
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '11' and result3.left is None and result3.right is None)  # True

# Test 4: Solo variables, no debe simplificarse
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')  # True

# Test 5: Simplificación parcial, lado izquierdo debe simplificarse pero el derecho no (porque tiene variables)
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(
    result5.value == '+' and 
    result5.left.value == '5' and 
    result5.left.left is None and 
    result5.left.right is None and 
    result5.right.value == '*' and 
    result5.right.left.value == 'z' and 
    result5.right.right.value == '4'
)  # True
