class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Asigna el valor al nodo
        self.left = left  # Apuntador al nodo izquierdo
        self.right = right  # Apuntador al nodo derecho

class DoublyLinkedListNode:
    def __init__(self, val=0):
        self.val = val  # Asigna el valor al nodo de la lista doblemente enlazada
        self.prev = None  # Apuntador al nodo anterior
        self.next = None  # Apuntador al nodo siguiente

def bst_to_dll(root):
    """Convierte un BST a una lista doblemente enlazada circular"""
    if not root:  # Si el árbol está vacío, retornamos None
        return None
    
    first, last = None, None  # Variables para rastrear el primer y último nodo de la lista

    def inorder_traversal(node):
        """Recorrido inorder para construir la lista doblemente enlazada"""
        nonlocal first, last
        if not node:  # Si el nodo es nulo, terminamos la función
            return
        
        inorder_traversal(node.left)  # Recorremos el subárbol izquierdo primero
        
        new_node = DoublyLinkedListNode(node.val)  # Creamos un nuevo nodo para la lista
        if last:  # Si hay un nodo previo en la lista
            last.next = new_node  # Enlazamos el nodo anterior con el nuevo nodo
            new_node.prev = last  # Enlazamos el nuevo nodo con el nodo anterior
        else:
            first = new_node  # Si es el primer nodo, lo guardamos
        
        last = new_node  # Actualizamos el último nodo en la lista
        
        inorder_traversal(node.right)  # Recorremos el subárbol derecho
    
    inorder_traversal(root)  # Llamamos al recorrido inorder para procesar todos los nodos
    
    first.prev = last  # Conectamos el primer nodo con el último
    last.next = first  # Conectamos el último nodo con el primero para hacerlo circular
    
    return first  # Retornamos la cabeza de la lista circular

# ✅ Función auxiliar para validar la lista doblemente enlazada circular
def validate_circular_dll(head, expected_values):
    """Verifica que la DLL tenga los valores esperados en orden y sea circular"""
    if not head:  # Si la cabeza es nula, validamos que la lista esperada esté vacía
        return expected_values == []
    
    values = []  # Lista para almacenar los valores de la lista enlazada
    current = head  # Empezamos desde el primer nodo
    while True:
        values.append(current.val)  # Agregamos el valor a la lista
        current = current.next  # Avanzamos al siguiente nodo
        if current == head:  # Si volvemos al inicio, significa que es circular
            break
    
    return values == expected_values  # Comparamos con la lista esperada

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
head1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗 Conversión simple

head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 📊 Conversión compleja

head3 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(head3, [5]) == True)  # 🌱 Nodo único

head4 = bst_to_dll(build_bst([1, 2, 3, 4]))
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Caso degenerado

head5 = bst_to_dll(None)
print(head5 is None)  # 📭 Árbol vacío
