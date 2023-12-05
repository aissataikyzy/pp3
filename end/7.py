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

def get_coefficients(matrix):
    matrix_size = len(matrix)

    if matrix_size == 2:
        return get_coefficients_2x2(matrix)
    elif matrix_size == 3:
        return get_coefficients_3x3(matrix)

def get_coefficients_2x2(matrix):
    transposed_matrix = multiply_transpose_by_matrix(matrix)
    a = -1
    b = transposed_matrix[0][0] + transposed_matrix[1][1]
    c = -(determinant2(matrix))
    l = [a, b, c]
    return l

def get_coefficients_3x3(matrix):
    transposed_matrix = multiply_transpose_by_matrix(matrix)
    a = -1
    b = transposed_matrix[0][0] + transposed_matrix[1][1] + transposed_matrix[2][2]
    
    c = transposed_matrix[0][0] * transposed_matrix[1][1] + transposed_matrix[1][1] * transposed_matrix[2][2] + transposed_matrix[2][2] * transposed_matrix[0][0] - transposed_matrix[0][1] * transposed_matrix[1][0] - transposed_matrix[1][2] * transposed_matrix[2][1] - transposed_matrix[2][0] * transposed_matrix[0][2]
    d = determinant3(matrix)
    return a, b, -c, d

def quadratic_roots(coefficients):
    a, b, c = coefficients
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return [root1, root2]
    else:
        return []

def cubic_roots(coefficients):
    a, b, c, d = coefficients
    # Coefficients of the depressed cubic equation x^3 + px^2 + qx + r
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    # Discriminant of the depressed cubic equation
    delta = (q/2)**2 + (p/3)**3

    # Case 1: Three real roots
    if delta > 0:
        u = (-q/2 + delta**0.5)**(1/3)
        v = (-q/2 - delta**0.5)**(1/3)
        roots = [u + v - b/(3*a)]
        return roots

    # Case 2: One real root
    elif delta == 0:
        if q >= 0:
            root = (-q/2)**(1/3)
        else:
            root = ((-q/2)**2)**(1/6)
        roots = [2 * root - b / (3 * a)]
        return roots

    # Case 3: Three real roots (complex)
    else:
        phi = (-q/2 + delta**0.5)**(1/3)
        roots = [phi * (i + 1) - b / (3 * a) for i in range(3)]
        return roots
    

def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def scalar_multiply(matrix, scalar):
    return [[matrix[i][j] * scalar for j in range(len(matrix[0]))] for i in range(len(matrix))]

def find_eigenvectors(matrix, eigenvalue):
    subtracted_matrix = subtract_matrices(matrix, scalar_multiply([[eigenvalue, 0, 0], [0, eigenvalue, 0], [0, 0, eigenvalue]], 1))
    
    # Form a system of linear equations
    system = [
        [subtracted_matrix[0][0], subtracted_matrix[0][1], subtracted_matrix[0][2], 0],
        [subtracted_matrix[1][0], subtracted_matrix[1][1], subtracted_matrix[1][2], 0],
        [subtracted_matrix[2][0], subtracted_matrix[2][1], subtracted_matrix[2][2], 0]
    ]

    # Apply Gaussian elimination to solve the system
    for i in range(len(system)):
        pivot = system[i][i]
        for j in range(i + 1, len(system)):
            factor = -system[j][i] / pivot
            for k in range(len(system[0])):
                system[j][k] += factor * system[i][k]

    # Back substitution
    eigenvector = [0, 0, 0]
    for i in range(len(system) - 1, -1, -1):
        eigenvector[i] = system[i][-1] / system[i][i]
        for j in range(i - 1, -1, -1):
            system[j][-1] -= system[j][i] * eigenvector[i]

    return eigenvector


# ... (previous code)

# Example usage
user_input_matrix = input_square_matrix()
transposed_user_input_matrix = transpose_matrix(user_input_matrix)
result = multiply_transpose_by_matrix(user_input_matrix)
determinant_value = determinant(user_input_matrix)
coefficients = get_coefficients(user_input_matrix)

# Print the original and transposed matrices
print("\nOriginal Matrix:")
for row in user_input_matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_user_input_matrix:
    print(row)

# Print the result of matrix multiplication
print("\nResult of Matrix Multiplication (Transpose * Matrix):")
for row in result:
    print(row)

# Print the determinant of the original matrix
print("\nDeterminant of the Original Matrix:")
print(determinant_value)

# Print the coefficients
print("\nCoefficients:")
print(coefficients)

# Find roots
if len(coefficients) == 4:
    eigenvalues = cubic_roots(coefficients)
    print("Eigenvalues for 3x3 matrix:", eigenvalues)
    # Find eigenvectors for each eigenvalue
    for eigenvalue in eigenvalues:
        eigenvector = find_eigenvectors(user_input_matrix, eigenvalue)
        print(f"Eigenvector for eigenvalue {eigenvalue}:", eigenvector)

elif len(coefficients) == 3:
    eigenvalues = quadratic_roots(coefficients)
    print("Eigenvalues for 2x2 matrix:", eigenvalues)
    # Find eigenvectors for each eigenvalue
    for eigenvalue in eigenvalues:
        eigenvector = find_eigenvectors(user_input_matrix, eigenvalue)
        print(f"Eigenvector for eigenvalue {eigenvalue}:", eigenvector)

else:
    print("Unsupported matrix size.")
