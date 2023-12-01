import numpy as np

def f(x, y):
    return np.sin(x + y)**2 + 5 + np.cos(y)**2 - np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25)

def manual_gradient(x, y):
    df_dx = 2 * (np.sin(x + y) * np.cos(x + y) - (2 * x + 54) * np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25) / 25)
    df_dy = 2 * (np.sin(x + y) * np.cos(x + y) + (2 * y + 146) * np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25) / 25)
    return np.array([df_dx, df_dy])

def backtracking_line_search(x, y, direction, alpha=0.5, beta=0.8):
    t = 1.0
    while f(x + t * direction[0], y + t * direction[1]) > f(x, y) + alpha * t * manual_gradient(x, y).dot(direction):
        t *= beta
    return t

def gradient_descent(starting_point, max_iterations=1000, tolerance=1e-6):
    x, y = starting_point
    best_solution = (x, y, f(x, y))
    for i in range(max_iterations):
        grad = manual_gradient(x, y)
        direction = -grad
        step_size = backtracking_line_search(x, y, direction)
        x = x + step_size * direction[0]
        y = y + step_size * direction[1]
        current_value = f(x, y)
        if current_value < best_solution[2]:
            best_solution = (x, y, current_value)
            save_solution(best_solution)
        if np.linalg.norm(grad) < tolerance:
            break
    return best_solution

def save_solution(solution):
    with open("best_solutions.txt", "a") as file:
        file.write(f"Solution: {solution[:2]}, Value: {solution[2]}\n")

def optimize_random_starting_points(num_starts=10):
    best_solution = None
    best_value = np.inf
    for _ in range(num_starts):
        starting_point = np.random.uniform(-100, 100, size=2)
        x, y, value = gradient_descent(starting_point)
        if value < best_value:
            best_solution = (x, y, value)
    return best_solution

if __name__ == "__main__":
    best_solution = optimize_random_starting_points()
    print("Best solution:", best_solution[:2])
    print("Best value:", best_solution[2])
