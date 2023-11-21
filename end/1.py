import numpy as np
def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    user_matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter values for row {i + 1} separated by space: ").split()))
        user_matrix.append(row)

    matrix_from_input = np.array(user_matrix)

    #print("\nMatrix entered by the user:")
    print(matrix_from_input)


#print(input_matrix())

def transpose_matrix(matrix):
    # Get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])

    # Create a new matrix with swapped rows and columns
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix

# Example usage
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)

# Print the original and transposed matrices
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
