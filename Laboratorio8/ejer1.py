class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def balance_bst(root):
    def inorder(node):
        return inorder(node.left) + [node] + inorder(node.right) if node else []
    
    def build_balanced(nodes):
        if not nodes: return None
        mid = len(nodes) // 2
        root = nodes[mid]
        root.left, root.right = build_balanced(nodes[:mid]), build_balanced(nodes[mid+1:])
        return root

    return build_balanced(inorder(root))

# **Ejemplo de uso**
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)

# Árbol desbalanceado
root = TreeNode(10)
root.right = TreeNode(20)
root.right.right = TreeNode(30)
root.right.right.right = TreeNode(40)

print("Árbol balanceado en orden:")
print_inorder(balance_bst(root))
