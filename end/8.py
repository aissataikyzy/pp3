import numpy as np

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

def SVD(matrix):
    eigenvectors = find_eigenvectors(np.dot(matrix, matrix.T))
    transpose_result = matrix.T

    # Construct matrix U
    U = [ev[1] for ev in eigenvectors]
    
    # Construct matrix Sigma
    singular_values = [np.sqrt(abs(ev[0])) for ev in eigenvectors]
    Sigma = np.diag(singular_values)
    
    # Construct matrix V
    V = [np.dot(transpose_result, ev[1]) for ev in eigenvectors]
    
    return U, Sigma, V

def PD(matrix):
    U, Sigma, V = SVD(matrix)
    
    # Construct matrix P
    P = np.dot(U.T, matrix)
    
    return U, Sigma, V, P


# Example usage
user_input_matrix = input_square_matrix()
transposed_user_input_matrix = transpose_matrix(user_input_matrix)
result = np.array(multiply_transpose_by_matrix(user_input_matrix))
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