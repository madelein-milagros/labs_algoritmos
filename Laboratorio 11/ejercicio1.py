class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value  # Inicializa un nodo con un valor dado
            self.left = None  # Inicializa la referencia al hijo izquierdo como None
            self.right = None  # Inicializa la referencia al hijo derecho como None

    def __init__(self):
        self.root = None  # Inicializa el árbol con una raíz vacía

    def insert(self, value):
        if self.root is None:  # Si el árbol está vacío, el nuevo nodo será la raíz
            self.root = self.Node(value)
        else:
            self._insert(self.root, value)  # Inserta el valor en la posición correcta

    def _insert(self, node, value):
        if value < node.value:  # Si el valor es menor, va al subárbol izquierdo
            if node.left is None:
                node.left = self.Node(value)  # Crea un nuevo nodo en el lado izquierdo
            else:
                self._insert(node.left, value)  # Llama recursivamente para insertar en la izquierda
        else:  # Si el valor es mayor o igual, va al subárbol derecho
            if node.right is None:
                node.right = self.Node(value)  # Crea un nuevo nodo en el lado derecho
            else:
                self._insert(node.right, value)  # Llama recursivamente para insertar en la derecha

    def build_from_list(self, values):
        for value in values:
            self.insert(value)  # Construye el árbol a partir de una lista de valores

    def range_query(self, min_val, max_val):
        """🎯 Encuentra todos los valores dentro del rango dado"""
        result = []  # Lista para almacenar los valores dentro del rango
        self._inorder_range(self.root, min_val, max_val, result)  # Llama al recorrido en orden
        return result  # Devuelve los valores encontrados

    def _inorder_range(self, node, min_val, max_val, result):
        if node is None:
            return  # Si el nodo es nulo, no hay nada que procesar

        if node.value > min_val:
            self._inorder_range(node.left, min_val, max_val, result)  # Explora el subárbol izquierdo si es necesario

        if min_val <= node.value <= max_val:
            result.append(node.value)  # Agrega el valor si está dentro del rango

        if node.value < max_val:
            self._inorder_range(node.right, min_val, max_val, result)  # Explora el subárbol derecho si es necesario

# 🧪 Casos de prueba
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print(" Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # Verifica si los valores en el rango son correctos

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print(" Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # Otro caso de prueba con diferentes valores

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print(" Test 3:", bst3.range_query(1, 5) == [])  # Debe devolver una lista vacía si no hay valores dentro del rango

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print(" Test 4:", bst4.range_query(10, 20) == [15])  # Comprueba con un solo nodo en el árbol

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print(" Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # Verifica múltiples valores en el rango

# 🚀 Ejecutar todas las pruebas
test_range_query()  # Llama a la función de prueba para comprobar la implementación

