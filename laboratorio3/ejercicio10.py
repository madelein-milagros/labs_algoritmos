def get_nth_from_end(self, n):
    """Return the data of the nth node from the end (1-based indexing)."""
    if n <= 0 or n > self.length or self.head is None:
        return None
    
    # The nth node from the end is the (length-n+1)th node from the beginning
    position = self.length - n
    
    current = self.head
    count = 0
    
    while count < position:
        current = current.get_next()
        count += 1
    
    return current.get_data()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)
        self.length += 1
    
    def get_nth_from_end(self, n):
       
        if n <= 0 or n > self.length or self.head is None:
            return None
        
        position = self.length - n
        
        current = self.head
        count = 0
        
        while count < position:
            current = current.get_next()
            count += 1
        
        return current.get_data()

# Ejemplo de uso:
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)


print(linked_list.get_nth_from_end(5))  
##ejercicio10
