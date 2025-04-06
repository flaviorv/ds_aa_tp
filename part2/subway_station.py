class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_station(self, station):
        if station not in self.adjacency_list:
            self.adjacency_list[station] = []

    def add_edge(self, station1, station2):
        if station1 not in self.adjacency_list:
            self.add_station(station1)
        if station2 not in self.adjacency_list:
            self.add_station(station2)
        self.adjacency_list[station1].append(station2)

    def _dfs(self, start, end, visited, path, _start=None):
        if visited is None:
            _start = start
            visited = set()
        print(start, end=" ")
        if end == start:
            path = True
            return path
        visited.add(start)
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                return self._dfs(neighbor, end, visited, path, _start)
  
    def dfs(self, start, end=None, visited=None):
        print("DFS:", end=" ")
        path = self._dfs(start, end, visited, path=False)

    def bfs(self, start, end=None):
        print("BFS:", end=" ")
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                if vertex == end:
                    return
                visited.add(vertex)
                queue.extend(self.adjacency_list[vertex])
        if end != None:
            print(f"- No path between {start} and {end}")
            return

if __name__ == "__main__":
    lines = [("A", "B"), ("A", "C"), ("B", "A"), ("B", "D"), ("B", "E"), ("C", "A"), ("C", "F"),
              ("D", "B"), ("D", "E"), ("E", "B"), ("E", "D"), ("E", "F"), ("F", "C"), ("F", "E"),]
    
    graph = Graph()
    for edge in lines:
        graph.add_edge(edge[0], edge[1])

    for lines in graph.adjacency_list:
        print(lines, graph.adjacency_list[lines])
   
    print("Passing through all stations:")
    graph.dfs("A")
    print()
    graph.bfs("A")
    print()
  
    print("From A until F")
    graph.dfs("A", "F")
    print()
    graph.bfs("A", "F")
    print()
