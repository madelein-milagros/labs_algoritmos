lass Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        result = ""
        while current:
            result += f"[{current.data}] -> "
            current = current.next
        result += "None"
        return result
# Testing
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(16)
    linked_list.insert_at_beginning(17)
    linked_list.insert_at_beginning(20)
    
    print(linked_list.display())
    
