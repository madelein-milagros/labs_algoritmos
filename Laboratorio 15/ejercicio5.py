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
        return len(self.adjacency_list.get(vertex, []))

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):
        def dfs(current, path):
            if max_length is not None and len(path) > max_length:
                return
            if current == end_vertex:
                paths.append(list(path))
                return
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()

        paths = []
        if start_vertex in self.adjacency_list and end_vertex in self.adjacency_list:
            dfs(start_vertex, [start_vertex])
        return paths

    def get_connected_components(self):
        visited = set()
        components = []

        def dfs(vertex, component):
            visited.add(vertex)
            component.append(vertex)
            for neighbor in self.adjacency_list.get(vertex, []):
                if neighbor not in visited:
                    dfs(neighbor, component)

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)
        return components


def test_1_5():
    graph = Graph()
    
    # Crear grafo con dos componentes
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # Componente separado
    
    # 1.5.1 Degree calculation
    print(graph.get_degree("Lima") == 2)

    # 1.5.2 Multiple paths finding
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    print(len(paths) >= 2)

    # 1.5.3 Connected components
    components = graph.get_connected_components()
    print(len(components) == 2)

    # 1.5.4 Empty graph analysis
    empty_graph = Graph()
    print(empty_graph.get_connected_components() == [])

    # 1.5.5 Non-existent vertex handling
    print(graph.get_degree("NonExistent") == 0)

# Ejecutamos test
test_1_5()

