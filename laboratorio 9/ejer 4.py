class GenericTreeNode:
    """Represents a node in a generic tree"""
    def __init__(self, value):
        self.value = value  # Stores the value of the node
        self.children = []  # List to store references to child nodes

class GenericTree:
    """Generic tree implementation"""
    def __init__(self, root=None):
        self.root = root  # Initializes the root of the tree
    
    def find_leaves(self):
        """Finds all leaf nodes in the tree"""
        def collect_leaves(node):
            if not node:  # If the node is None (empty tree), return an empty list
                return []
            if not node.children:  # If the node has no children, it's a leaf
                return [node.value]  # Add the leaf node's value to the list
            leaves = []  # Initialize an empty list to store leaf nodes
            for child in node.children:  # Recursively iterate over each child
                leaves.extend(collect_leaves(child))  # Collect leaves from the subtree
            return leaves  # Return the collected leaf values

        return collect_leaves(self.root)  # Start the recursive search from the root

# ✅ Test cases
# Test 1: Empty tree
empty_tree = GenericTree(None)  # Create an empty tree with no root
print(empty_tree.find_leaves() == [])  # Expected output: [] (no leaves in the tree)

# Test 2: Single node (root is leaf)
single = GenericTree(GenericTreeNode('X'))  # Create a tree with a single node 'X'
print(single.find_leaves() == ['X'])  # Expected output: ['X'] (root itself is a leaf)

# Test 3: Linear tree A → B → C
linear_root = GenericTreeNode('A')  # Root node 'A'
linear_b = GenericTreeNode('B')  # Child node 'B'
linear_c = GenericTreeNode('C')  # Child node 'C'
linear_root.children = [linear_b]  # 'A' has one child: 'B'
linear_b.children = [linear_c]  # 'B' has one child: 'C'
linear_tree = GenericTree(linear_root)  # Create tree with the root 'A'
print(linear_tree.find_leaves() == ['C'])  # Expected output: ['C'] (last node is a leaf)

# Test 4: Multiple leaves
tree_root = GenericTreeNode('A')  # Root node 'A'
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')  # Children of 'A'
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')  # Leaves
tree_root.children = [b, c, d]  # Assign children to 'A'
b.children = [e, f, g]  # Assign leaves to 'B'
d.children = [h]  # Assign leaf to 'D'
tree = GenericTree(tree_root)  # Create tree
print(sorted(tree.find_leaves()) == ['C', 'E', 'F', 'G', 'H'])  # Expected output: all leaf nodes sorted

# Test 5: Wide tree
wide_root = GenericTreeNode('A')  # Root node 'A'
wide_root.children = [GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D'), 
                        GenericTreeNode('E'), GenericTreeNode('F')]  # Direct children (all leaves)
wide_tree = GenericTree(wide_root)  # Create the tree
print(sorted(wide_tree.find_leaves()) == ['B', 'C', 'D', 'E', 'F'])  # Expected output: all leaves sorted

