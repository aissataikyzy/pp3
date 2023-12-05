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

def power_iteration(matrix, num_iterations=1000, tolerance=1e-6):
    """Find the dominant eigenvalue and eigenvector using power iteration."""
    n = len(matrix)
    
    # Initialize a random vector
    eigen_vector = [1.0] * n
    
    for _ in range(num_iterations):
        # Apply the matrix to the vector
        matrix_times_vector = [sum(matrix[i][k] * eigen_vector[k] for k in range(n)) for i in range(n)]
        
        # Find the dominant eigenvalue
        eigenvalue = sum(matrix_times_vector[i] * eigen_vector[i] for i in range(n))
        
        # Normalize the vector
        normalized_vector = [x / max(abs(x), 1e-10) for x in matrix_times_vector]
        
        # Check for convergence
        if sum((x - y)**2 for x, y in zip(normalized_vector, eigen_vector)) < tolerance:
            break
        
        eigen_vector = normalized_vector
    
    return eigenvalue, eigen_vector

def find_eigenvectors(matrix, eigenvalue):
    size = len(matrix)

    # Subtract eigenvalue times the identity matrix from the original matrix
    subtracted_matrix = [[matrix[i][j] - eigenvalue * (i == j) for j in range(size)] for i in range(size)]

    # Solve the system of linear equations (A - λI)x = 0
    # Using Gaussian elimination to row-reduce the augmented matrix [A - λI | 0]
    augmented_matrix = [subtracted_matrix[i] + [0] for i in range(size)]
    
    # Perform Gaussian elimination
    for i in range(size):
        pivot = augmented_matrix[i][i]
        for j in range(i + 1, size):
            factor = augmented_matrix[j][i] / pivot
            for k in range(size + 1):
                augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

    # Back-substitution to find the eigenvector
    eigenvector = [0] * size
    for i in range(size - 1, -1, -1):
        eigenvector[i] = augmented_matrix[i][-1] / augmented_matrix[i][i]
        for j in range(i - 1, -1, -1):
            augmented_matrix[j][-1] -= augmented_matrix[j][i] * eigenvector[i]

    return eigenvector

# Example usage:
user_matrix = input_square_matrix()
result_matrix = multiply_transpose_by_matrix(user_matrix)

print("\nMatrix obtained by multiplying the transpose by the matrix:")
for row in result_matrix:
    print(row)

eigenvalue, _ = power_iteration(result_matrix)
print("\nDominant Eigenvalue:", eigenvalue)

eigenvector = find_eigenvectors(result_matrix, eigenvalue)
print("Corresponding Eigenvector:", eigenvector)
