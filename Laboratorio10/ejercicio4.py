class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def preorder_traversal(root):
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

# Test 1: Simple tree
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(
    inorder_traversal(node1) == ['2', '+', '3'] and
    preorder_traversal(node1) == ['+', '2', '3'] and
    postorder_traversal(node1) == ['2', '3', '+']
)

# Test 2: Nested left tree
node2 = Node('+')
node2.left = Node('*')
node2.right = Node('5')
node2.left.left = Node('2')
node2.left.right = Node('3')
print(
    inorder_traversal(node2) == ['2', '*', '3', '+', '5'] and
    preorder_traversal(node2) == ['+', '*', '2', '3', '5'] and
    postorder_traversal(node2) == ['2', '3', '*', '5', '+']
)

# Test 3: Single node
node3 = Node('X')
print(
    inorder_traversal(node3) == ['X'] and
    preorder_traversal(node3) == ['X'] and
    postorder_traversal(node3) == ['X']
)

# Test 4: Empty tree
print(
    inorder_traversal(None) == [] and
    preorder_traversal(None) == [] and
    postorder_traversal(None) == []
)

# Test 5: Complex tree
node5 = Node('/')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('a')
node5.left.right = Node('b')
node5.right.left = Node('c')
node5.right.right = Node('d')
print(
    inorder_traversal(node5) == ['a', '+', 'b', '/', 'c', '-', 'd'] and
    preorder_traversal(node5) == ['/', '+', 'a', 'b', '-', 'c', 'd'] and
    postorder_traversal(node5) == ['a', 'b', '+', 'c', 'd', '-', '/']
)
