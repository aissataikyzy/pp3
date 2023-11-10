import numpy as np
import math
import random

def read_coordinates_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    coordinates = np.array([list(map(float, line.strip().split())) for line in lines])
    return coordinates

def distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def total_distance(solution):
    total = 0
    for i in range(len(solution) - 1):
        total += distance(solution[i], solution[i + 1])
    # Add distance from the last point back to the starting point
    total += distance(solution[-1], solution[0])
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
            probability = np.exp((current_cost - new_cost) / temperature)
            if random.random() < probability:
                current_solution = new_solution
                current_cost = new_cost

        temperature *= 1 - cooling_rate

    return best_solution, best_cost

# Example usage:
file_path = 'qatar.txt'  # Change this to the path of your file
coordinates = read_coordinates_from_file(file_path)
initial_solution = np.arange(len(coordinates))
cost_function = lambda x: total_distance(coordinates[x])
initial_temperature = 1000
cooling_rate = 0.001
iterations = 100000

best_solution, best_cost = simulated_annealing(initial_solution, cost_function, initial_temperature, cooling_rate, iterations)

print("Best Solution Order:", best_solution)
print("Best Cost:", best_cost)
print(f"Вероятность оптимального решения: {(best_cost-9352)/9352*100:.2f}%")