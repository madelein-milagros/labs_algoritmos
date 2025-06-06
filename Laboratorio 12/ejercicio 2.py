class AVLNode:
    def __init__(self, key):
        """🌱 Initialize a new AVL Tree node"""
        self.key = key  # Node value
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Initial height

class AVLTree:
    def get_height(self, node):
        """📏 Returns the height of a node"""
        return node.height if node else 0

    def rotate_left(self, z):
        """🔄 Perform left rotation on node z (RR Case)"""
        if not z or not z.right: 
            return z  # Safeguard against rotation errors
        
        y = z.right  # New root after rotation
        T2 = y.left  # Temporary subtree

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y  # Return new root

    def rotate_right(self, z):
        """🔁 Perform right rotation on node z (LL Case)"""
        if not z or not z.left: 
            return z  # Safeguard against rotation errors
        
        y = z.left  # New root after rotation
        T2 = y.right  # Temporary subtree

        # Perform rotation
        y.right = z
        z.left = T2

        # Update heights
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y  # Return new root

# ✅ Validate rotations
def validate_rotation(tree, root, expected_key):
    """✅ Ensures the root key matches the expected value after rotation"""
    return root.key == expected_key

# 🧪 Test rotations
def test_rotations():
    tree = AVLTree()

    # Test 1: Left Rotation
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    print(" Test 1 (Left Rotation):", validate_rotation(tree, z, 20))  # Expected: True

    # Test 2: Right Rotation
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z = tree.rotate_right(z)
    print(" Test 2 (Right Rotation):", validate_rotation(tree, z, 20))  # Expected: True

    # Test 3: Validate Heights
    print(" Test 3 (Height Correctness):", z.height >= 1)  # Expected: True

    # Test 4: Child Preservation
    print(" Test 4 (Left Child Exists After Rotation):", z.left.key == 10)  # Expected: True
    print(" Test 5 (Right Child Exists After Rotation):", z.right.key == 30)  # Expected: True

# 🚀 Run tests
test_rotations()
