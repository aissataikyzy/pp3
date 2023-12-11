import numpy as np
import tkinter as tk
from tkinter import messagebox

class MatrixCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")

        self.matrix = None
        self.result = None

        self.create_widgets()

    def create_widgets(self):
        # Matrix entry
        self.matrix_entry_label = tk.Label(self.root, text="Enter the values for each row in the matrix:")
        self.matrix_entry_label.pack()

        self.matrix_entry = tk.Entry(self.root)
        self.matrix_entry.pack()

        # SVD button
        self.svd_button = tk.Button(self.root, text="SVD", command=self.perform_svd)
        self.svd_button.pack()

        # PD button
        self.pd_button = tk.Button(self.root, text="Polar Decomposition", command=self.perform_pd)
        self.pd_button.pack()

    def perform_svd(self):
        matrix_str = self.matrix_entry.get()
        try:
            self.matrix = np.array(eval(matrix_str))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid matrix: {e}")
            return

        self.result = multiply_transpose_by_matrix(self.matrix)
        eigenvalues = find_eigenvalues(self.result)
        eigenvectors = find_eigenvectors(self.result)

        U, Sigma, V = manual_svd(eigenvectors)

        messagebox.showinfo("SVD Result", f"Matrix U:\n{U}\n\nMatrix Sigma:\n{Sigma}\n\nMatrix V:\n{V}")

    def perform_pd(self):
        matrix_str = self.matrix_entry.get()
        try:
            self.matrix = np.array(eval(matrix_str))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid matrix: {e}")
            return

        eigenvectors = find_eigenvectors(self.result)

        U, P, result_pd = manual_pd(eigenvectors, self.matrix)

        messagebox.showinfo("Polar Decomposition Result", f"Matrix N:\n{U}\n\nMatrix H:\n{result_pd}")


def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed_matrix


def multiply_transpose_by_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed_matrix = transpose_matrix(matrix)
    result_matrix = [[0] * cols for _ in range(cols)]

    for i in range(cols):
        for j in range(cols):
            result_matrix[i][j] = sum(transposed_matrix[i][k] * matrix[k][j] for k in range(rows))

    return result_matrix


# def determinant(a_list):
#     matrix_size = len(a_list)
#     if matrix_size == 2:
#         return a_list[0][0] * a_list[1][1] - a_list[0][1] * a_list[1][0]
#     elif matrix_size == 3:
#         return a_list[0][0] * (a_list[1][1] * a_list[2][2] - a_list[1][2] * a_list[2][1]) - \
#                a_list[0][1] * (a_list[1][0] * a_list[2][2] - a_list[2][0] * a_list[1][2]) + \
#                a_list[0][2] * (a_list[1][0] * a_list[2][1] - a_list[2][0] * a_list[1][1])
#     elif matrix_size == 4:
#         return a_list[0][0] * (a_list[1][1] * (a_list[2][2] * a_list[3][3] - a_list[2][3] * a_list[3][2]) - \
#                                a_list[1][2] * (a_list[2][1] * a_list[3][3] - a_list[3][1] * a_list[2][3]) + \
#                                a_list[1][3] * (a_list[2][1] * a_list[3][2] - a_list[3][1] * a_list[2][2])) - \
#                a_list[0][1] * (a_list[1][0] * (a_list[2][2] * a_list[3][3] - a_list[2][3] * a_list[3][2]) - \
#                                a_list[1][2] * (a_list[2][0] * a_list[3][3] - a_list[3][0] * a_list[2][3]) + \
#                                a_list[1][3] * (a_list[2][0] * a_list[3][2] - a_list[3][0] * a_list[2][2])) + \
#                a_list[0][2] * (a_list[1][0] * (a_list[2][1] * a_list[3][3] - a_list[2][3] * a_list[3][1]) - \
#                                a_list[1][1] * (a_list[2][0] * a_list[3][3] - a_list[3][0] * a_list[2][3]) + \
#                                a_list[1][3] * (a_list[2][0] * a_list[3][1] - a_list[3][0] * a_list[2][1])) - \
#                a_list[0][3] * (a_list[1][0] * (a_list[2][1] * a_list[3][2] - a_list[2][2] * a_list[3][1]) - \
#                                a_list[1][1] * (a_list[2][0] * a_list[3][2] - a_list[3][0] * a_list[2][2]) + \
#                                a_list[1][2] * (a_list[2][0] * a_list[3][1] - a_list[3][0] * a_list[2][1]))

def find_eigenvalues(matrix):
    if len(matrix) == 2:
        return find_eigenvalues_2x2(matrix)
    elif len(matrix) == 3:
        return find_eigenvalues_3x3(matrix)
    else:
        raise ValueError("Eigenvalues can only be computed for 2x2 or 3x3 matrices.")


