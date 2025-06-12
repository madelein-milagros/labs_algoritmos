class MinHeap:
    def _init_(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)  
        self._heapify_up(len(self.heap) - 1)  

    def _heapify_up(self, index):
        # Mientras no estemos en la raíz y el valor actual sea menor que el del padre
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
        
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index  # Subimos al nuevo índice del padre
            else:
                break  # Si ya está en orden, salimos del bucle

# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5); print("🍀 Test 1:", h.heap == [5])
    h.insert(3); print("🍀 Test 2:", h.heap == [3,5])
    h.insert(4); print("🍀 Test 3:", h.heap == [3,5,4])
    h.insert(1); print("🍀 Test 4:", h.heap == [1,3,4,5])
    # 🍀 Test 5: parent ≤ children
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True)
        and (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)

test_min_heap_insert()
