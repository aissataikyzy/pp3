import numpy as np

def custom_function(x, y):
    return np.sin(x + y)**2 + 5 + np.cos(y)**2 - np.exp(-(x**2 + y**2 + 146*y + 54*x + 6058)/25)

def manual_gradient(x, y):
    h = 1e-6
    df_dx = (custom_function(x + h, y) - custom_function(x - h, y)) / (2 * h)
    df_dy = (custom_function(x, y + h) - custom_function(x, y - h)) / (2 * h)
    return np.array([df_dx, df_dy])

def backtracking_line_search(x, y, direction, alpha=0.5, beta=0.8):
    t = 1.0
    while custom_function(x + t * direction[0], y + t * direction[1]) > custom_function(x, y) + alpha * t * manual_gradient(x, y).dot(direction):
        t *= beta
    return t

def gradient_descent(starting_point, max_iterations=1000, tolerance=1e-8):
    x, y = starting_point
    for i in range(max_iterations):
        grad = manual_gradient(x, y)
        direction = -grad
        step_size = backtracking_line_search(x, y, direction)
        x = x + step_size * direction[0]
        y = y + step_size * direction[1]
        current_value = custom_function(x, y)
        print(f"Iteration {i + 1}, Value: {current_value}")
        if current_value < 5:
            print("Converged to a value below 5.")
            break
        if np.linalg.norm(grad) < tolerance:
            print("Converged to a local minimum.")
            break
    return x, y, custom_function(x, y)

if __name__ == "__main__":
    starting_point = np.random.uniform(-100, 100, size=2)
    result = gradient_descent(starting_point)
    print("Final solution:", result[:2])
    print("Final value:", result[2])
