from collections import deque

# Definición del nodo del árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Función para recorrido por niveles (level-order traversal)
def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # Inicia la cola con el nodo raíz

    while queue:
        current = queue.popleft()       # Saca el nodo actual
        result.append(current.value)    # Agrega su valor al resultado

        # Encola los hijos del nodo actual
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print("Recorrido por niveles:", level_order_traversal(root))
