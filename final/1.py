# Ввод функции от переменных
def input_function(num_vars):
    expression = input(f"Введите функцию от {num_vars} переменных (используйте x[1], x[2], ..., x[{num_vars}]): ")
    return lambda x: eval(expression, {'x{}'.format(i+1): x[i] for i in range(num_vars)})

# Численное вычисление первой производной (градиента)
def gradient(x, func, num_vars, h=1e-5):
    grad = []
    for i in range(num_vars):
        x_plus_h = x.copy()
        x_minus_h = x.copy()
        x_plus_h[i] += h
        x_minus_h[i] -= h
        grad_i = (func(x_plus_h) - func(x_minus_h)) / (2 * h)
        grad.append(grad_i)
    return grad

# Численное вычисление второй производной (гессиана)
def hessian(x, func, num_vars, h=1e-5):
    hess = []
    for i in range(num_vars):
        row = []
        x_plus_h = x.copy()
        x_minus_h = x.copy()
        x_plus_h[i] += h
        x_minus_h[i] -= h
        for j in range(num_vars):
            hess_ij = (func(x_plus_h) - 2 * func(x) + func(x_minus_h)) / (h ** 2)
            row.append(hess_ij)
        hess.append(row)
    return hess

# Ввод количества переменных
num_variables = int(input("Введите количество переменных: "))

# Ввод функции
user_function = input_function(num_variables)

# Пример использования
x_values = [float(input(f"Введите начальное значение переменной x{i + 1}: ")) for i in range(num_variables)]
grad = gradient(x_values, user_function, num_variables)
hessi = hessian(x_values, user_function, num_variables)
print("Градиент:", grad)
print("Гессиан:", hessi)
