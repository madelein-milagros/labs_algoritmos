class QueueWithTwoStacks:
    def __init__(self):
        self.stack_enqueue = []  
        self.stack_dequeue = []  

    def enqueue(self, value):
        self.stack_enqueue.append(value)

    def _transfer(self):
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())

    def dequeue(self):
        if not self.stack_dequeue:
            self._transfer()
        if not self.stack_dequeue:
            raise IndexError("Dequeue from empty queue")
        return self.stack_dequeue.pop()

    def peek(self):
        if not self.stack_dequeue:
            self._transfer()
        if not self.stack_dequeue:
            raise IndexError("Peek from empty queue")
        return self.stack_dequeue[-1]

    def isEmpty(self):
        return not self.stack_enqueue and not self.stack_dequeue

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

q = QueueWithTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  
print(q.peek())     
print(q.size())     
print(q.isEmpty())  
q.dequeue()
q.dequeue()
print(q.isEmpty())  

