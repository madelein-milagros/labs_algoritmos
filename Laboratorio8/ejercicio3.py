from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        """Construye un árbol a partir de una lista de valores (nivel por nivel)."""
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        self.root = nodes[0]
        for i in range(len(nodes)):
            if nodes[i] is not None:
                left_idx = 2 * i + 1
                right_idx = 2 * i + 2
                if left_idx < len(nodes):
                    nodes[i].left = nodes[left_idx]
                if right_idx < len(nodes):
                    nodes[i].right = nodes[right_idx]

def vertical_order_traversal(root):
    """
    Devuelve una lista de listas con los nodos agrupados por columnas verticales.
    """
    if not root:
        return []

    column_table = defaultdict(list)  # Diccionario con clave columna, valores = nodos en esa columna
    queue = deque([(root, 0)])  # Cola para BFS: contiene pares (nodo, columna)

    while queue:
        node, column = queue.popleft()
        if node is not None:
            column_table[column].append(node.val)
            queue.append((node.left, column - 1))  # Izquierda es columna - 1
            queue.append((node.right, column + 1))  # Derecha es columna + 1

    # Ordenamos por columnas de menor a mayor
    sorted_columns = sorted(column_table.keys())
    return [column_table[col] for col in sorted_columns]

# --------------------------------------------------
# 🧪 CASOS DE PRUEBA
def test_vertical_order_traversal():
    print("▶ Ejecutando casos de prueba para vertical_order_traversal...\n")

    # Caso de prueba 1: Árbol binario normal
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    resultado1 = vertical_order_traversal(tree1.root)
    print("Caso 1: Esperado [[4], [2], [1, 5], [3], [6]]")
    print("Resultado:", resultado1, "\n")

    # Caso de prueba 2: Árbol de líneas verticales
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    resultado2 = vertical_order_traversal(tree2.root)
    print("Caso 2: Esperado [[3], [2], [1]]")
    print("Resultado:", resultado2, "\n")

# Ejecutar pruebas
test_vertical_order_traversal()
