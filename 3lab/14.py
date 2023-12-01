import numpy as np

def manual_gradient(x, y, func):
    h = 1e-6
    df_dx = (func(x + h, y) - func(x - h, y)) / (2 * h)
    df_dy = (func(x, y + h) - func(x, y - h)) / (2 * h)
    return np.array([df_dx, df_dy])

def backtracking_line_search(x, y, direction, func, alpha=0.2, beta=0.8):
    t = 1.0
    while func(x + t * direction[0], y + t * direction[1]) > func(x, y) + alpha * t * manual_gradient(x, y, func).dot(direction):
        t *= beta
    return t

def gradient_descent(starting_point, func, max_iterations=5000, tolerance=1e-4, reset_iterations=1000):
    x, y = starting_point
    best_solution = (x, y, func(x, y))
    reset_counter = 0

    for i in range(max_iterations):
        grad = manual_gradient(x, y, func)
        direction = -grad
        step_size = backtracking_line_search(x, y, direction, func=func)
        x = x + step_size * direction[0]
        y = y + step_size * direction[1]
        current_value = func(x, y)

        if current_value < best_solution[2]:
            best_solution = (x, y, current_value)
            save_solution(best_solution, i + 1)  # Pass the line number where the solution was found

        if np.linalg.norm(grad) < tolerance:
            break

        reset_counter += 1
        if reset_counter >= reset_iterations:
            x, y = np.random.uniform(-100, 100, size=2)
            reset_counter = 0

    if best_solution[2] >= 4:
        best_solution = None

    return best_solution

def save_solution(solution, line_number):
    with open("best_solutions.txt", "a") as file:
        file.write(f"Line {line_number}: Solution: {solution[:2]}, Value: {solution[2]}\n")

def optimize_random_starting_points(func, num_starts=50):
    best_solution = None
    best_value = np.inf
    for _ in range(num_starts):
        starting_point = np.random.uniform(-100, 100, size=2)
        x, y, value = gradient_descent(starting_point, func)
        if value < best_value:
            best_solution = (x, y, value)
    return best_solution


if __name__ == "__main__":
    def custom_function(x, y):
        return np.sin(x + y)**2 + 5 + np.cos(y)**2 - np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25)

    best_solution = optimize_random_starting_points(custom_function)

    # Run additional iterations without resetting starting points
    for _ in range(5000):
        starting_point = np.random.uniform(-100, 100, size=2)
        x, y, value = gradient_descent(starting_point, custom_function, max_iterations=1, reset_iterations=np.inf)
        if value < best_solution[2]:
            best_solution = (x, y, value)

    # Check if the final solution has a value less than 4
    if best_solution[2] >= 4:
        starting_point = np.random.uniform(-100, 100, size=2)
        x, y, value = gradient_descent(starting_point, custom_function, max_iterations=1, reset_iterations=np.inf)
        if value < best_solution[2]:
            best_solution = (x, y, value)

    print("Best solution after iterations:", best_solution[:2])
    print("Best value after iterations:", best_solution[2])
