class Node:
    """Node in an expression tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    """Expression tree implementation"""
    def __init__(self):
        self.root = None

    @classmethod
    def from_infix(cls, tokens):
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def infix_to_postfix(tokens):
            output = []
            stack = []
            for token in tokens:
                if token.isalnum():  # Acepta números y letras
                    output.append(token)
                elif token in "+-*/":
                    while stack and precedence(stack[-1]) >= precedence(token):
                        output.append(stack.pop())
                    stack.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()
            while stack:
                output.append(stack.pop())
            return output

        def build_tree(postfix):
            stack = []
            for token in postfix:
                node = Node(token)
                if token in '+-*/':
                    node.right = stack.pop()
                    node.left = stack.pop()
                stack.append(node)
            return stack[-1]

        postfix = infix_to_postfix(tokens)
        tree = cls()
        tree.root = build_tree(postfix)
        return tree

# ✅ Test cases

tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')

tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')

tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')

tree4 = ExpressionTree.from_infix(['x', '+', 'y', '*', 'z'])
print(tree4.root.value == '+' and tree4.root.right.value == '*')

tree5 = ExpressionTree.from_infix(['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'])
print(tree5.root.value == '/' and tree5.root.left.value == '+' and tree5.root.right.value == '-')
