# Define a class to represent a node in a binary tree
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value      # The value stored in the current node
        self.left = left        # Reference to the left child node
        self.right = right      # Reference to the right child node

# Define a function that mirrors (reverses) a binary tree
def mirror_tree(node):
    if node is None:
        return None  # Base case: if the node is empty, return None (do nothing)

    # Recursively mirror the right subtree and assign it to the left
    # Recursively mirror the left subtree and assign it to the right
    node.left, node.right = mirror_tree(node.right), mirror_tree(node.left)

    return node  # Return the current node (now with swapped children)

# Helper function to print the tree values using in-order traversal (left-root-right)
def print_in_order(node):
    if node:
        print_in_order(node.left)       # Recursively print the left subtree
        print(node.value, end=' ')      # Print the current node's value
        print_in_order(node.right)      # Recursively print the right subtree

# Entry point of the program
if __name__ == "__main__":

    root = TreeNode(1)  # Root node with value 1
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))  # Left subtree
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))  # Right subtree

    print("Original tree (in-order):")
    print_in_order(root)  # Print the original tree in in-order format

    mirror_tree(root)  # Perform the mirroring operation on the tree

    print("\nMirrored tree (in-order):")
    print_in_order(root)  # Print the mirrored tree in in-order format
