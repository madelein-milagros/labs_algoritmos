class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
        def get_next(self):
            return self.next
        
        def set_next(self, next_node):
            self.next = next_node

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        
        new_node = self.Node(data)
        new_node.set_next(self.head) 
        self.head = new_node  
        self.length += 1
        return True

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if self.head is None:  
            self.head = new_node
        else:
            current = self.head
            while current.get_next(): 
                current = current.get_next()
            current.set_next(new_node)  
        self.length += 1
        return True

    def insert_at_position(self, position, data):
       
        if position < 0 or position > self.length:
            return False
        
        
        if position == 0:
            return self.insert_at_beginning(data)
        
        
        if position == self.length:
            return self.insert_at_end(data)
        
       
        new_node = self.Node(data)
        current = self.head
        count = 0
        
        # Traverse to the node just before the insertion point
        while count < position - 1:
            current = current.get_next()
            count += 1
        
        # Insert the new node after 'current' and adjust pointers
        new_node.set_next(current.get_next())  # The new node's next points to current's next
        current.set_next(new_node)  # The current node's next now points to the new node
        
        self.length += 1
        return True

    def print_list(self):
        """Helper function to print the list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.get_next()
        print("None")

# Ejemplo de uso:
linked_list = LinkedList()
linked_list.insert_at_beginning(10)  # Lista: 10
linked_list.insert_at_end(20)        # Lista: 10 -> 20
linked_list.insert_at_position(1, 15) # Lista: 10 -> 15 -> 20
linked_list.print_list()              # Imprime: 10 -> 15 -> 20 -> None