class AVLNode:
    def __init__(self, key):
        """🌱 Constructor para crear un nodo AVL"""
        self.key = key  # Valor del nodo
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho
        self.height = 1  # Altura del nodo (inicialmente 1)

class AVLTree:
    def get_height(self, node):
        """📏 Retorna la altura de un nodo"""
        return node.height if node else 0

    def get_balance(self, node):
        """⚖️ Calcula el factor de balance (altura izquierda - altura derecha)"""
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        """🔄 Rotación derecha (LL Case)"""
        x = y.left
        T2 = x.right

        # Realiza la rotación
        x.right = y
        y.left = T2

        # Actualiza alturas
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x  # Nueva raíz

    def rotate_left(self, x):
        """🔄 Rotación izquierda (RR Case)"""
        y = x.right
        T2 = y.left

        # Realiza la rotación
        y.left = x
        x.right = T2

        # Actualiza alturas
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y  # Nueva raíz

    def insert(self, root, key):
        """🌱 Inserta un nodo y rebalancea el árbol AVL"""
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Aplicar rotaciones si el árbol está desbalanceado
        if balance > 1 and key < root.left.key:  # LL Case
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:  # RR Case
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:  # LR Case
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:  # RL Case
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder(self, root):
        """📜 Recorrido in-order (izquierda, raíz, derecha)"""
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

def is_balanced(root):
    """✅ Verifica si el árbol es un AVL válido"""
    if not root:
        return True
    
    balance = abs(AVLTree().get_balance(root))
    
    if balance > 1:
        return False
    
    return is_balanced(root.left) and is_balanced(root.right)

# 🧪 Test con validación
def test_avl_balance():
    avl = AVLTree()
    root = None
    for val in [10, 20, 30]:
        root = avl.insert(root, val)
    print("Test 1 (RR) Balanceado:", is_balanced(root))  # Expected: True

    avl = AVLTree()
    root = None
    for val in [30, 20, 10]:
        root = avl.insert(root, val)
    print("Test 2 (LL) Balanceado:", is_balanced(root))  # Expected: True

    avl = AVLTree()
    root = None
    for val in [30, 10, 20]:
        root = avl.insert(root, val)
    print("Test 3 (LR) Balanceado:", is_balanced(root))  # Expected: True

    avl = AVLTree()
    root = None
    for val in [10, 30, 20]:
        root = avl.insert(root, val)
    print("Test 4 (RL) Balanceado:", is_balanced(root))  # Expected: True

    avl = AVLTree()
    root = None
    for val in [15, 10, 20, 25, 30]:
        root = avl.insert(root, val)
    print("Test 5 (Balanced) Balanceado:", is_balanced(root))  # Expected: True

# 🚀 Ejecutar validaciones
test_avl_balance()
