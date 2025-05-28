class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_from_list(self, values):
        """Construye un BST a partir de una lista de valores."""
        for value in values:
            self.insert(value)

    def insert(self, value):
        """Inserta un valor en el BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Inserción recursiva en el BST."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def is_valid_bst(self):
        """Verifica si el árbol es un BST válido."""
        def validate(node, min_val, max_val):
            # Un nodo nulo es válido
            if node is None:
                return True
            # El valor del nodo debe estar dentro del rango (min_val, max_val)
            if not (min_val < node.value < max_val):
                return False
            # Validar recursivamente los subárboles izquierdo y derecho
            return (validate(node.left, min_val, node.value) and
                    validate(node.right, node.value, max_val))
        # Iniciar la validación desde la raíz con el rango infinito
        return validate(self.root, float('-inf'), float('inf'))

def test_is_valid_bst():
    bst1 = BinarySearchTree()
    bst1.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("Test 1:", bst1.is_valid_bst() == True)  # Árbol válido

    bst2 = BinarySearchTree()
    bst2.root = Node(5)
    bst2.root.left = Node(6)  # Violación: izquierdo > raíz
    bst2.root.right = Node(7)
    print("Test 2:", bst2.is_valid_bst() == False)  # Violación en el lado izquierdo

    bst3 = BinarySearchTree()
    bst3.root = Node(5)
    bst3.root.left = Node(3)
    bst3.root.right = Node(4)  # Violación: derecho < raíz
    print("Test 3:", bst3.is_valid_bst() == False)  # Violación en el lado derecho

    bst4 = BinarySearchTree()
    bst4.build_from_list([42])
    print("Test 4:", bst4.is_valid_bst() == True)  # Árbol con un solo nodo

    bst5 = BinarySearchTree()
    print("Test 5:", bst5.is_valid_bst() == True)  # Árbol vacío

# Ejecutar los casos de prueba
test_is_valid_bst()
