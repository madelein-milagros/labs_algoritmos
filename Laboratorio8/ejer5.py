class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        if not values:
            return
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        self.root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()

def prune_tree(node, target):
    if not node:
        return None
    node.left = prune_tree(node.left, target)
    node.right = prune_tree(node.right, target)
    if node.val != target and not node.left and not node.right:
        return None
    return node

def print_tree(node):
    if not node:
        return []
    return [node.val] + print_tree(node.left) + print_tree(node.right)

# 🔍 CASO 4: El valor 4 no está en el árbol
tree = BinaryTree()
tree.build_tree_from_list([1, 2, 3])
tree.root = prune_tree(tree.root, 4)
print(print_tree(tree.root))  # 👉 Salida: []
