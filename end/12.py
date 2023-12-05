import numpy as np
from tkinter import Tk, Frame, Label, Button, OptionMenu, StringVar, Entry


def input_square_matrix():
    while True:
        size = int(input("Enter the size of the square matrix (e.g., for a 2x2 matrix, enter 2): "))
        
        if size < 2:
            print("Matrix size must be at least 2x2. Please enter a valid size.")
        else:
            break

    user_matrix = []

    for i in range(size):
        row = list(map(int, input(f"Enter values for row {i + 1} separated by space: ").split()))
        
        if len(row) != size:
            print(f"Invalid number of elements in the row. Please enter {size} values.")
            i -= 1  # Decrement the index to re-enter the current row
            continue
        
        user_matrix.append(row)

    print("\nMatrix entered by the user:")
    for row in user_matrix:
        print(row)

    return user_matrix

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

def determinant(matrix):
    matrix_size = len(matrix)
    if matrix_size == 2:
        return determinant2(matrix)
    elif matrix_size == 3:
        return determinant3(matrix)
    # elif matrix_size == 4:
    #     return determinant4(matrix)

def determinant2(matrix):
    transposed_matrix = multiply_transpose_by_matrix(matrix)
    return transposed_matrix[0][0] * transposed_matrix[1][1] - transposed_matrix[0][1] * transposed_matrix[1][0]

def determinant3(matrix):
    transposed_matrix = multiply_transpose_by_matrix(matrix)
    return (
        transposed_matrix[0][0] * (transposed_matrix[1][1] * transposed_matrix[2][2] - transposed_matrix[1][2] * transposed_matrix[2][1]) -
        transposed_matrix[0][1] * (transposed_matrix[1][0] * transposed_matrix[2][2] - transposed_matrix[2][0] * transposed_matrix[1][2]) +
        transposed_matrix[0][2] * (transposed_matrix[1][0] * transposed_matrix[2][1] - transposed_matrix[2][0] * transposed_matrix[1][1])
    )


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

    discriminant = (a + d)**2 - 4 * (a * d - b * c)

    if discriminant >= 0:
        eigenvalue1 = (a + d + discriminant**0.5) / 2
        eigenvalue2 = (a + d - discriminant**0.5) / 2
        return [eigenvalue1, eigenvalue2]
    else:
        real_part = (a + d) / 2
        imaginary_part = (-discriminant)**0.5 / 2
        eigenvalue1 = complex(real_part, imaginary_part)
        eigenvalue2 = complex(real_part, -imaginary_part)
        return [eigenvalue1, eigenvalue2]

def find_eigenvalues_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    # Define the coefficients of the characteristic polynomial
    p = -(a + e + i)
    q = a*e + a*i + e*i - b*d - c*f - g*h
    r = -a*e*i + a*f*h + b*d*i - b*f*g - c*d*h + c*g*f

    # Use numpy's roots function to find the roots of the cubic equation
    coefficients = [1, p, q, r]
    eigenvalues = np.roots(coefficients)

    return eigenvalues

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
    return sum(x**2 for x in v)**0.5

def gaussian_elimination(A, b):
    n = len(b)
    augmented_matrix = np.column_stack((A, b))

    for i in range(n):
        pivot_row = next((j for j in range(i, n) if augmented_matrix[j, i] != 0), None)

        if pivot_row is not None:
            if pivot_row != i:
                augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]

            diag_value = augmented_matrix[i, i]
            augmented_matrix[i, :] /= diag_value

            for j in range(i + 1, n):
                factor = augmented_matrix[j, i]
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.sum(augmented_matrix[i, i+1:n] * x[i+1:])

    return x

def normalize_vector(v):
    norm = sum(x**2 for x in v)**0.5
    if norm == 0:
        return v
    return np.array([x / norm for x in v])


def power_iteration(matrix, initial_guess, max_iterations=100, tolerance=1e-10):
    v = normalize_vector(initial_guess)
    
    for _ in range(max_iterations):
        v_new = np.dot(matrix, v)
        eigenvalue = np.dot(v, v_new)
        
        if np.linalg.norm(v_new - eigenvalue * v) < tolerance:
            break
        
        v = normalize_vector(v_new)

    return eigenvalue, normalize_vector(v)


def find_eigenvectors_2x2(matrix):
    eigenvalues = find_eigenvalues_2x2(matrix)
    eigenvectors = []

    for eigenvalue in eigenvalues:
        system_matrix = matrix - eigenvalue * np.identity(2)
        _, normalized_v = power_iteration(system_matrix, np.random.rand(2))
        
        # Ensure that the eigenvector is unique by checking eigenvalues
        is_unique = all(
            not np.allclose(eigenvalue, ev[0]) for ev in eigenvectors
        )
        
        # Check if the eigenvalue and eigenvector are unique
        if is_unique:
            eigenvectors.append((eigenvalue, normalized_v))

    return eigenvectors

