#ejercicio4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return True
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return True

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# Test
lista = LinkedList()
lista.insert_at_end(10)
lista.insert_at_end(20)
lista.insert_at_end(30)
lista.display()  
