import itertools
import random
import time
import numpy as np

def generate_distance_matrix(n, seed=42):
    random.seed(seed)
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1, n):
            distance = random.randint(10, 100)
            matrix[i][j] = matrix[j][i] = distance
    return matrix

def tsp_brute_force(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')
    for perm in itertools.permutations(cities[1:]):
        path = [0] + list(perm) + [0]
        cost = sum(dist_matrix[path[i]][path[i + 1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            min_path = path
    return min_path, min_cost

def tsp_held_karp(dist_matrix):
    n = len(dist_matrix)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (dist_matrix[0][k], [0, k])
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = sum(1 << x for x in subset)
            for k in subset:
                prev_bits = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k:
                        continue
                    res.append((C[(prev_bits, m)][0] + dist_matrix[m][k], C[(prev_bits, m)][1] + [k]))
                C[(bits, k)] = min(res)
    bits = (2 ** n - 1) - 1
    res = []
    for k in range(1, n):
        cost = C[(bits, k)][0] + dist_matrix[k][0]
        path = C[(bits, k)][1] + [0]
        res.append((cost, path))
    return min(res)

def tsp_nearest_neighbor(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    path = [0]
    visited[0] = True
    total_cost = 0
    current = 0
    for _ in range(n - 1):
        next_city = min((dist_matrix[current][j], j) for j in range(n) if not visited[j])[1]
        total_cost += dist_matrix[current][next_city]
        visited[next_city] = True
        path.append(next_city)
        current = next_city
    total_cost += dist_matrix[current][0]
    path.append(0)
    return path, total_cost

def tsp_genetic(dist_matrix, population_size=100, generations=200, mutation_rate=0.01):
    n = len(dist_matrix)

    def create_individual():
        individual = list(range(1, n))
        random.shuffle(individual)
        return [0] + individual + [0]

    def fitness(ind):
        return sum(dist_matrix[ind[i]][ind[i + 1]] for i in range(n))

    def mutate(ind):
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, n), 2)
            ind[i], ind[j] = ind[j], ind[i]
        return ind

    def crossover(p1, p2):
        start, end = sorted(random.sample(range(1, n), 2))
        child_middle = p1[start:end]
        child = [0] + child_middle + [x for x in p2 if x not in child_middle and x != 0] + [0]
        return child
    population = [create_individual() for _ in range(population_size)]
    for _ in range(generations):
        population = sorted(population, key=fitness)
        new_population = population[:10]
        while len(new_population) < population_size:
            p1, p2 = random.choices(population[:50], k=2)
            child = mutate(crossover(p1, p2))
            new_population.append(child)
        population = new_population

    best = min(population, key=fitness)
    return best, fitness(best)

def compare_algorithms(n):
    dist_matrix = generate_distance_matrix(n)
    results = {}

    start = time.time()
    path, cost = tsp_brute_force(dist_matrix)
    results['Brute Force'] = (cost, round((time.time() - start), 3))

    start = time.time()
    cost, path = tsp_held_karp(dist_matrix)
    results['Held-Karp'] = (cost, round((time.time() - start), 3))

    start = time.time()
    path, cost = tsp_nearest_neighbor(dist_matrix)
    results['Nearest Neighbor'] = (cost, round((time.time() - start), 3))

    start = time.time()
    path, cost = tsp_genetic(dist_matrix)
    results['Genetic Algorithm'] = (cost, round((time.time() - start), 3))

    return results

city_sizes = [4, 5, 6, 8, 10]
all_results = {n: compare_algorithms(n) for n in city_sizes}
for cities, content in all_results.items():
    print(cities, content)
