test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        # Initialize empty adjacency list
        self.adjacency_list = {}

    def get_vertices(self):
        # Return list of all vertices
        return list(self.adjacency_list.keys())

    def get_vertex_count(self):
        # Return number of vertices in graph
        return len(self.adjacency_list)

    def has_vertex(self, vertex):
        # Check if vertex exists in graph
        return vertex in self.adjacency_list

def test_1_1():
    # 1.1.1 Empty graph initialization
    graph = Graph()
    record_test("1.1.1 Empty graph initialization", graph.get_vertex_count() == 0)
    
    # 1.1.2 Vertex counting
    graph.adjacency_list = {"Lima": [], "Cusco": []}  # Simulate adding vertices
    record_test("1.1.2 Vertex counting", graph.get_vertex_count() == 2)
    
    # 1.1.3 Vertex existence check
    record_test("1.1.3 Vertex existence check", graph.has_vertex("Lima") == True)
    
    # 1.1.4 Empty graph edge case
    empty_graph = Graph()
    record_test("1.1.4 Empty graph edge case", empty_graph.has_vertex("Lima") == False)
    
    # 1.1.5 Type validation
    record_test("1.1.5 Type validation", isinstance(graph.get_vertices(), list))

# 🚀 Run tests
test_1_1()

# 📋 Summary
for r in test_results:
    print(r)
