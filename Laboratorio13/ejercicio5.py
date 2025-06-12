class MaxHeap:
    # 🦁 MaxHeap data structure using list
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def delete_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()
    h.insert(1);         print(" Test 1:", h.heap==[1])
    for v in [3,2,8,5]:
        h.insert(v)
    print(" Test 2:", h.heap[0]==max(h.heap))
    h.delete_max();      print(" Test 3:", h.heap[0]==max(h.heap))
    h = MaxHeap()
    for v in [5,3,1]:
        h.insert(v)
    h.delete_max();      print(" Test 4:", h.heap==[3,1])
    h=MaxHeap(); h.insert(10)
    print("Test 5:", h.delete_max()==10 and h.heap==[])

test_max_heap()
