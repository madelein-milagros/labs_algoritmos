from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def print_level_order(self, root):
        """📡 Level-order print with heights"""
        if not root:
            return

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(f"{node.val}(h{node.height})")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(", ".join(level_nodes))

# 🧪 Test it!
def test_level_order_heights():
    avl = AVLTree()
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)

    print("🧪 Test 1–5: Expected output:")
    # Expected:
    # 10(h3)
    # 5(h2), 15(h1)
    # 2(h1), 7(h1)
    avl.print_level_order(root)

# 🚀 Go!
test_level_order_heights()
