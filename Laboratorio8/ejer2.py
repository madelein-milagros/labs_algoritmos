from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        if not values:
            return None
        self.root = Node(values[0])
        queue = deque([self.root])
        i = 1
        while queue and i < len(values):
            current = queue.popleft()
            if i < len(values) and values[i] is not None:
                current.left = Node(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = Node(values[i])
                queue.append(current.right)
            i += 1
        return self.root

def serialize(root):
    if not root:
        return "#"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("#")
    return ",".join(result)

def deserialize(data):
    if data == "#":
        return None
    nodes = data.split(",")
    root = Node(int(nodes[0]))
    queue = deque([root])
    i = 1
    while queue:
        current = queue.popleft()
        if nodes[i] != "#":
            current.left = Node(int(nodes[i]))
            queue.append(current.left)
        i += 1
        if nodes[i] != "#":
            current.right = Node(int(nodes[i]))
            queue.append(current.right)
        i += 1
    return root

bt = BinaryTree()
bt.build_tree_from_list([1, 2, 3, None, 4])
s = serialize(bt.root)
print("Serialized:", s)
r = deserialize(s)
print("Re-Serialized:", serialize(r))
print("✅ Coinciden" if s == serialize(r) else "❌ No coinciden")
