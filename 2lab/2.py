import numpy as np
import random
import time

def read_coordinates_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    coordinates = np.array([list(map(float, line.strip().split())) for line in lines])
    return coordinates

def distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def total_distance(solution, coordinates):
    total = 0
    for i in range(len(solution) - 1):
        total += distance(coordinates[solution[i]], coordinates[solution[i + 1]])
    # Add distance from the last point back to the starting point
    total += distance(coordinates[solution[-1]], coordinates[solution[0]])
    return total

def generate_neighboring_solution(solution):
    new_solution = solution.copy()
    # Reverse a random segment of the route
    idx1, idx2 = sorted(np.random.choice(len(new_solution), size=2, replace=False))
    new_solution[idx1:idx2] = new_solution[idx1:idx2][::-1]
    return new_solution

def simulated_annealing(initial_solution, cost_function, temperature, cooling_rate, iterations):
    current_solution = initial_solution
    current_cost = cost_function(current_solution)

    best_solution = current_solution
    best_cost = current_cost

    for i in range(iterations):
        new_solution = generate_neighboring_solution(current_solution)
        new_cost = cost_function(new_solution)

        if new_cost < current_cost:
            current_solution = new_solution
            current_cost = new_cost

            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost
        else:
            # Check if temperature is too small before calculating probability
            if temperature > 1e-10:
                probability = np.exp((current_cost - new_cost) / temperature)
                if random.random() < probability:
                    current_solution = new_solution
                    current_cost = new_cost

        temperature *= 1 - cooling_rate

    return best_solution, best_cost

def write_solution_to_file(file_path, solution, cost, ans, execution_time):
    with open(file_path, 'a') as file:
        file.write(f"Best Solution Order: {solution}\n")
        file.write(f"Best Cost: {cost}\n")
        file.write(f"Optimality Probability: {ans:.2f}%\n")
        file.write(f"Execution Time: {execution_time:.2f} seconds\n")

# Set the path to your coordinates file
file_path = 'qatar.txt'
output_file_path = 'output_solutions.txt'
coordinates = read_coordinates_from_file(file_path)
initial_solution = np.arange(len(coordinates))
cost_function = lambda x: total_distance(x, coordinates)
initial_temperature = 100
cooling_rate = 0.0001
iterations = 5000000

start_time = time.time()
best_solution, best_cost = simulated_annealing(initial_solution, cost_function, initial_temperature, cooling_rate, iterations)
end_time = time.time()
execution_time = end_time - start_time

optimal_cost = 9352
ans = (1 - best_cost / optimal_cost) * 100

write_solution_to_file(output_file_path, best_solution, best_cost, ans, execution_time)
print(f"Results written to {output_file_path}")
print(f"Optimality Probability: {ans:.2f}%")
print(f"Execution Time: {execution_time:.2f} seconds")
