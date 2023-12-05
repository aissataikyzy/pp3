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


# def power_iteration(matrix, initial_guess, max_iterations=100, tolerance=1e-10):
#     v = normalize_vector(initial_guess)
    
#     for _ in range(max_iterations):
#         v_new = np.dot(matrix, v)
#         eigenvalue = np.dot(v, v_new)
        
#         if np.linalg.norm(v_new - eigenvalue * v) < tolerance:
#             break
        
#         v = normalize_vector(v_new)

#     return eigenvalue, normalize_vector(v)


def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

def solve_lu_decomposition(L, U, b):
    n = len(b)

    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = b
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return x


def inverse_iteration(matrix, eigenvalue, initial_guess, max_iterations=100, tolerance=1e-10):
    n = np.array((matrix))
    m = n.shape[0]
    I = np.eye(m)
    A = n - eigenvalue * I  

    v = initial_guess

    for _ in range(max_iterations):
        L, U = lu_decomposition(A)
        v_new = solve_lu_decomposition(L, U, v)
        v_new /= norm(v_new)  
        if norm(v - v_new) < tolerance:
            break
        v = v_new
        
    return v_new


def find_eigenvectors_2x2(matrix):
    # eigenvalues = find_eigenvalues_2x2(matrix)
    # eigenvectors = []

    # for eigenvalue in eigenvalues:
    #     system_matrix = matrix - eigenvalue * np.identity(2)
    #     _, normalized_v = power_iteration(system_matrix, np.random.rand(2))
        
    #     # Ensure that the eigenvector is unique by checking eigenvalues
    #     is_unique = all(
    #         not np.allclose(eigenvalue, ev[0]) for ev in eigenvectors
    #     )
        
    #     # Check if the eigenvalue and eigenvector are unique
    #     if is_unique:
    #         eigenvectors.append(normalized_v)

    # return eigenvectors
    eigval = find_eigenvalues(matrix)
    e1, e2 = eigval[0], eigval[1]
    v1 = inverse_iteration(multiply_transpose_by_matrix(matrix), e1, np.random.rand(2))
    v2 = inverse_iteration(multiply_transpose_by_matrix(matrix), e2, np.random.rand(2))
    V = np.array((v1, v2))
    
    return V
    

def find_eigenvectors_3x3(matrix):
    # eigenvalues = find_eigenvalues_3x3(matrix)
    # eigenvectors = []

    # for eigenvalue in eigenvalues:
    #     system_matrix = matrix - eigenvalue * np.identity(3)
    #     _, normalized_v = power_iteration(system_matrix, np.random.rand(3))
        
    #     # Ensure that the eigenvector is unique by checking eigenvalues
    #     is_unique = all(
    #         not np.allclose(eigenvalue, ev[0]) for ev in eigenvectors
    #     )
        
    #     # Check if the eigenvalue and eigenvector are unique
    #     if is_unique:
    #         eigenvectors.append(normalized_v)

    # return eigenvectors
    eigval = find_eigenvalues(matrix)
    e1, e2, e3 = eigval[0], eigval[1], eigval[2]
    v1 = inverse_iteration(multiply_transpose_by_matrix(matrix), e1, np.random.rand(3))
    v2 = inverse_iteration(multiply_transpose_by_matrix(matrix), e2, np.random.rand(3))
    v3 = inverse_iteration(multiply_transpose_by_matrix(matrix), e3, np.random.rand(3))
    V = np.array((v1, v2, v3))
    
    return V
    
    

def manual_svd(matrix):    
    n = np.array((matrix))
    # Construct matrix Sigma
    singular_values = find_eigenvalues(multiply_transpose_by_matrix(matrix))
    Sigma = [[np.sqrt(singular_values[i]) if j == i else 0 for j in range(len(singular_values))] for i in range(len(singular_values))]
    
    # Construct matrix V
    V = find_eigenvectors(matrix)
    V = V.T
    
    # Construct matrix U
    U_1 = (np.dot(matrix, V))
    U_1 = transpose_matrix(U_1)
    U_1 = [normalize_vector(i) for i in U_1]
    U_1 = transpose_matrix(U_1)
    U = np.dot(U_1, transpose_matrix(Sigma))
    U = transpose_matrix(U)
    U = [normalize_vector(i) for i in U]
    U = transpose_matrix(U)
    
    return U, Sigma, V

# Example usage
user_input_matrix = input_square_matrix()
transposed_user_input_matrix = transpose_matrix(user_input_matrix)
result = multiply_transpose_by_matrix(user_input_matrix)
eigen_val = find_eigenvalues(result)
print("Eigenvalues:", eigen_val)
eigen_vec = find_eigenvectors(result)
print("Eigenvectors:", eigen_vec)

U, Sigma, V = manual_svd(user_input_matrix)

# Print the result
print("Matrix U:")
for row in U:
    print(row)

print("\nMatrix Sigma:")
for row in Sigma:
    print(row)

print("\nMatrix V:")
for row in V:
    print(row)