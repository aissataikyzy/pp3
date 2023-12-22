import math

def polynomial_derivative(coefs, order):
    derivative_coefs = coefs.copy()
    for _ in range(order):
        derivative_coefs = [i * derivative_coefs[i] for i in range(1, len(derivative_coefs))]
    return derivative_coefs

def evaluate_polynomial(coefs, x):
    return sum(coef * x ** i for i, coef in enumerate(coefs))

def taylor_series_coefficients(func_coefs, order, x0):
    taylor_coefs = []
    for n in range(order + 1):
        derivative_coefs = polynomial_derivative(func_coefs, n)
        taylor_coef = evaluate_polynomial(derivative_coefs, x0) / math.factorial(n)
        taylor_coefs.append(taylor_coef)
    return taylor_coefs

# Для f(x) = 2 + x^2 + x^3 + x^7
func_coefs = [2, 0, 1, 1, 0, 0, 0, 1]

# Вычисление коэффициентов ряда Тейлора до 7-го порядка включительно в точке x0 = 0
taylor_coefs = taylor_series_coefficients(func_coefs, 7, 0)

print("Коэффициенты ряда Тейлора:", taylor_coefs)
