# Fixed objective function
def objective_function(x):
    return -(x**2) + 10

# Generate all neighbors
def get_neighbors(x, steps):
    return [x + step for step in steps]

# Hill Climbing Algorithm
def hill_climbing(start, steps):
    current = start
    current_value = objective_function(current)
    path = [current]

    while True:
        neighbors = get_neighbors(current, steps)
        best_neighbor = None
        best_value = current_value

        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            if neighbor_value > best_value:
                best_neighbor = neighbor
                best_value = neighbor_value

        if best_neighbor is None:
            break

        current = best_neighbor
        current_value = best_value
        path.append(current)

    return current, current_value, path


# -------- MAIN --------
test_cases = [
    {"start": 5, "steps": [-1, 1]},
    {"start": -4, "steps": [-1, 1]},
    {"start": 8, "steps": [-2, -1, 1, 2]},
    {"start": 0, "steps": [-1, 1]},
]

for index, test_case in enumerate(test_cases, start=1):
    start = test_case["start"]
    steps = test_case["steps"]
    solution, value, path = hill_climbing(start, steps)

    print(f"Test Case {index}")
    print("Start:", start)
    print("Steps:", steps)
    print("Path:", path)
    print("Best Solution:", solution)
    print("Best Value:", value)
    print()
