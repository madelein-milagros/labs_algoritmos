class GenericTreeNode:
    """Representa un nodo en un árbol genérico"""
    def __init__(self, value):
        self.value = value  # Almacena el valor del nodo
        self.children = []  # Lista para almacenar referencias a los nodos hijos

class GenericTree:
    """Implementación de un árbol genérico"""
    def __init__(self, root=None):
        self.root = root  # Inicializa la raíz del árbol
    
    def find_leaves(self):
        """Encuentra todos los nodos hoja en el árbol"""
        def collect_leaves(node):
            if not node:  # Si el nodo es None (árbol vacío), devuelve una lista vacía
                return []
            if not node.children:  # Si el nodo no tiene hijos, es una hoja
                return [node.value]  # Agrega el valor del nodo hoja a la lista
            leaves = []  # Inicializa una lista vacía para almacenar los nodos hoja
            for child in node.children:  # Itera recursivamente sobre cada hijo
                leaves.extend(collect_leaves(child))  # Recoge las hojas del subárbol
            return leaves  # Devuelve los valores de las hojas recolectadas

        return collect_leaves(self.root)  # Comienza la búsqueda recursiva desde la raíz

# ✅ Casos de prueba
# Prueba 1: Árbol vacío
empty_tree = GenericTree(None)  # Crea un árbol vacío sin raíz
print(empty_tree.find_leaves() == [])  # Salida esperada: [] (no hay hojas en el árbol)

# Prueba 2: Un solo nodo (la raíz es hoja)
single = GenericTree(GenericTreeNode('X'))  # Crea un árbol con un solo nodo 'X'
print(single.find_leaves() == ['X'])  # Salida esperada: ['X'] (la raíz es una hoja)

# Prueba 3: Árbol lineal A → B → C
linear_root = GenericTreeNode('A')  # Nodo raíz 'A'
linear_b = GenericTreeNode('B')  # Nodo hijo 'B'
linear_c = GenericTreeNode('C')  # Nodo hijo 'C'
linear_root.children = [linear_b]  # 'A' tiene un hijo: 'B'
linear_b.children = [linear_c]  # 'B' tiene un hijo: 'C'
linear_tree = GenericTree(linear_root)  # Crea el árbol con la raíz 'A'
print(linear_tree.find_leaves() == ['C'])  # Salida esperada: ['C'] (el último nodo es una hoja)

# Prueba 4: Múltiples hojas
tree_root = GenericTreeNode('A')  # Nodo raíz 'A'
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')  # Hijos de 'A'
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')  # Hojas
tree_root.children = [b, c, d]  # Asigna hijos a 'A'
b.children = [e, f, g]  # Asigna hojas a 'B'
d.children = [h]  # Asigna hoja a 'D'
tree = GenericTree(tree_root)  # Crea el árbol
print(sorted(tree.find_leaves()) == ['C', 'E', 'F', 'G', 'H'])  # Salida esperada: todas las hojas ordenadas

# Prueba 5: Árbol ancho
wide_root = GenericTreeNode('A')  # Nodo raíz 'A'
wide_root.children = [GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D'), 
                        GenericTreeNode('E'), GenericTreeNode('F')]  # Hijos directos (todos hojas)
wide_tree = GenericTree(wide_root)  # Crea el árbol
print(sorted(wide_tree.find_leaves()) == ['B', 'C', 'D', 'E', 'F'])  # Salida esperada: todas las hojas ordenadas