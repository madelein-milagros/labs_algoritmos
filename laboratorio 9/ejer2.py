class Node:
    """Node in an expression tree"""
    def __init__(self, value):
        self.value = value  # Operator or operand
        self.left = None    # Left child
        self.right = None   # Right child

class ExpressionTree:
    """Expression tree implementation"""

    def __init__(self):
        self.root = None  # Tree root

    @classmethod
    def from_infix(cls, tokens):
        # Define operator precedence
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        # Convert infix expression to postfix (RPN)
        def infix_to_postfix(tokens):
            output = []  # Postfix result
            stack = []   # Operator stack
            for token in tokens:
                if token.isdigit():  # If it's a number
                    output.append(token)
                elif token in "+-*/":  # If it's an operator
                    while stack and precedence(stack[-1]) >= precedence(token):
                        output.append(stack.pop())  # Pop higher/equal precedence
                    stack.append(token)
                elif token == '(':  # Left parenthesis
                    stack.append(token)
                elif token == ')':  # Right parenthesis
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()  # Remove '('
            while stack:
                output.append(stack.pop())  # Pop remaining ops
            return output

        # Build expression tree from postfix
        def build_tree(postfix):
            stack = []  # Stack for nodes
            for token in postfix:
                node = Node(token)  # Create a node
                if token in '+-*/':  # If operator, pop two nodes
                    node.right = stack.pop()
                    node.left = stack.pop()
                stack.append(node)  # Push new subtree
            return stack[-1]  # Root node

        postfix = infix_to_postfix(tokens)  # Convert to postfix
        tree = cls()                        # Create tree
        tree.root = build_tree(postfix)    # Build from postfix
        return tree                         # Return tree

    
# ✅ Test cases

tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')  # 🌱 Simple tree

tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')  # 📊 Precedence structure

tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')  # 🔗 
