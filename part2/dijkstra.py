class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []
        self.adjacency_list[vertex1].append((vertex2, weight))

    def dijkstra(self, origin, destination):
        unvisited = list(self.adjacency_list.keys())
        weights = {vertex: float("inf") for vertex in self.adjacency_list}
        weights[origin] = 0
        predecessors = {}
        while unvisited:
            current = min(unvisited, key=lambda vertex: weights[vertex])
            if weights[current] == float("inf"):
                break
            for neighbor in self.adjacency_list[current]:
                vertex, weight = neighbor[0], neighbor[1]
                new_weight = weights[current] + weight
                if new_weight < weights[vertex]:
                    weights[vertex] = new_weight
                    predecessors[vertex] = current
            unvisited.remove(current)
        path = []
        current = destination
        while current in predecessors.keys():
            path.insert(0, (current, weights[current]))
            current = predecessors[current]
        path.insert(0, (origin, 0))
        return path
    
    def show(self):
        for vertex in self.adjacency_list:
            print(vertex, self.adjacency_list[vertex])

    def min_path(self, origin, destination):
        path = self.dijkstra(origin, destination)
        if len(path) <= 1:
            print("Path not found")
        else:
            print(f"\nShortest Path Found Between {origin} and {destination}")
            for i in range(len(path)):
                if i != len(path)-1:
                    print(path[i], end="=>")
                else:
                    print(path[i], f"\nKm: {path[i][1]}")

if __name__ == "__main__":
    print("Graph")
    g1 = Graph()
    e1 = [
        ("CD", "A", 4), ("CD", "B", 2), ("A", "C", 5), ("A", "D", 10),
        ("B", "A", 3), ("B", "D", 8), ("C", "D", 2), ("C", "E", 4),
        ("D", "E", 6), ("D", "F", 5), ("E", "F", 3)
    ]

    [g1.add_edge(ori, des, wei) for ori, des, wei in e1]
    g1.show()
    g1.min_path("CD", "F")