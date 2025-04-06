class Graph:
    def __init__(self, length):
        self.adjacency_list = {}
        self.adjacency_matrix = [[0 for _ in range(length)] for _ in range(length)] 


    def add_route(self, origin, destination, distance):
        if origin not in self.adjacency_list:
            self.adjacency_list[origin] = {}
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = {}
        self.adjacency_list[origin][destination] = distance
        self.adjacency_matrix[matrix_indexes[origin]][matrix_indexes[destination]] = distance

    def show_ajacency_list(self):
         print("Adjacency list")
         for edge in self.adjacency_list:
            print(edge, self.adjacency_list[edge])

    def show_adjacency_matrix(self):
        print("Adjacency_matrix")
        for edge in self.adjacency_matrix:
            print(edge)

if __name__ == "__main__":
    matrix_indexes = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
    
    routes = [("A", "B", 4), ("A", "C", 2), ("B", "A", 4), ("B", "D", 5), ("C", "A", 2), 
              ("C", "D", 8), ("C", "E", 3), ("D", "B", 5), ("D", "C", 8), ("D", "F", 6), 
              ("E", "C", 3), ("E", "F", 1), ("F", "D", 6), ("F", "E", 1)]
    
    graph = Graph(len(matrix_indexes))
    for neighborhood1, neighborhood2, distance in routes:
        graph.add_route(neighborhood1, neighborhood2, distance)
    
    graph.show_ajacency_list()
    graph.show_adjacency_matrix()
    
