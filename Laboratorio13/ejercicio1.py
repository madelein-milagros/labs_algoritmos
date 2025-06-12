class MinHeap:
    # 📦 MinHeap data structure using list
    def __init__(self):
        # Initialize empty list for heap
        self.heap = []

    def is_empty(self):
        # Return True if heap is empty
        return len(self.heap) == 0

# 🧪 Test cases
def test_min_heap_init_and_empty():
    h = MinHeap()
    print(" Test 1:", h.is_empty() == True)
    h.heap.append(1)
    print(" Test 2:", h.is_empty() == False)
    h.heap.clear()
    print(" Test 3:", h.is_empty() == True)
    h.heap.extend([2, 3, 4])
    print(" Test 4:", h.is_empty() == False)
    h.heap.pop(); h.heap.pop(); h.heap.pop()
    print(" Test 5:", h.is_empty() == True)

test_min_heap_init_and_empty()
