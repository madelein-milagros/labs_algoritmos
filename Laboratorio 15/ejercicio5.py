test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def get_degree(self, vertex):
        # Return how many neighbors the vertex has
        return len(self.adjacency_list.get(vertex, []))

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):
        # Use DFS to explore all paths
        def dfs(current, path):
            if current == end_vertex:
                paths.append(path)
                return
            if max_length is not None and len(path) >= max_length:
                return
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    dfs(neighbor, path + [neighbor])

        paths = []
        if start_vertex in self.adjacency_list and end_vertex in self.adjacency_list:
            dfs(start_vertex, [start_vertex])
        return paths

    def get_connected_components(self):
        # DFS to discover all separate graph sections
        visited = set()
        components = []

        def dfs(vertex, component):
            visited.add(vertex)
            component.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)
        return components

# ✅ TESTS
def test_1_5():
    graph = Graph()

    # Build graph with two components
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # Separate component

    # 1.5.1 Degree calculation
    lima_degree = graph.get_degree("Lima")
    record_test("1.5.1 Degree calculation", lima_degree == 2)

    # 1.5.2 Multiple paths finding
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    has_multiple_paths = len(paths) >= 2
    record_test("1.5.2 Multiple paths finding", has_multiple_paths)

    # 1.5.3 Connected components
    components = graph.get_connected_components()
    has_two_components = len(components) == 2
    record_test("1.5.3 Connected components", has_two_components)

    # 1.5.4 Empty graph analysis
    empty_graph = Graph()
    empty_components = empty_graph.get_connected_components()
    record_test("1.5.4 Empty graph analysis", empty_components == [])

    # 1.5.5 Non-existent vertex handling
    degree = graph.get_degree("NonExistent")
    record_test("1.5.5 Non-existent vertex handling", degree == 0 or degree is None)

# 🚀 Run and summarize test results
test_1_5()
for r in test_results:
    print(r)
