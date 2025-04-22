from collections import deque

# Definition of the binary tree node
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Function for level-order traversal
def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()  # Remove the first node from the queue
        result.append(node.val)  # Process the node

        # Add its children (if they exist)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Test the function
if __name__ == "__main__":
    # Create a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Level-order traversal:", level_order_traversal(root))
    # Expected output: [1, 2, 3, 4, 5, 6]
