class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def from_infix(self, tokens):
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
                if token.isdigit():
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
        tree = ExpressionTree()
        tree.root = build_tree(postfix)
        return tree
#test
tree2 = ExpressionTree().from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+')
print(tree2.root.left.value == '2')
print(tree2.root.right.value == '*')
print(tree2.root.right.left.value == '3')
print(tree2.root.right.right.value == '4')
