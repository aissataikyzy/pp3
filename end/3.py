def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    user_matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter values for row {i + 1} separated by space: ").split()))
        user_matrix.append(row)

    print("\nMatrix entered by the user:")
    for row in user_matrix:
        print(row)

    return user_matrix

def transpose_matrix(matrix):
    # Get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])

    # Create a new matrix with swapped rows and columns
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix

def multiply_transpose_by_matrix(matrix):
    # Get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])

    # Transpose the matrix
    transposed_matrix = transpose_matrix(matrix)

    # Initialize the result matrix with zeros
    result_matrix = [[0] * cols for _ in range(cols)]

    # Perform matrix multiplication
    for i in range(cols):
        for j in range(cols):
            # Calculate the dot product of the i-th row of the transposed matrix and the j-th column of the original matrix
            result_matrix[i][j] = sum(transposed_matrix[i][k] * matrix[k][j] for k in range(rows))

    return result_matrix

# Example usage
user_input_matrix = input_matrix()
transposed_user_input_matrix = transpose_matrix(user_input_matrix)
result = multiply_transpose_by_matrix(user_input_matrix)

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
