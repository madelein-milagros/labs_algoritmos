class QueueWithTwoStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    # Enqueue: Add to the end of the queue
    def enqueue(self, value):
        self.stack_enqueue.append(value)

    # Dequeue: Remove from the front of the queue
    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        self._shift_stacks_if_needed()
        return self.stack_dequeue.pop()

    # Peek: View the front without removing it
    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        self._shift_stacks_if_needed()
        return self.stack_dequeue[-1]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.stack_enqueue) == 0 and len(self.stack_dequeue) == 0

    # Get the total size
    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

    # Transfer elements if stack_dequeue is empty
    def _shift_stacks_if_needed(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

# Test the queue
if __name__ == "__main__":
    queue = QueueWithTwoStacks()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("First element (peek):", queue.peek())   # 10
    print("Removed:", queue.dequeue())            # 10
    print("Current size:", queue.size())          # 2
    print("Is empty:", queue.is_empty())          # False
    print("Removed:", queue.dequeue())            # 20
    print("Removed:", queue.dequeue())            # 30
    print("Is empty now:", queue.is_empty())      # True
