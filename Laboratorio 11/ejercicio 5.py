# 🌳 Nodo del Árbol
class Node:
    def __init__(self, value):
        self.value = value  # Almacena el valor del nodo
        self.left = None  # Inicializa la referencia al hijo izquierdo como None
        self.right = None  # Inicializa la referencia al hijo derecho como None

# 🌲 Clase del Árbol Binario de Búsqueda
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Inicializa el árbol sin nodos (vacío)

    def insert(self, value):
        if not self.root:  # Si el árbol está vacío, el nuevo nodo será la raíz
            self.root = Node(value)
        else:
            self._insert(self.root, value)  # Inserta el valor en la posición correcta

    def _insert(self, node, value):
        if value < node.value:  # Si el valor es menor, va al subárbol izquierdo
            if node.left:
                self._insert(node.left, value)  # Llama recursivamente si hay un nodo izquierdo
            else:
                node.left = Node(value)  # Crea un nuevo nodo en el lado izquierdo
        else:  # Si el valor es mayor o igual, va al subárbol derecho
            if node.right:
                self._insert(node.right, value)  # Llama recursivamente si hay un nodo derecho
            else:
                node.right = Node(value)  # Crea un nuevo nodo en el lado derecho

    def build_from_list(self, values):
        for value in values:
            self.insert(value)  # Construye el árbol a partir de una lista de valores

    def bst_to_dll(self):
        """🔁 Convierte el BST a una lista doblemente enlazada circular ordenada"""
        def inorder(node):
            nonlocal last, first
            if not node:
                return
            # 1. Procesar el subárbol izquierdo
            inorder(node.left)

            # 2. Procesar el nodo actual
            if last:
                last.right = node  # Conectar el nodo previo con el actual
                node.left = last  # Conectar el nodo actual con el previo
            else:
                first = node  # Definir el primer nodo de la lista

            last = node  # Actualizar el último nodo visitado

            # 3. Procesar el subárbol derecho
            inorder(node.right)

        if not self.root:
            return None  # Si el árbol está vacío, devuelve None

        first, last = None, None
        inorder(self.root)  # Ejecutar recorrido en orden

        # 🔁 Hacer la lista circular
        first.left = last  # Conectar el primer nodo con el último
        last.right = first  # Conectar el último nodo con el primero

        return first  # 🎉 Retorna la cabeza de la lista doblemente enlazada circular

# ✅ Validador de la lista doblemente enlazada circular
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []  # Si la cabeza es None, verificar lista vacía
    values = []  # Lista para almacenar valores ordenados
    current = head
    while True:
        values.append(current.value)  # Agregar el valor del nodo actual a la lista
        current = current.right  # Moverse al siguiente nodo
        if current == head:  # Si volvemos al primer nodo, hemos recorrido toda la lista
            break
    return values == expected_values  # Comprobar si los valores coinciden con lo esperado

# 🧪 Casos de prueba
def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print(" Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗 Verifica la conversión correcta

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print(" Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 🌳 Estructura más compleja

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print(" Test 3:", validate_circular_dll(head3, [5]) == True)  # 🌱 Árbol con un solo nodo

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print(" Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Árbol degenerado (lista)

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print(" Test 5:", head5 is None)  # 📭 Árbol vacío, debe devolver None

# 🚀 Ejecutar pruebas
test_bst_to_dll()  # Llama a la función de prueba para validar la conversión


