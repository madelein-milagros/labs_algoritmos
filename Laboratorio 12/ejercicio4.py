class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class AVLTree:
    def insert(self, root, key):
        if root is None:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    def is_avl_balanced(self, root):
        def check(node):
            if not node:
                return 0
            left_height = check(node.left)
            if left_height ==-1:
                return -1
            right_height =check(node.right)
            if right_height ==-1:
                return -1

            if abs(left_height - right_height)>1:
                return -1
            return max(left_height, right_height)+1
        return check(root) != -1
                

# 🧪 Test cases
def test_is_avl_balanced():
    avl = AVLTree()

    # Test 1: Balanced tree [20, 10, 30]
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1:", avl.is_avl_balanced(root) == True)  # ✅

    # Test 2: Manual unbalance (right-heavy)
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("🧪 Test 2:", avl.is_avl_balanced(unbalanced) == False)  # ⚠️

    # Test 3: Empty tree
    print("🧪 Test 3:", avl.is_avl_balanced(None) == True)  # 🌱

    # Test 4: Deep imbalance
    deep_unbalanced = AVLNode(10)
    deep_unbalanced.left = AVLNode(5)
    deep_unbalanced.left.left = AVLNode(2)
    deep_unbalanced.left.left.left = AVLNode(1)
    print("🧪 Test 4:", avl.is_avl_balanced(deep_unbalanced) == False)  # ❌

    # Test 5: Proper AVL-like shape (balanced)
    root2 = None
    for val in [50, 30, 70, 20, 40, 60, 80]:
        root2 = avl.insert(root2, val)
    print("🧪 Test 5:", avl.is_avl_balanced(root2) == True)  # ✅

# 🚀 Run tests
test_is_avl_balanced()