def find_eigenvectors_3x3(matrix):
    eigenvalues = find_eigenvalues_3x3(matrix)
    eigenvectors = []

    for eigenvalue in eigenvalues:
        system_matrix = matrix - eigenvalue * np.identity(3)
        _, normalized_v = power_iteration(system_matrix, np.random.rand(3))
        
        # Ensure that the eigenvector is unique by checking eigenvalues
        is_unique = all(
            not np.allclose(eigenvalue, ev[0]) for ev in eigenvectors
        )
        
        # Check if the eigenvalue and eigenvector are unique
        if is_unique:
            eigenvectors.append((eigenvalue, normalized_v))

    return eigenvectors
"""

def SVD(A):
    def Norm(v):
        sqs = 0
        for i in v:
            sqs += (i**2)
        return np.sqrt(sqs)

    def rel_err(x1, x0):
        return abs((x1 - x0) / x1) * 100

    def ev(a):
        x = np.array([[np.random() for i in range(len(a))]])
        max_iter = 10
        old_eigval = 0
        tlr = 0.5
        for i in range(max_iter):
            x = np.dot(a, x.T)
            eigval = Norm(x.T)
            error = rel_err(eigval, old_eigval)
            x = x / eigval
            e, res = [eigval, x]
            if tlr < 0.5:
                break
            old_eigval = eigval
        return e, res

    A = np.array(A)  # Convert input to NumPy array
    B = A.T @ A
    eig, V = ev(B)

    if len(A) == 2:
        u0 = A @ V[:, 0] / Norm(A @ V[:, 0])
        u1 = A @ V[:, 1] / Norm(A @ V[:, 1])
        U = np.array([u0, u1])
    else:
        u0 = A @ V[:, 0] / Norm(A @ V[:, 0])
        u1 = A @ V[:, 1] / Norm(A @ V[:, 1])
        u2 = A @ V[:, 2] / Norm(A @ V[:, 2])
        U = np.array([u0, u1, u2])
    U = U.T

    D = np.round(U.T @ A @ V, decimals=5)
    D = np.where(np.eye(D.shape[0], dtype=bool), D, 0)

    return U, D, V
"""

"""

def power_iteration(matrix, initial_guess, max_iterations=100, tolerance=1e-10):
    v = normalize_vector(initial_guess)
    
    for _ in range(max_iterations):
        v_new = np.dot(matrix, v)
        eigenvalue = np.dot(v, v_new)
        
        if np.linalg.norm(v_new - eigenvalue * v) < tolerance:
            break
        
        v = normalize_vector(v_new)

    return eigenvalue, normalize_vector(v)

def normalize_vector(v):
    return v / np.linalg.norm(v)

def find_eigenvectors(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    eigenvectors = []

    for eigenvalue in eigenvalues:
        system_matrix = matrix - eigenvalue * np.identity(matrix.shape[0])
        _, normalized_v = power_iteration(system_matrix, np.random.rand(matrix.shape[0]))
        
        # Ensure that the eigenvector is unique by checking eigenvalues
        is_unique = all(
            not np.allclose(eigenvalue, ev[0]) for ev in eigenvectors
        )
        
        # Check if the eigenvalue and eigenvector are unique
        if is_unique:
            eigenvectors.append((eigenvalue, normalized_v))

    return eigenvectors
"""
def SVD(matrix):
    eigenvectors = find_eigenvectors(np.dot(matrix, matrix.T))
    
    # Construct matrix U
    U = [ev[1] for ev in eigenvectors]
    
    # Construct matrix Sigma
    singular_values = [np.sqrt(abs(ev[0])) for ev in eigenvectors]
    Sigma = np.diag(singular_values)
    
    # Construct matrix V
    V = [np.dot(matrix.T, ev[1]) for ev in eigenvectors]
    
    return U, Sigma, V

def PD(matrix):
    U, Sigma, V = SVD(matrix)
    
    # Construct matrix P
    P = np.dot(U.T, matrix)
    
    return U, P
"""

# Example usage
user_input_matrix = input_square_matrix()
transposed_user_input_matrix = transpose_matrix(user_input_matrix)
result = multiply_transpose_by_matrix(user_input_matrix)
eigen_val = find_eigenvalues(result)
print("Eigenvalues:", eigen_val)
eigen_vec = find_eigenvectors(result)
print("Eigenvectors:", eigen_vec)


U, D, V = SVD(result)

# Print the result
print("Matrix U:")
print(U)
print("\nMatrix D:")
print(D)
print("\nMatrix V:")
print(V)

U, P = PD(result)
print("\nPolar Decomposition:")
print("Matrix U:")
print(U)
print("\nMatrix P:")
print(P)
"""


