from collections import deque  # Import deque to use an efficient queue

# Define the class for a binary tree node
class TreeNode:
    def __init__(self, value):
        self.val = value          # Node's value
        self.left = None          # Left child
        self.right = None         # Right child

# Function to perform level order traversal
def level_order_traversal(root):
    if not root:
        return []  # If the tree is empty, return an empty list

    result = []  # This list will store the values of the nodes level by level
    queue = deque([root])  # Use a queue to process nodes, starting with the root

    while queue:
        level = []  # Temporary list to store the values of the current level
        level_length = len(queue)  # Number of nodes at the current level

        for _ in range(level_length):  # Iterate over all nodes at this level
            node = queue.popleft()     # Remove the current node from the queue
            level.append(node.val)     # Add its value to the current level list

            if node.left:              # If the node has a left child
                queue.append(node.left)  # Add it to the queue for the next level
            if node.right:             # If the node has a right child
                queue.append(node.right)  # Also add it to the queue

        result.append(level)  # Add the complete level list to the final result

    return result  # Return the list of lists with values level by level
root = TreeNode(1)              # Root node
root.left = TreeNode(2)         # Left child of root
root.right = TreeNode(3)        # Right child of root
root.left.left = TreeNode(4)    # Left child of node 2
root.left.right = TreeNode(5)   # Right child of node 2
root.right.right = TreeNode(6)  # Right child of node 3

# Call the function and print the result
print(level_order_traversal(root))  # Output: [[1], [2, 3], [4, 5, 6]]


