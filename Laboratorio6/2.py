class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            raise Exception("Queue is full")
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def get_elements(self):
        result = []
        i = self.front
        for _ in range(self.count):
            result.append(self.queue[i])
            i = (i + 1) % self.size
        return result

def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return []

    k %= n  

    q = CircularQueue(n)

    for item in arr:
        q.enqueue(item)

    for _ in range(n - k):
        q.enqueue(q.dequeue())

    return q.get_elements()

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    steps = 3
    rotated = rotate_array(array, steps)
    print(rotated)  
