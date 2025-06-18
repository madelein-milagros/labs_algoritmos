test_results = []

def record_test(test_name, condition):
    status = "[OK]" if condition else "[FAIL]"
    test_results.append(f"{status} {test_name}")

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return max_value

    def build_heap(self, array):
        self.heap = array[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index, parent = parent, (parent - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        while 2 * index + 1 < size:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

def test_1_5():
    heap = MaxHeap()

    # 1.5.1 MaxHeap insertion
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)

    # 1.5.2 MaxHeap deletion
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)

    # 1.5.3 Build heap from array
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))

    # 1.5.4 Heap property verification
    is_valid = all(
        heap.heap[i] >= heap.heap[2 * i + 1] if 2 * i + 1 < len(heap.heap) else True
        and heap.heap[i] >= heap.heap[2 * i + 2] if 2 * i + 2 < len(heap.heap) else True
        for i in range(len(heap.heap) // 2)
    )
    record_test("1.5.4 Heap property verification", is_valid)

    # 1.5.5 Empty array handling
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

test_1_5()

for r in test_results:
    print(r)
