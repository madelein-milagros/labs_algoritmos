# Define a class for each node in the expression tree
class ExpressionNode:
    def __init__(self, value):
        self.value = value      # Node value (operator or operand)
        self.left = None        # Left child
        self.right = None       # Right child

    def is_leaf(self):
        # A node is a leaf if it has no children
        return self.left is None and self.right is None
# Define the expression tree class
class ExpressionTree:
    def __init__(self, root=None):
        self.root = root  # Root node of the tree

    # Method to simplify the expression tree
    def simplify(self):
        # Helper to check if a node value is a constant (number)
        def is_constant(value):
            try:
                float(value)  # Try converting to number
                return True
            except:
                return False  # If fails, it's a variable or operator

        # Helper to perform basic arithmetic operations
        def evaluate(op, a, b):
            a, b = float(a), float(b)  # Convert to float
            if op == '+': return str(int(a + b))
            elif op == '-': return str(int(a - b))
            elif op == '*': return str(int(a * b))
            elif op == '/': return str(int(a / b))

        # Recursive function to simplify the tree
        def simplify_node(node):
            if node is None or node.is_leaf():
                return node  # Base case: return if null or leaf node

            # Simplify left and right subtrees
            node.left = simplify_node(node.left)
            node.right = simplify_node(node.right)

            # If both children are constants, evaluate and replace node
            if (node.left and node.right and
                is_constant(node.left.value) and is_constant(node.right.value)):
                return ExpressionNode(evaluate(node.value, node.left.value, node.right.value))

            return node  # Return the node if not simplifiable

        # Start simplifying from the root
        self.root = simplify_node(self.root)


# ---------- TEST CASES BELOW ----------

# Test 1: (2 + 3) => 5
tree1 = ExpressionTree()
tree1.root = ExpressionNode('+')                   # Root node '+'
tree1.root.left = ExpressionNode('2')              # Left child 2
tree1.root.right = ExpressionNode('3')             # Right child 3
tree1.simplify()                                   # Simplify the tree
print("Test 1:", tree1.root.value == '5')          # Should print True

# Test 2: (2 + 3) * x => 5 * x
tree2 = ExpressionTree()
tree2.root = ExpressionNode('*')                   # Root node '*'
add = ExpressionNode('+')                          # Subtree for (2 + 3)
add.left = ExpressionNode('2')                     # Left operand
add.right = ExpressionNode('3')                    # Right operand
tree2.root.left = add                              # Set left subtree
tree2.root.right = ExpressionNode('x')             # Right child is variable 'x'
tree2.simplify()                                   # Simplify the tree
# Should print True if left subtree is simplified to '5' and right is 'x'
print("Test 2:", tree2.root.value == '*' and tree2.root.left.value == '5' and tree2.root.right.value == 'x')

# Test 3: x + y => No simplification possible
tree3 = ExpressionTree()
tree3.root = ExpressionNode('+')                   # Root node '+'
tree3.root.left = ExpressionNode('x')              # Left is variable 'x'
tree3.root.right = ExpressionNode('y')             # Right is variable 'y'
tree3.simplify()                                   # Simplify the tree (no change)
# Should print True if tree stays the same
print("Test 3:", tree3.root.value == '+' and tree3.root.left.value == 'x' and tree3.root.right.value == 'y')
