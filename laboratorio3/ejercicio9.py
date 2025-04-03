class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def delete_from_beginning(self):
        if self.head is None:
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data
    
    def search(self, data):
        """Find the position of data in the list, or return -1 if not found."""
        if self.head is None:
            return -1
        
        current = self.head
        position = 0
        
        while current is not None:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Ejemplo 
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.print_list()

print("Deleted:", ll.delete_from_beginning())
ll.print_list()

print("Position of 20:", ll.search(20))
print("Position of 40:", ll.search(40))
