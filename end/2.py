import math

def dot_product(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            val = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(val)
        result.append(row)
    return result

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def normalize_vector(vector):
    magnitude = math.sqrt(sum(val * val for val in vector))
    return [val / magnitude for val in vector]

def scale_matrix(matrix, scalar):
    return [[val * scalar for val in row] for row in matrix]

def subtract_matrices(matrix1, matrix2):
    return [[val1 - val2 for val1, val2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

def power_iteration(matrix):
    n = len(matrix)
    b = [1] * n
    for _ in range(50):
        b = normalize_vector(dot_product(matrix, [b])[0])  # Fix here: select the first inner list [b] 
    eigenvalue = dot_product([b], dot_product(matrix, [b]))[0][0]
    return eigenvalue, b

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


def SVD(matrix):
    # Calculate A^T * A
    ATA = dot_product(transpose(matrix), matrix)

    # Find dominant eigenvalue and eigenvector of A^T * A using power iteration
    eigenvalue, eigenvector = power_iteration(ATA)

    # Calculate singular value and normalize eigenvector
    singular_value = math.sqrt(eigenvalue)
    U = [normalize_vector([eigenvector])]

    # Calculate V
    V_temp = []
    AV = dot_product(matrix, U[0])
    V_temp.append(normalize_vector(AV))
    V = transpose(V_temp)

    # Construct diagonal matrix Sigma
    Sigma = [[0] * len(V[0]) for _ in range(len(U))]
    Sigma[0][0] = singular_value

    return U, Sigma, V


matrix = input_square_matrix()
U, Sigma, V = SVD(matrix)

print("\nSingular Value Decomposition:")
print("U:")
for row in U:
    print(row)

print("\nSigma:")
for row in Sigma:
    print(row)

print("\nV:")
for row in V:
    print(row)