def find_eigenvalues_2x2(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    discriminant = (a + d) ** 2 - 4 * (a * d - b * c)

    if discriminant >= 0:
        eigenvalue1 = (a + d + discriminant ** 0.5) / 2
        eigenvalue2 = (a + d - discriminant ** 0.5) / 2
        return [eigenvalue1, eigenvalue2]
    else:
        real_part = (a + d) / 2
        imaginary_part = (-discriminant) ** 0.5 / 2
        eigenvalue1 = complex(real_part, imaginary_part)
        eigenvalue2 = complex(real_part, -imaginary_part)
        return [eigenvalue1, eigenvalue2]


def find_eigenvalues_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    # Define the coefficients of the characteristic polynomial
    p = -(a + e + i)
    q = a * e + a * i + e * i - b * d - c * f - g * h
    r = -a * e * i + a * f * h + b * d * i - b * f * g - c * d * h + c * g * f

    # Use numpy's roots function to find the roots of the cubic equation
    coefficients = [1, p, q, r]
    eigenvalues = np.roots(coefficients)

    return eigenvalues


import numpy as np

def find_eigenvectors(matrix):
    if len(matrix) == 2:
        return find_eigenvectors_2x2(matrix)
    elif len(matrix) == 3:
        return find_eigenvectors_3x3(matrix)
    else:
        raise ValueError("Eigenvectors can only be computed for 2x2 or 3x3 matrices.")

def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def norm(v):
    return sum(x ** 2 for x in v) ** 0.5

def normalize_vector(v):
    norm_value = norm(v)
    if norm_value == 0:
        return v
    return [x / norm_value for x in v]

def custom_allclose(val1, val2, tol=1e-10):
    if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
        return abs(val1 - val2) < tol
    elif isinstance(val1, np.ndarray) and isinstance(val2, np.ndarray):
        return all(abs(x - y) < tol for x, y in zip(val1, val2))
    else:
        raise ValueError("Unsupported types for custom_allclose")

# Usage:
# is_close = custom_allclose(array1, array2, tolerance)


def power_iteration(matrix, initial_guess, max_iterations=100, tolerance=1e-10):
    v = normalize_vector(initial_guess)

    for _ in range(max_iterations):
        v_new = np.dot(matrix, v)
        eigenvalue = dot_product(v, v_new)

        # Calculate the Euclidean norm manually
        norm_diff = sum((x - y)**2 for x, y in zip(v_new, [eigenvalue * val for val in v]))

        if norm_diff < tolerance:
            break

        v = normalize_vector(v_new)

    return eigenvalue, normalize_vector(v)


def find_eigenvectors_2x2(matrix):
    eigenvalues = find_eigenvalues_2x2(matrix)
    eigenvectors = []

    for eigenvalue in eigenvalues:
        system_matrix = matrix - eigenvalue * np.identity(2)
        _, v = power_iteration(system_matrix, np.random.rand(2))

        print(f"Eigenvalue: {eigenvalue}, Eigenvector (before normalization): {v}")

        # Ensure that the eigenvector is unique by checking eigenvalues
        is_unique = all(
            not custom_allclose(eigenvalue, ev[0]) and custom_allclose(1.0, norm(ev[1])) for ev in eigenvectors
        )

        # Check if the eigenvalue and eigenvector are unique
        if is_unique:
            eigenvectors.append((eigenvalue, v))

    return eigenvectors


def find_eigenvectors_3x3(matrix):
    eigenvalues = find_eigenvalues_3x3(matrix)
    eigenvectors = []

    for eigenvalue in eigenvalues:
        system_matrix = matrix - eigenvalue * np.identity(3)
        _, v = power_iteration(system_matrix, np.random.rand(3))

        print(f"Eigenvalue: {eigenvalue}, Eigenvector (before normalization): {v}")

        # Ensure that the eigenvector is unique by checking eigenvalues
        is_unique = all(
            not custom_allclose(eigenvalue, ev[0]) and custom_allclose(1.0, norm(ev[1])) for ev in eigenvectors
        )

        # Check if the eigenvalue and eigenvector are unique
        if is_unique:
            eigenvectors.append((eigenvalue, v))

    return eigenvectors



def manual_svd(eigenvectors):
    # Construct matrix U using normalized eigenvectors
    U = [ev[1] for ev in eigenvectors]

    # Construct matrix Sigma
    singular_values = [np.sqrt(abs(ev[0])) for ev in eigenvectors]
    Sigma = [[singular_values[i] if j == i else 0 for j in range(len(U))] for i in range(len(U))]

    # Construct matrix V
    V = U

    return U, Sigma, V



def manual_pd(eigenvectors, matrix):
    # Construct matrix U, Sigma, and V
    U, Sigma, V = manual_svd(eigenvectors)

    # Convert U to a NumPy array
    U = np.array(U)

    # Construct matrix P
    P = np.sqrt(np.dot(matrix.T, matrix))

    # Construct matrix H
    result_pd = np.dot(U, np.dot(P, U.T))

    # Convert result_pd to a list
    result_pd = result_pd.tolist()

    return U.tolist(), P.tolist(), result_pd




# Main program
root = tk.Tk()
app = MatrixCalculatorApp(root)
root.mainloop()
