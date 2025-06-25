test_results = []
def record_test(test_name, condition):
    emoji = "" if condition else ""
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

    def find_path(self, start_vertex, end_vertex):
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            return []

        if start_vertex == end_vertex:
            return [start_vertex]

        visited = set()
        queue = [(start_vertex, [start_vertex])]

        while queue:
            current, path = queue.pop(0)
            if current not in visited:
                visited.add(current)
                for neighbor in self.adjacency_list[current]:
                    if neighbor == end_vertex:
                        return path + [neighbor]
                    else:
                        queue.append((neighbor, path + [neighbor]))

        return []

    def is_connected(self, vertex1, vertex2):
        return len(self.find_path(vertex1, vertex2)) > 0


def test_1_4():
    graph = Graph()

    # Build test graph: Lima - Cusco - Arequipa
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_vertex("Trujillo")  # Isolated vertex

    # 1.4.1 Direct connection path
    path = graph.find_path("Lima", "Cusco")
    record_test("1.4.1 Direct connection path", path == ["Lima", "Cusco"])

    # 1.4.2 Indirect connection path
    path = graph.find_path("Lima", "Arequipa")
    is_valid_path = len(path) == 3 and path[0] == "Lima" and path[-1] == "Arequipa"
    record_test("1.4.2 Indirect connection path", is_valid_path)

    # 1.4.3 No path case
    path = graph.find_path("Lima", "Trujillo")
    record_test("1.4.3 No path case", path == [])

    # 1.4.4 Self path
    path = graph.find_path("Lima", "Lima")
    record_test("1.4.4 Self path", path == ["Lima"])

    # 1.4.5 Connectivity check
    connected = graph.is_connected("Lima", "Arequipa")
    not_connected = graph.is_connected("Lima", "Trujillo")
    record_test("1.4.5 Connectivity check", connected and not not_connected)

#  Run tests
test_1_4()

#  Summary
for r in test_results:
    print(r)
