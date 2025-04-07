import itertools

greedy_iterations = 0
brute_force_combinations = 0

def greedy_warehouse_cover(stores, warehouses):
    global greedy_iterations
    uncovered_stores = set(stores)
    selected_warehouses = []
    while uncovered_stores:
        best_warehouse = None
        stores_covered_by_best = set()
        for warehouse, can_serve in warehouses.items():
            greedy_iterations += 1
            new_coverage = uncovered_stores & can_serve
            if len(new_coverage) > len(stores_covered_by_best):
                best_warehouse = warehouse
                stores_covered_by_best = new_coverage
        if not best_warehouse:
            break
        selected_warehouses.append(best_warehouse)
        uncovered_stores -= stores_covered_by_best
    return selected_warehouses


def brute_force_warehouse_cover(stores, warehouses):
    global brute_force_combinations
    warehouse_names = list(warehouses.keys())
    n = len(warehouse_names)
    best_solution = None
    for r in range(1, n + 1):
        for subset in itertools.combinations(warehouse_names, r):
            brute_force_combinations += 1
            covered = set()
            for w in subset:
                covered |= warehouses[w]
            if covered >= stores:
                if best_solution is None or len(subset) < len(best_solution):
                    best_solution = subset

    return list(best_solution) if best_solution else []


stores = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}

warehouses = {
    'Warehouse 1': {'A', 'B'},
    'Warehouse 2': {'B', 'C', 'D'},
    'Warehouse 3': {'D', 'E'},
    'Warehouse 4': {'C', 'E'},
    'Warehouse 5': {'F'},
    'Warehouse 6': {'G'},
    'Warehouse 7': {'H'},
    'Warehouse 8': {'A', 'F', 'G'},
    'Warehouse 9': {'B', 'C', 'H'},
    'Warehouse 10': {'D', 'E', 'F', 'G'}
}

greedy_result = greedy_warehouse_cover(stores, warehouses)
brute_result = brute_force_warehouse_cover(stores, warehouses)

print("Greedy solution:", greedy_result)
print("Greedy iterations:", greedy_iterations)
print("Brute-force solution:", brute_result)
print("Brute-force combinations tried:", brute_force_combinations)
