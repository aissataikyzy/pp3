import numpy as np

def backtracking_line_search(x, y, direction, func, alpha=0.5, beta=0.8):
    t = 1.0
    while func(x + t * direction[0], y + t * direction[1]) > func(x, y) + alpha * t * custom_manual_gradient(x, y, func).dot(direction):
        t *= beta
    return t

def gradient_descent(starting_point, func, manual_gradient_func, max_iterations=5000, tolerance=1e-6):
    x, y = starting_point
    best_solution = (x, y, func(x, y))
    for i in range(max_iterations):
        grad = manual_gradient_func(x, y, func)
        direction = -grad
        step_size = backtracking_line_search(x, y, direction, func=func)
        x = x + step_size * direction[0]
        
        y = y + step_size * direction[1]
        current_value = func(x, y)
        if current_value < best_solution[2]:
            best_solution = (x, y, current_value)
            save_solution(best_solution)
        if np.linalg.norm(grad) < tolerance:
            break
    return best_solution

def save_solution(solution):
    with open("best_solutions.txt", "a") as file:
        file.write(f"Solution: {solution[:2]}, Value: {solution[2]}\n")

def optimize_random_starting_points(func, manual_gradient_func, num_starts=10):
    best_solution = None
    best_value = np.inf
    for _ in range(num_starts):
        starting_point = np.random.uniform(-100, 100, size=2)
        x, y, value = gradient_descent(starting_point, func, manual_gradient_func)
        if value < best_value:
            best_solution = (x, y, value)
    return best_solution

if __name__ == "__main__":
    def custom_function(x, y):
        return np.sin(x + y)**2 + 5 + np.cos(y)**2 - np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25)

    def custom_manual_gradient(x, y, func):
        h = 1e-6
        df_dx = (func(x + h, y) - func(x - h, y)) / (2 * h)
        df_dy = (func(x, y + h) - func(x, y - h)) / (2 * h)
        return np.array([df_dx, df_dy])

    best_solution = optimize_random_starting_points(custom_function, custom_manual_gradient)
    print("Best solution:", best_solution[:2])
    print("Best value:", best_solution[2])
