from collections import defaultdict, deque

# Definition of a binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function to perform vertical order traversal of a binary tree
def vertical_order_traversal(root):
    if not root:
        return []  # If the tree is empty, return an empty list

    column_table = defaultdict(list)  # Dictionary to hold nodes by column index
    queue = deque([(root, 0)])  # Queue for BFS: stores (node, column index)

    while queue:
        node, column = queue.popleft()  # Dequeue a node and its column index
        if node:
            column_table[column].append(node.val)  # Append node value to its column
            queue.append((node.left, column - 1))  # Enqueue left child with column - 1
            queue.append((node.right, column + 1))  # Enqueue right child with column + 1

    # Sort the columns from leftmost to rightmost
    sorted_columns = sorted(column_table.items())
    return [vals for col, vals in sorted_columns]  # Return only the values per column

# Example binary tree:
#        3
#       / \
#      9   8
#     / \ / \
#    4  0 1  7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)

# Perform vertical order traversal
result = vertical_order_traversal(root)
print(result)  # Output: [[4], [9], [3, 0, 1], [8], [7]]
