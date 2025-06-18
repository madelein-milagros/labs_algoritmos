test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []
    def _parent_index(self, index):
        # Calculate parent index using heap property
        return (index-1)//2 if index >0 else None  
    def _left_child_index(self, index):
        # Calculate left child index
        return  2* index +1 
    def _right_child_index(self, index):
        # Calculate right child index
        return 2 * index +2
    def _has_left_child(self, index):
        # Check if left child exists
         return self._left_child_index(index)< len(self.heap)   
    def _has_right_child(self, index):
        # Check if right child exists
         return self._right_child_index(index)< len(self.heap)

def test_1_2():
    heap = MinHeap()
    heap.heap = [1, 3, 2, 7, 4, 5, 8]  # Sample heap for testing
    
    # 1.2.1 Parent calculation
    record_test("1.2.1 Parent calculation", heap._parent_index(4) == 1)
    
    # 1.2.2 Children calculation
    left_correct = heap._left_child_index(1) == 3
    right_correct = heap._right_child_index(1) == 4
    record_test("1.2.2 Children calculation", left_correct and right_correct)
    
    # 1.2.3 Root node edge case
    record_test("1.2.3 Root node edge case", heap._parent_index(0) == -1 or heap._parent_index(0) is None)
    
    # 1.2.4 Boundary validation
    has_children = heap._has_left_child(1) and heap._has_right_child(1)
    record_test("1.2.4 Boundary validation", has_children)
    
    # 1.2.5 Invalid index handling
    no_children = not heap._has_left_child(6) and not heap._has_right_child(6)
    record_test("1.2.5 Invalid index handling", no_children)

# 🚀 Run tests
test_1_2()

# 📋 Summary
for r in test_results:
    print(r)
