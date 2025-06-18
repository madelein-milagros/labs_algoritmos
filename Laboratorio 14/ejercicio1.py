test_results = []

def record_test(test_name, condition):
    if condition:
        test_results.append(f"[OK] {test_name}")
    else:
        test_results.append(f"[FAIL] {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        return self.heap[0] if not self.is_empty() else None

def test_1_1():
    # 1.1.1 Empty heap initialization
    heap = MinHeap()
    record_test("1.1.1 Empty heap initialization", heap.is_empty() == True)

    # 1.1.2 Size tracking
    heap.heap = [1, 3, 2]  # Simula elementos en el heap
    record_test("1.1.2 Size tracking", heap.size() == 3)

    # 1.1.3 Peek functionality
    record_test("1.1.3 Peek functionality", heap.peek() == 1)

    # 1.1.4 Empty heap edge case
    empty_heap = MinHeap()
    record_test("1.1.4 Empty heap edge case", empty_heap.peek() is None)

    # 1.1.5 Type validation
    record_test("1.1.5 Type validation", isinstance(heap.is_empty(), bool))

# Ejecutar pruebas
test_1_1()

# Imprimir resultados
for r in test_results:
    print(r)
