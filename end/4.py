def input_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    user_matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Введите значения для строки {i + 1} через пробел: ").split()))
        user_matrix.append(row)

    return user_matrix

def determinant(matrix):
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(size):
        minor_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(minor_matrix)

    return det

def find_eigenvalues(matrix):
    size = len(matrix)

    characteristic_poly = [1]
    for i in range(1, size + 1):
        characteristic_poly.append((-1) ** i * determinant(matrix[:i][:i]))

    eigenvalues = [0] * (size - 1)
    for i in range(size - 1):
        eigenvalues[i] = -characteristic_poly[i + 1] / characteristic_poly[i]

    return eigenvalues

# Пример использования
user_input_matrix = input_matrix()

eigenvalues = find_eigenvalues(user_input_matrix)

print("\nсобственные значения:")
for eigenvalue in eigenvalues:
    print(eigenvalue)
