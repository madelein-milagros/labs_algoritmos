class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value  # Almacena el valor del nodo
            self.left = None  # Inicializa la referencia al hijo izquierdo como None
            self.right = None  # Inicializa la referencia al hijo derecho como None

    def __init__(self):
        self.root = None  # Inicializa el árbol sin nodos (vacío)

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

    def kth_smallest(self, k):
        """📊 Encuentra el k-ésimo elemento más pequeño en el BST sin convertirlo en un arreglo"""
        def inorder(node):
            nonlocal count, result
            if not node or result is not None:  # Terminar si no hay nodo o ya encontramos el resultado
                return

            inorder(node.left)  # Recorrer el subárbol izquierdo primero
            
            count += 1  # Incrementar contador cuando visitamos un nodo
            if count == k:  # Si el contador alcanza k, guardamos el resultado
                result = node.value
                return
            
            inorder(node.right)  # Recorrer el subárbol derecho
        
        count, result = 0, None  # Inicializar el contador y el resultado
        inorder(self.root)  # Iniciar recorrido desde la raíz
        return result  # Retornar el valor k-ésimo más pequeño

# 🧪 Casos de prueba
def test_kth_smallest():
    bst1 = BinarySearchTree()
    bst1.build_from_list([3, 1, 4, 2])
    print(" Test 1:", bst1.kth_smallest(2) == 2)  # 🎯 Segundo menor

    bst2 = BinarySearchTree()
    bst2.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print(" Test 2:", bst2.kth_smallest(1) == 2)  # 📉 El primero (mínimo)

    print(" Test 3:", bst2.kth_smallest(7) == 8)  # 📈 El último (máximo)

    bst3 = BinarySearchTree()
    bst3.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print(" Test 4:", bst3.kth_smallest(4) == 4)  # 🔗 Elemento en la mitad

    bst4 = BinarySearchTree()
    bst4.build_from_list([10])
    print(" Test 5:", bst4.kth_smallest(1) == 10)  # 🌱 Único nodo

# 🚀 Ejecutar pruebas
test_kth_smallest()  # Llama a la función de prueba para validar la implementación
