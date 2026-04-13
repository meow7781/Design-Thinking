# Function to take user-defined objective function
def get_objective_function():
    expr = input("Enter objective function in terms of x (e.g., -(x**2)+10): ")
    allowed_names = {"abs": abs, "max": max, "min": min, "pow": pow, "round": round}

    def objective_function(x):
        return eval(expr, {"__builtins__": {}}, {**allowed_names, "x": x})

    return objective_function

# Function to generate all neighbors using steps
def get_neighbors(x, steps):
    return [x + step for step in steps]

# Hill Climbing Algorithm
def hill_climbing(start, objective_function, steps):
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
objective_function = get_objective_function()
start = int(input("Enter initial state: "))
steps = list(map(int, input("Enter step values (e.g., -1 1): ").split()))

if not steps:
    raise ValueError("Please provide at least one step value.")

solution, value, path = hill_climbing(start, objective_function, steps)

print("\n--- Result ---")
print("Path:", path)
print("Best Solution:", solution)
print("Best Value:", value)
