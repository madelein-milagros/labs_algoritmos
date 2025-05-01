class TreeNodo:
    def __init__(self, val=0, left=0, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    if not root:
        return -1
    return 1 + max(tree_height(root.left), tree_height(root.right))


def test_tree_height():
    root = TreeNodo(1)
    root.left = TreeNodo(2)
    root.right = TreeNodo(3)
    root.left.left = TreeNodo(4)
    root.right.right =TreeNodo(5)
    assert tree_height(root)==2


    empty_tree = None           #arbol vacio
    assert tree_height(empty_tree) ==-1

    single_node = TreeNodo(1)
    assert tree_height(single_node)==0

    left_skewed = TreeNodo(1)
    left_skewed.left = TreeNodo (2)
    left_skewed.left.left =TreeNodo(3)
    left_skewed.left.left.left = TreeNodo(4)
    assert tree_height(left_skewed)==3

    perfect = TreeNodo(1)
    perfect.left = TreeNodo(2)
    perfect.right = TreeNodo(3)
    perfect.left.left = TreeNodo(4)
    perfect.left.right = TreeNodo(5)
    perfect.right.left =TreeNodo(6)
    perfect.right.right = TreeNodo(7)
    assert tree_height(perfect) ==2

    print("all height tests passed ")
test_tree_height()
