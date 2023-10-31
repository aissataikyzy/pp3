# l = input()
# l1 = l.split()
# l2 = 0
# for i in l1:
#     l2 += float(i)
# print(l2)

# l = input()
# l1 = l.split()
# l2 = 0
# l3 = 0
# for i in l1:
#     l2 += 1
#     l3 += float(i)
# print(l3/l2)

def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Матрица должна быть размером 2x2")
    
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    det = a * d - b * c
    return det

def determinant_3x3(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        raise ValueError("Матрица должна быть размером 3x3")
    
    a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
    d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
    g, h, i = matrix[2][0], matrix[2][1], matrix[2][2]
    
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

# Считывание элементов матрицы
def read_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Введите элемент ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix

# Вывод результата
matrix_size = int(input("Введите размер матрицы (2 или 3): "))
if matrix_size == 2:
    matrix = read_matrix()
    det = determinant_2x2(matrix)
    print(f"Определитель: {det}")
elif matrix_size == 3:
    matrix = read_matrix()
    det = determinant_3x3(matrix)
    print(f"Определитель: {det}")
else:
    print("Поддерживаются только матрицы размером 2x2 и 3x3.")
