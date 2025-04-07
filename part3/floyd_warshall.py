class Graph:
    def __init__(self):
        self.vertices = {}
        self.adjacency_matrix = []

    def add_edge(self, origin, destination, average_time):
        if origin not in self.vertices:
            self.vertices[origin] = len(self.vertices)
            self.adjacency_matrix.append([])
        if destination not in self.vertices:
            self.vertices[destination] = len(self.vertices)
            self.adjacency_matrix.append([]) 
        for row in self.adjacency_matrix:
            diff = len(self.vertices) - len(row)
            if diff > 0:
                for _ in range(diff):
                    row.append(float("inf"))
        self.adjacency_matrix[self.vertices[origin]][self.vertices[destination]] = average_time

    def floyd_warshall(self):
        length = len(self.adjacency_matrix)
        for k in range(length):
            for i in range(length):
                for j in range(length):
                    if self.adjacency_matrix[i][k] + self.adjacency_matrix[k][j] < self.adjacency_matrix[i][j]:
                        self.adjacency_matrix[i][j] = self.adjacency_matrix[i][k] + self.adjacency_matrix[k][j]
        return self.adjacency_matrix
    
    def show(self):
        print("Neighborhoods:")
        for neighborhood in self.vertices:
            print(neighborhood, self.adjacency_matrix[self.vertices[neighborhood]])

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 10)
    g.add_edge('B', 'C', 3)
    g.add_edge('B', 'D', 8)
    g.add_edge('C', 'D', 2)
    g.add_edge('C', 'E', 7)
    g.add_edge('D', 'E', 4)
    g.add_edge('D', 'F', 6)
    g.add_edge('E', 'F', 5)
        
    g.show()
    paths = g.floyd_warshall()
    g.show()

    
    
    print("Lower time:")
    print(f"From A to F: {paths[g.vertices["A"]][g.vertices["F"]]}min")
        

