class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None
class ExpressionTree:
    """Expression tree implementation"""
    def __init__(self, root=None):
        self.root = root
    def simplify(self):
        """Simplify the expression tree by evaluating constants"""
        def simplify_node(node):
            if node is None or node.is_leaf():
                return node
            node.left = simplify_node(node.left)
            node.right = simplify_node(node.right)

            if node.left and node.right:
                try:
                    left_val = float(node.left.value)
                    right_val = float(node.right.value)
                    if node.value == '+':
                        result = left_val + right_val
                    elif node.value == '-':
                        result = left_val - right_val
                    elif node.value == '*':
                        result = left_val * right_val
                    elif node.value == '/':
                        result = left_val / right_val
                    else:
                        return node  # operador desconocido

                    # Convertir a entero si no hay decimales
                    new_value = str(int(result)) if result.is_integer() else str(result)
                    return ExpressionNode(new_value)
                except ValueError:
                    pass  # No se puede convertir, hay variables
            return node

        self.root = simplify_node(self.root)


# ✅ Test cases
# Test 1: All constants
# Input: (2 + 3)
const_tree = ExpressionTree()
const_tree.root = ExpressionNode('+')
const_tree.root.left = ExpressionNode('2')
const_tree.root.right = ExpressionNode('3')
const_tree.simplify()
print(const_tree.root.value == '5' and const_tree.root.left is None and const_tree.root.right is None)  # 🔢 Single node

# Test 2: Partial simplification
# Input: (2 + 3) * x
partial_tree = ExpressionTree()
partial_tree.root = ExpressionNode('*')
add = ExpressionNode('+')
add.left, add.right = ExpressionNode('2'), ExpressionNode('3')
partial_tree.root.left = add
partial_tree.root.right = ExpressionNode('x')
partial_tree.simplify()
print(partial_tree.root.value == '*' and partial_tree.root.left.value == '5' and partial_tree.root.right.value == 'x')  # ✨ Partial

# Test 3: No simplification possible
# Input: x + y
no_simp_tree = ExpressionTree()
no_simp_tree.root = ExpressionNode('+')
no_simp_tree.root.left = ExpressionNode('x')
no_simp_tree.root.right = ExpressionNode('y')
no_simp_tree.simplify()
print(no_simp_tree.root.value == '+' and no_simp_tree.root.left.value == 'x' and no_simp_tree.root.right.value == 'y')  # 🔤 No change

# Test 4: Complex nested simplification
# Input: ((2 * 3) + (8 / 4))
complex_tree = ExpressionTree()
complex_tree.root = ExpressionNode('+')
mult = ExpressionNode('*')
div = ExpressionNode('/')
mult.left, mult.right = ExpressionNode('2'), ExpressionNode('3')
div.left, div.right = ExpressionNode('8'), ExpressionNode('4')
complex_tree.root.left, complex_tree.root.right = mult, div
complex_tree.simplify()
print(complex_tree.root.value == '8' and complex_tree.root.left is None)  # 🎯 Fully simplified

# Test 5: Mixed variables and constants
# Input: x * (6 / 2)
mixed_tree = ExpressionTree()
mixed_tree.root = ExpressionNode('*')
div = ExpressionNode('/')
div.left, div.right = ExpressionNode('6'), ExpressionNode('2')
mixed_tree.root.left = ExpressionNode('x')
mixed_tree.root.right = div
mixed_tree.simplify()
print(mixed_tree.root.value == '*' and mixed_tree.root.left.value == 'x' and mixed_tree.root.right.value == '3')  # 🔄 Right simplified
