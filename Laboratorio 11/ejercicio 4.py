class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Asigna el valor al nodo
        self.left = left  # Apuntador al nodo izquierdo
        self.right = right  # Apuntador al nodo derecho

def kth_smallest(root, k):
    """Encuentra el k-ésimo elemento más pequeño en un BST"""
    if not root:  # Si el árbol está vacío, retornamos None
        return None
    
    count = 0  # Contador para rastrear cuántos nodos hemos visitado
    result = None  # Variable para almacenar el resultado

    def inorder_traversal(node):
        """Recorrido inorder para encontrar el k-ésimo elemento"""
        nonlocal count, result
        if not node or result is not None:  # Si el nodo es nulo o ya encontramos el resultado, terminamos
            return
        
        inorder_traversal(node.left)  # Recorremos el subárbol izquierdo primero
        
        count += 1  # Incrementamos el contador
        if count == k:  # Si hemos alcanzado el k-ésimo elemento
            result = node.val  # Almacenamos el valor y terminamos
            return
        
        inorder_traversal(node.right)  # Recorremos el subárbol derecho
    
    inorder_traversal(root)  # Llamamos al recorrido inorder para procesar los nodos
    return result  # Retornamos el k-ésimo elemento encontrado

# ✅ Función auxiliar para construir el BST desde una lista
def build_bst(values):
    if not values:  # Si la lista está vacía, retornamos None
        return None
    
    values.sort()  # Ordenamos los valores para formar un BST válido
    return sorted_list_to_bst(values, 0, len(values) - 1)  # Llamamos a la función auxiliar

def sorted_list_to_bst(values, left, right):
    if left > right:  # Caso base: si el índice izquierdo supera al derecho, retornamos None
        return None
    
    mid = (left + right) // 2  # Calculamos el punto medio de la lista ordenada
    node = TreeNode(values[mid])  # Creamos un nodo con el valor del medio
    node.left = sorted_list_to_bst(values, left, mid - 1)  # Construimos el subárbol izquierdo
    node.right = sorted_list_to_bst(values, mid + 1, right)  # Construimos el subárbol derecho
    return node  # Retornamos el nodo raíz del BST

# ✅ Casos de prueba
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)  # 🎯 Segundo más pequeño
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)  # 📊 Mínimo valor
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)  # 📈 Máximo valor
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)  # 🔗 Elemento del medio
print(kth_smallest(build_bst([10]), 1) == 10)  # 🌱 Nodo único
