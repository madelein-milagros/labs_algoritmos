class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.key} ", end="")
            self.inorder(root.right)

    # 🌳 Check if tree is AVL balanced and BST
    def is_balanced_avl(self, root):
        def check(node):
            if not node:
                return True, -1
            left_balanced, left_height = check(node.left)
            right_balanced, right_height = check(node.right)

            balance = left_height - right_height
            is_balanced = left_balanced and right_balanced and abs(balance) <= 1
            is_bst = (not node.left or node.left.key < node.key) and \
                     (not node.right or node.right.key > node.key)
            height = 1 + max(left_height, right_height)
            return is_balanced and is_bst, height

        balanced, _ = check(root)
        return balanced

# 🧪 Tests
def test_avl_delete():
    avl = AVLTree()
    root = None
    for val in [20, 10, 30, 25, 35]:
        root = avl.insert(root, val)

    root = avl.delete(root, 35)
    print(avl.is_balanced_avl(root))  # Test 1

    root = avl.delete(root, 25)
    print(avl.is_balanced_avl(root))  # Test 2

    root = avl.delete(root, 20)
    print(avl.is_balanced_avl(root))  # Test 3

    root = avl.delete(root, 30)
    print(avl.is_balanced_avl(root))  # Test 4

    root = avl.delete(root, 10)
    print(avl.is_balanced_avl(root))  # Test 5 (tree should be empty or one node)

# 🚀 Run
test_avl_delete()
