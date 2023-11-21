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

# Example usage
user_input_matrix = input_matrix()
transposed_user_input_matrix = transpose_matrix(user_input_matrix)

# Print the original and transposed matrices
print("\nTransposed Matrix:")
for row in transposed_user_input_matrix:
    print(row)
