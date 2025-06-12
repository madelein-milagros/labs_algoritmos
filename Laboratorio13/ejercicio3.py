class MinHeap:
    def __init__(self):
        self.heap = []

    def delete_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        heap = self.heap
        size = len(heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and heap[left] < heap[smallest]:
                smallest = left
            if right < size and heap[right] < heap[smallest]:
                smallest = right

            if smallest != index:
                heap[index], heap[smallest] = heap[smallest], heap[index]
                index = smallest
            else:
                break

#  Test cases
def test_min_heap_delete_min():
    h = MinHeap()
    print(" Test 1:", h.delete_min() is None)
    h.heap = [1]
    print(" Test 2:", h.delete_min() == 1 and h.heap == [])
    h.heap = [1, 3, 2]
    print(" Test 3:", h.delete_min() == 1 and h.heap == [2, 3])
    h.heap = [1, 3, 4, 5]
    print(" Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])
    h.heap = [1, 2, 3, 4, 5]
    print(" Test 5:", h.delete_min() == 1 and h.heap == [2, 4, 3, 5])

test_min_heap_delete_min()
