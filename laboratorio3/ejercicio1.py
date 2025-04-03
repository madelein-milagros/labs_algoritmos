def display(self):
    if self.head is None:
        return "Empty List"
    current = self.head
    result = ""
    
    while current is not None:
        result += str(current.get_data())+ "->"
        current = current.get_next()
        
    return result + "None"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        
    def display(self):
        if self.head is None:
            return "Empty list"

        current = self.head
        result = ""

        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()

        return result + "None"

lista = LinkedList()
print(lista.display())  

lista.insert(10)
lista.insert(20)
lista.insert(30)
print(lista.display())  

