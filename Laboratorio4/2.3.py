
class Node:
    """Node class for the Linked List Stack."""
    
    def __init__(self, data=None):
        """Initialize node with data and next reference."""
        self.data = data
        self.next = None


class LinkedListStack:
    """Stack implementation using a linked list."""
    
    def __init__(self):
        """Initialize empty stack using linked list."""
        self.head = None  # Top of the stack
        self.count = 0  # Number of elements
    
    def is_empty(self):
        """Check if stack is empty."""
        return self.head is None
    
    def push(self, item):
        """Add item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        
        item = self.head.data
        self.head = self.head.next
        self.count -= 1
        return item
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        
        return self.head.data
    
    def size(self):
        """Return the number of items in the stack."""
        return self.count
    
    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: []"
        
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
            
        return f"Stack: [{', '.join(items)}]"
def test_linked_list_stack():
    print("Test: Linked list stack implementation")
    stack = LinkedListStack()
    print(f"Empty stack: {stack}")
    for i in range(1, 6):
        stack.push(i * 10)
        print(f"After push({i*10}): {stack}")
    
    print(f"Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    
    while not stack.is_empty():
        print(f"Pop: {stack.pop()}, Remaining: {stack}")
    try:
        empty_peek = stack.peek()
        print("Peek should have raised an exception!")
    except IndexError as e:
        print(f"Error as expected: {e}")
    print("All linked list stack tests passed!")
if __name__ == "__main__":
    test_linked_list_stack()

