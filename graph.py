class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Добавить вершину"""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавить ребро между вершинами"""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # Если граф неориентированный

    def print_graph(self):
        """Вывести граф"""
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")


#  Создаём граф
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")

graph.print_graph()
