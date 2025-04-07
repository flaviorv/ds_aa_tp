import random

num_cities = 10
num_edges = 20

edges = set()
graph = {f"City {i}": {} for i in range(num_cities)}

while len(edges) < num_edges:
    u = random.randint(0, num_cities - 1)
    v = random.randint(0, num_cities - 1)
    if u == v:
        continue
    edge = tuple(sorted((u, v)))
    if edge in edges:
        continue
    edges.add(edge)
    cost = random.randint(1, 50)
    city_u = f"City {u}"
    city_v = f"City {v}"
    graph[city_u][city_v] = cost
    graph[city_v][city_u] = cost

def prim(graph):
    cities = list(graph.keys())
    selected = set()
    mst = []
    total_cost = 0
    iterations = 0
    selected.add(cities[0])
    while len(selected) < len(cities):
        min_cost = float('inf')
        min_edge = (None, None)
        for u in selected:
            for v, cost in graph[u].items():
                iterations += 1
                if v not in selected and cost < min_cost:
                    min_cost = cost
                    min_edge = (u, v)
        if min_edge[0] is not None:
            u, v = min_edge
            selected.add(v)
            mst.append((u, v, min_cost))
            total_cost += min_cost
        else:
            break
    return mst, total_cost, iterations


mst_edges, total_cost, iterations = prim(graph)

print("Minimum Spanning Tree (Prim O(V^2)):")

print(f"Cities: {num_cities} Connections: {num_edges}")
print(f"\nTotal MST Cost: ${total_cost}M")
print(f"Iterations (edge checks): {iterations}")