class MatrixCalculator:

    def __init__(self, master):
        self.master = master
        self.master.title('Calculate SVD and PD')
        self.master["bg"] = '#F5EFF6'

        self.window_width = 500
        self.window_height = 500
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.x_position = (self.screen_width - self.window_width) // 2
        self.y_position = (self.screen_height - self.window_height) // 2

        self.master.geometry(f'{self.window_width}x{self.window_height}+{self.x_position}+{self.y_position}')

        self.welcome_label = Label(self.master, text='Welcome!', font=('Comic Sans Ms', 50), fg='#bb88d3', bg='#F5EFF6')
        self.welcome_label.place(x=125, y=90)

        self.start_button = Button(self.master, text='Start', font=('Comic Sans Ms', 15), fg='#bb88d3', bg='white', command=self.choose)
        self.start_button.place(x=200, y=180)

        self.result = StringVar()
        self.frame1 = None
        self.frame2 = None

    def go_back(self):
        if self.frame1:
            self.frame1.destroy()
            self.frame1 = None

        if self.frame2:
            self.frame2.place_forget()
        self.welcome_label.place(x=125, y=90)
        self.start_button.place(x=200, y=180)

    def calculate(self, method):

        def solve(self):
            pass

        if self.frame1:
            self.frame1.destroy()

        size = int(self.size_var.get()[0])
        entries = []

        cell_size = 50
        cell_padding = 10
        dx = 120
        dy = 150

        for i in range(size):
            for j in range(size):
                x = j * cell_size + cell_padding + dx
                y = i * cell_size + cell_padding + dy

                entry = Entry(self.frame2, width=3)
                entry.place(x=x, y=y)
                entries.append(entry)

        matrix_label = Label(self.frame2, text=f"Calculate {method} for {size}x{size} matrix", font=('Comic Sans Ms', 14), fg='#bb88d3', bg='#F5EFF6')
        matrix_label.place(x=40, y=300)

        calculate_button = Button(self.frame2, text="Calculate", font=('Comic Sans Ms', 14), fg='#bb88d3', command=solve)
        calculate_button.place(x=150, y=350)



    def select(self, method):
        if self.frame1:
            self.frame1.destroy()

        self.result.set(f"Performing {method}...")

        self.frame2 = Frame(self.master, bg='#F5EFF6', width=500, height=500)
        self.frame2.place(x=50, y=20)

        select_size_label = Label(self.frame2, text='Please select size of matrix!', font=('Comic Sans Ms', 24), fg='#bb88d3', bg='#F5EFF6')
        select_size_label.place(x=30, y=30)

        self.size_var = StringVar(value="2x2")

        option_menu = OptionMenu(self.frame2, self.size_var, "2x2", "3x3")
        option_menu.place(x=150, y=75)

        select1_button = Button(self.frame2, text="Select", font=('Comic Sans Ms', 12), fg='#bb88d3', command=lambda: self.calculate(method))
        select1_button.place(x=250, y=75)

    def choose(self):
        self.welcome_label.place_forget()
        self.start_button.place_forget()

        self.frame1 = Frame(self.master, bg='#F5EFF6', width=500, height=500)
        self.frame1.place(x=50, y=20)

        choose_label = Label(self.frame1, text='Please select one!', font=('Comic Sans Ms', 24), fg='#bb88d3', bg='#F5EFF6')
        choose_label.place(x=100, y=80)

        options = ["Singular value decomposition", "Polar decomposition"]
        var = StringVar(value=options[0])

        option_menu = OptionMenu(self.frame1, var, *options)
        option_menu.place(x=100, y=130)

        self.back_button = Button(self.frame1, text="Main menu", font=('Comic Sans Ms', 12), fg='#bb88d3',  command=self.go_back)
        self.back_button.place(x=10, y=300)

        self.result_label = Label(self.frame1, textvariable=self.result)
        self.result_label.place(x=50, y=150)

        select_button = Button(self.frame1, text="Select", font=('Comic Sans Ms', 12), fg='#bb88d3', command=lambda: self.select(var.get()))
        select_button.place(x=300, y=300)


class MatrixCalculator:

    # ... (Your existing code above)

    def calculate(self, method):
        if self.frame1:
            self.frame1.destroy()

        size = int(self.size_var.get()[0])
        entries = []

        cell_size = 50
        cell_padding = 10
        dx = 120
        dy = 150

        for i in range(size):
            for j in range(size):
                x = j * cell_size + cell_padding + dx
                y = i * cell_size + cell_padding + dy

                entry = Entry(self.frame2, width=3)
                entry.place(x=x, y=y)
                entries.append(entry)

        matrix_label = Label(self.frame2, text=f"Calculate {method} for {size}x{size} matrix", font=('Comic Sans Ms', 14), fg='#bb88d3', bg='#F5EFF6')
        matrix_label.place(x=40, y=300)

        def solve():
            matrix_values = [[int(entry.get()) for entry in row] for row in entries]
            matrix = np.array(matrix_values)

            if method == "Singular value decomposition":
                U, Sigma, V = SVD(matrix)
                self.result.set(f"Matrix U:\n{U}\n\nMatrix Sigma:\n{Sigma}\n\nMatrix V:\n{V}")
            elif method == "Polar decomposition":
                U, P = PD(matrix)
                self.result.set(f"Matrix U:\n{U}\n\nMatrix P:\n{P}")

        calculate_button = Button(self.frame2, text="Calculate", font=('Comic Sans Ms', 14), fg='#bb88d3', command=solve)
        calculate_button.place(x=150, y=350)
        

root = Tk()
app = MatrixCalculator()
root.mainloop()