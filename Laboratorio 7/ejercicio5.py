class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
def is_balanced(root):
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)

def test_is_balanced():
    # Test Case 1: Balanced tree
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)
    
    # Test Case 2: Empty tree (trivially balanced)
    empty_tree = None
    
    # Test Case 3: Single node tree (trivially balanced)
    single_node = TreeNode(1)
    
    # Test Case 4: Unbalanced tree - left-heavy
    unbalanced_left = TreeNode(1)
    unbalanced_left.left = TreeNode(2)
    unbalanced_left.left.left = TreeNode(3)
    unbalanced_left.left.left.left = TreeNode(4)
    
    # Test Case 5: Just balanced on the edge case
    edge_balanced = TreeNode(1)
    edge_balanced.left = TreeNode(2)
    edge_balanced.right = TreeNode(3)
    edge_balanced.left.left = TreeNode(4)
    edge_balanced.left.right = TreeNode(5)
    edge_balanced.left.left.left = TreeNode(6)
    
    print("Test 1:", is_balanced(balanced))        # True
    print("Test 2:", is_balanced(empty_tree))      # True
    print("Test 3:", is_balanced(single_node))     # True
    print("Test 4:", is_balanced(unbalanced_left)) # False
    print("Test 5:", is_balanced(edge_balanced))   # True

test_is_balanced()
