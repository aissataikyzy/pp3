import numpy as np

def f(x, y):
    return np.sin(x + y)**2 + 5 + np.cos(y)**2 - np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25)

def manual_gradient(x, y):
    df_dx = 2 * (np.sin(x + y) * np.cos(x + y) - (2 * x + 54) * np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25) / 25)
    df_dy = 2 * (np.sin(x + y) * np.cos(x + y) + (2 * y + 146) * np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25) / 25)
    return np.array([df_dx, df_dy])

def backtracking_line_search(x, y, direction, alpha=0.2, beta=0.8):
    t = 1.0
    while f(x + t * direction[0], y + t * direction[1]) > f(x, y) + alpha * t * manual_gradient(x, y).dot(direction):
        t *= beta
    return t

def gradient_descent(starting_point, max_iterations=5000, tolerance=1e-4, reset_iterations=1000):
    x, y = starting_point
    best_solution = (x, y, f(x, y))
    reset_counter = 0

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

        if current_value < 5 or current_value > 5.3:
            break

        reset_counter += 1
        if reset_counter >= reset_iterations:
            x, y = np.random.uniform(-100, 100, size=2)
            reset_counter = 0

    return best_solution

def save_solution(solution):
    with open("best_solutions.txt", "a") as file:
        file.write(f"Solution: {solution[:2]}, Value: {solution[2]}\n")

def optimize_random_starting_points(num_starts=50):
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
    print("Best solution after random starts:", best_solution[:2])
    print("Best value after random starts:", best_solution[2])

    # Run additional iterations without resetting starting points
    for _ in range(5000):
        starting_point = np.random.uniform(-100, 100, size=2)
        x, y, value = gradient_descent(starting_point, max_iterations=1, reset_iterations=np.inf)
        if value < best_solution[2] and value < 5.3:
            best_solution = (x, y, value)

    print("Best solution after additional iterations:", best_solution[:2])
    print("Best value after additional iterations:", best_solution[2])
