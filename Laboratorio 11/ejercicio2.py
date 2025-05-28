class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_from_list(self, values):
        """Builds BST from a list of values."""
        for value in values:
            self.insert(value)

    def insert(self, value):
        """Inserts a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Helper method to insert recursively."""
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

    def find_lca(self, val1, val2):
        """Finds the lowest common ancestor of two values."""
        def lca(node):
            if node is None:
                return None
            # If both values are less than current node's value, LCA is in left subtree
            if val1 < node.value and val2 < node.value:
                return lca(node.left)
            # If both values are greater than current node's value, LCA is in right subtree
            if val1 > node.value and val2 > node.value:
                return lca(node.right)
            # If values diverge, current node is the LCA
            return node

        ancestor = lca(self.root)
        return ancestor.value if ancestor else None

# 🧪 Test cases
def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("Test 1:", bst1.find_lca(2, 8) == 6)

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("Test 2:", bst2.find_lca(0, 4) == 2)

    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("Test 3:", bst3.find_lca(2, 3) == 2)

    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("Test 4:", bst4.find_lca(5, 5) == 5)

    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("Test 5:", bst5.find_lca(1, 3) == 2)

# 🚀 Run all tests
test_find_lca()
