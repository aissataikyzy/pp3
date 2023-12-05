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

def determinant(a_list):
    matrix_size = len(a_list)
    if matrix_size == 2:
        return a_list[0][0] * a_list[1][1] - a_list[0][1] * a_list[1][0]
    elif matrix_size == 3:
        return a_list[0][0] * (a_list[1][1] * a_list[2][2] - a_list[1][2] * a_list[2][1]) - \
               a_list[0][1] * (a_list[1][0] * a_list[2][2] - a_list[2][0] * a_list[1][2]) + \
               a_list[0][2] * (a_list[1][0] * a_list[2][1] - a_list[2][0] * a_list[1][1])
    elif matrix_size == 4:
        return a_list[0][0] * (a_list[1][1] * (a_list[2][2] * a_list[3][3] - a_list[2][3] * a_list[3][2]) - \
                               a_list[1][2] * (a_list[2][1] * a_list[3][3] - a_list[3][1] * a_list[2][3]) + \
                               a_list[1][3] * (a_list[2][1] * a_list[3][2] - a_list[3][1] * a_list[2][2])) - \
               a_list[0][1] * (a_list[1][0] * (a_list[2][2] * a_list[3][3] - a_list[2][3] * a_list[3][2]) - \
                               a_list[1][2] * (a_list[2][0] * a_list[3][3] - a_list[3][0] * a_list[2][3]) + \
                               a_list[1][3] * (a_list[2][0] * a_list[3][2] - a_list[3][0] * a_list[2][2])) + \
               a_list[0][2] * (a_list[1][0] * (a_list[2][1] * a_list[3][3] - a_list[2][3] * a_list[3][1]) - \
                               a_list[1][1] * (a_list[2][0] * a_list[3][3] - a_list[3][0] * a_list[2][3]) + \
                               a_list[1][3] * (a_list[2][0] * a_list[3][1] - a_list[3][0] * a_list[2][1])) - \
               a_list[0][3] * (a_list[1][0] * (a_list[2][1] * a_list[3][2] - a_list[2][2] * a_list[3][1]) - \
                               a_list[1][1] * (a_list[2][0] * a_list[3][2] - a_list[3][0] * a_list[2][2]) + \
                               a_list[1][2] * (a_list[2][0] * a_list[3][1] - a_list[3][0] * a_list[2][1]))





# Example usage
user_input_matrix = input_square_matrix()
transposed_user_input_matrix = transpose_matrix(user_input_matrix)
result = multiply_transpose_by_matrix(user_input_matrix)
determinant_value = determinant(user_input_matrix)

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
