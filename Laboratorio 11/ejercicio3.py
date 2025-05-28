class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val                # Valor del nodo
        self.left = left              # Referencia al hijo izquierdo
        self.right = right            # Referencia al hijo derecho

# . Función para validar si el árbol es un BST
def is_valid_bst(root):
    # Función auxiliar que recorre el árbol recursivamente
    def helper(node, min_val, max_val):
        if not node:
            return True  # Un nodo nulo (árbol vacío) siempre es válido

        # Verificamos si el valor actual del nodo está fuera de los límites válidos
        if not (min_val < node.val < max_val):
            return False  # Si se viola la propiedad de BST, retornamos False

        # Repetimos la validación para el subárbol izquierdo y derecho
        # El valor actual del nodo se vuelve el nuevo límite superior/inferior
        return (helper(node.left, min_val, node.val) and
                helper(node.right, node.val, max_val))

    # Llamada inicial con los límites máximos posibles
    return helper(root, float('-inf'), float('inf'))

#  Construye un árbol binario a partir de una lista (orden por niveles)
def build_tree(values):
    if not values:
        return None  # Si la lista está vacía, retornamos None

    # Creamos nodos para cada valor (None queda como nodo vacío)
    nodes = [TreeNode(val) if val is not None else None for val in values]
    
    kids = nodes[::-1]    # Invertimos la lista para extraer nodos como si fuera una pila
    root = kids.pop()     # El primer nodo es la raíz del árbol

    # Asignamos hijos izquierdos y derechos a cada nodo
    for node in nodes:
        if node:
            if kids: 
                node.left = kids.pop()   # Asignar hijo izquierdo
            if kids: 
                node.right = kids.pop()  # Asignar hijo derecho
    return root

#  Árbol inválido: el hijo izquierdo es mayor que la raíz (violación de BST)
def build_invalid_tree1():
    root = TreeNode(5)         # Nodo raíz con valor 5
    root.left = TreeNode(6)    # Error: 6 > 5 (izquierdo inválido)
    root.right = TreeNode(7)   # Válido
    return root

#   Árbol inválido: el hijo derecho es menor que la raíz (violación de BST)
def build_invalid_tree2():
    root = TreeNode(5)         # Nodo raíz con valor 5
    root.left = TreeNode(3)    # Válido
    root.right = TreeNode(4)   # Error: 4 < 5 (derecho inválido)
    return root

#  Casos de prueba con impresión de resultados esperados
# Árbol:       5
#             / \
#            3   7
#           / \ / \
#          2  4 6  8   → Cumple con todas las reglas de BST
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)   # ✅ BST válido

# Árbol con violación en el lado izquierdo (6 > 5)
print(is_valid_bst(build_invalid_tree1()) == False)             # ❌ BST inválido

# Árbol con violación en el lado derecho (4 < 5)
print(is_valid_bst(build_invalid_tree2()) == False)             # ❌ BST inválido

# Árbol con un solo nodo: siempre es un BST válido
print(is_valid_bst(build_tree([42])) == True)                   # 🌱 Árbol válido

# Árbol vacío: se considera válido
print(is_valid_bst(None) == True)                               # 📭 Árbol vacío válido
