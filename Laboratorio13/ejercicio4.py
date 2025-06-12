class MinHeap:
    def build_heap(self, array):
        self.heap = array.copy()
        start = (len(self.heap) // 2) - 1
        for i in range(start, -1, -1):
            self._heapify_down(i)
    
    def _heapify_down(self, index):
        heap = self.heap
        n = len(heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right
            
            if smallest != index:
                heap[index], heap[smallest] = heap[smallest], heap[index]
                index = smallest
            else:
                break

def test_build_heap():
    h = MinHeap()
    h.build_heap([5,3,8,1,2]); print("🔨 Test 1:", h.heap[0]==1)
    h.build_heap([7,6,5,4,3,2,1]); print("🔨 Test 2:", h.heap[0]==1)
    h.build_heap([2,1]);           print("🔨 Test 3:", h.heap==[1,2])
    h.build_heap([10]);            print("🔨 Test 4:", h.heap==[10])
    h.build_heap([]);              print("🔨 Test 5:", h.heap==[])

test_build_heap()
