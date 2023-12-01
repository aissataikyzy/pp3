import numpy as np
import matplotlib.pyplot as plt

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

def gradient_descent(starting_point, func, max_iterations=5000, tolerance=1e-4, reset_iterations=1000, return_trajectory=False):
    x, y = starting_point
    best_solution = (x, y, func(x, y))
    reset_counter = 0
    trajectory = []

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

        if current_value < 5 or current_value > 5.3:  # Fix the condition here
            break

        reset_counter += 1
        if reset_counter >= reset_iterations:
            x, y = np.random.uniform(-100, 100, size=2)
            reset_counter = 0

        if return_trajectory:
            trajectory.append((x, y, current_value))

    if return_trajectory:
        return best_solution, trajectory
    else:
        return best_solution

def save_solution(solution, line_number):
    with open("best_solutions.txt", "a") as file:
        file.write(f"Line {line_number}: Solution: {solution[:2]}, Value: {solution[2]}\n")

def plot_optimization_progress(func, trajectory, ax=None):
    if ax is None:
        fig, ax = plt.subplots()

    x_vals = np.linspace(-100, 100, 400)
    y_vals = np.linspace(-100, 100, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = func(X, Y)

    contour = ax.contour(X, Y, Z, levels=20, cmap='viridis', alpha=0.8)
    x_vals = [point[0] for point in trajectory]
    y_vals = [point[1] for point in trajectory]
    ax.plot(x_vals, y_vals, marker='o', color='red', label='Optimization Trajectory')
    best_solution = min(trajectory, key=lambda x: x[2])
    ax.plot(best_solution[0], best_solution[1], marker='*', markersize=10, color='green', label='Best Solution')

    ax.set_title('Optimization Progress')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()

    plt.show()

def optimize_random_starting_points(func, num_starts=50, return_trajectory=False):
    best_solution = None
    best_value = np.inf
    trajectory = []

    for _ in range(num_starts):
        starting_point = np.random.uniform(-100, 100, size=2)
        result = gradient_descent(starting_point, func, return_trajectory=return_trajectory)

        if return_trajectory:
            try:
                x, y, value, current_trajectory = result
            except ValueError:
                x, y, value = result
                current_trajectory = []
        else:
            x, y, value = result
            current_trajectory = []

        if value < best_value:
            best_solution = (x, y, value)
            best_value = value
            if return_trajectory:
                trajectory = list(current_trajectory)

    if return_trajectory:
        return best_solution, trajectory
    else:
        return best_solution


if __name__ == "__main__":
    def custom_function(x, y):
        return np.sin(x + y)**2 + 5 + np.cos(y)**2 - np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25)

    best_solution, trajectory = optimize_random_starting_points(custom_function, num_starts=50, return_trajectory=True)

    for _ in range(5000):
        starting_point = np.random.uniform(-100, 100, size=2)
        x, y, value, current_trajectory = gradient_descent(starting_point, custom_function, max_iterations=1, reset_iterations=np.inf, return_trajectory=True)
        if value < best_solution[2]:
            best_solution = (x, y, value)
            trajectory = current_trajectory

    print("Best solution after iterations:", best_solution[:2])
    print("Best value after iterations:", best_solution[2])

    plot_optimization_progress(custom_function, trajectory)
