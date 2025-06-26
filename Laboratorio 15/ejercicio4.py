
from collections import deque

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
        queue = deque([[start_vertex]])

        while queue:
            path = queue.popleft()
            vertex = path[-1]
            if vertex == end_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return []

    def is_connected(self, vertex1, vertex2):
        return bool(self.find_path(vertex1, vertex2))
