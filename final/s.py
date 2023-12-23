import numpy as np

# Objective function
def f(x1, x2, x3, x4, x5, t):
    return x1 * x2 + x3 * (x4**2) + x5

# Constraints
def g1(x1, x2, x3, x4, x5):
    return x1 * x2 * x3 - 130

def g2(x1, x2, x3, x4, x5):
    return x4**2 * x5 - 54

# first derivatives
def df_dx1(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1 + h, x2, x3, x4, x5, t) - f(x1 - h, x2, x3, x4, x5, t)) / (2 * h))


def df_dx2(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2 + h, x3, x4, x5, t) - f(x1, x2 - h, x3, x4, x5, t)) / (2 * h))


def df_dx3(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2, x3 + h, x4, x5, t) - f(x1, x2, x3 - h, x4, x5, t)) / (2 * h))


def df_dx4(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2, x3, x4 + h, x5, t) - f(x1, x2, x3, x4 - h, x5, t)) / (2 * h))


def df_dx5(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2, x3, x4, x5 + h, t) - f(x1, x2, x3, x4, x5 - h, t)) / (2 * h))

# second derivatives
def d2f_dx1(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1 + h, x2, x3, x4, x5, t) - 2 * f(x1, x2, x3, x4, x5, t) + f(x1 - h, x2, x3, x4, x5, t)) / (h ** 2))


def d2f_dx2(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2 + h, x3, x4, x5, t) - 2 * f(x1, x2, x3, x4, x5, t) + f(x1, x2 - h, x3, x4, x5, t)) / (h ** 2))


def d2f_dx3(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2, x3 + h, x4, x5, t) - 2 * f(x1, x2, x3, x4, x5, t) + f(x1, x2, x3 - h, x4, x5, t)) / (h ** 2))


def d2f_dx4(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2, x3, x4 + h, x5, t) - 2 * f(x1, x2, x3, x4, x5, t) + f(x1, x2, x3, x4 - h, x5, t)) / (h ** 2))


def d2f_dx5(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return ((f(x1, x2, x3, x4, x5 + h, t) - 2 * f(x1, x2, x3, x4, x5, t) + f(x1, x2, x3, x4, x5 - h, t)) / (h ** 2))

# mixed second derivatives
def d2f_dx1dx2(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1 + h, x2 + h, x3, x4, x5, t) - f(x1 + h, x2 - h, x3, x4, x5, t) - f(x1 - h, x2 + h, x3, x4, x5, t) + f(
        x1 - h, x2 - h, x3, x4, x5, t)) / (4 * h * h)


def d2f_dx1dx3(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1 + h, x2, x3 + h, x4, x5, t) - f(x1 + h, x2, x3 - h, x4, x5, t) - f(x1 - h, x2, x3 + h, x4, x5, t) + f(
        x1 - h, x2, x3 - h, x4, x5, t)) / (4 * h * h)


def d2f_dx1dx4(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1 + h, x2, x3, x4 + h, x5, t) - f(x1 + h, x2, x3, x4 - h, x5, t) - f(x1 - h, x2, x3, x4 + h, x5, t) + f(
        x1 - h, x2, x3, x4 - h, x5, t)) / (4 * h * h)


def d2f_dx1dx5(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1 + h, x2, x3, x4, x5 + h, t) - f(x1 + h, x2, x3, x4, x5 - h, t) - f(x1 - h, x2, x3, x4, x5 + h, t) + f(
        x1 - h, x2, x3, x4, x5 - h, t)) / (4 * h * h)


def d2f_dx2dx3(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1, x2 + h, x3 + h, x4, x5, t) - f(x1, x2 - h, x3 + h, x4, x5, t) - f(x1, x2 + h, x3 - h, x4, x5, t) + f(
        x1, x2 - h, x3 - h, x4, x5, t)) / (4 * h * h)


def d2f_dx2dx4(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1, x2 + h, x3, x4 + h, x5, t) - f(x1, x2 - h, x3, x4 + h, x5, t) - f(x1, x2 + h, x3, x4 - h, x5, t) + f(
        x1, x2 - h, x3, x4 - h, x5, t)) / (4 * h * h)


def d2f_dx2dx5(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1, x2 + h, x3, x4, x5 + h, t) - f(x1, x2 - h, x3, x4, x5 + h, t) - f(x1, x2 + h, x3, x4, x5 - h, t) + f(
        x1, x2 - h, x3, x4, x5 - h, t)) / (4 * h * h)


def d2f_dx3dx4(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1, x2, x3 + h, x4 + h, x5, t) - f(x1, x2, x3 + h, x4 - h, x5, t) - f(x1, x2, x3 - h, x4 + h, x5, t) + f(
        x1, x2, x3 - h, x4 - h, x5, t)) / (4 * h * h)


def d2f_dx3dx5(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1, x2, x3 + h, x4, x5 + h, t) - f(x1, x2, x3 + h, x4, x5 - h, t) - f(x1, x2, x3 - h, x4, x5 + h, t) + f(
        x1, x2, x3 - h, x4, x5 - h, t)) / (4 * h * h)


def d2f_dx4dx5(x, t):
    h = 10e-5
    x1, x2, x3, x4, x5 = x
    return (f(x1, x2, x3, x4 + h, x5 + h, t) - f(x1, x2, x3, x4 - h, x5 + h, t) - f(x1, x2, x3, x4 + h, x5 - h, t) + f(
        x1, x2, x3, x4 - h, x5 - h, t)) / (4 * h * h)

def gradient(x, t):
    return np.array([df_dx1(x, t), df_dx2(x, t), df_dx3(x, t), df_dx4(x, t), df_dx5(x, t)])


def hessian_matrix(x, t):
    hessian = np.array([
        [d2f_dx1(x, t), d2f_dx1dx2(x, t), d2f_dx1dx3(x, t), d2f_dx1dx4(x, t), d2f_dx1dx5(x, t)],
        [d2f_dx1dx2(x, t), d2f_dx2(x, t), d2f_dx2dx3(x, t), d2f_dx2dx4(x, t), d2f_dx2dx5(x, t)],
        [d2f_dx1dx3(x, t), d2f_dx2dx3(x, t), d2f_dx3(x, t), d2f_dx3dx4(x, t), d2f_dx3dx5(x, t)],
        [d2f_dx1dx4(x, t), d2f_dx2dx4(x, t), d2f_dx3dx4(x, t), d2f_dx4(x, t), d2f_dx4dx5(x, t)],
        [d2f_dx1dx5(x, t), d2f_dx2dx5(x, t), d2f_dx3dx5(x, t), d2f_dx4dx5(x, t), d2f_dx5(x, t)],
    ])
    return hessian

# Example usage:
x_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
grad = gradient(x_values, 0) 
hessi = hessian_matrix(x_values, 0)  
print("Gradient:", grad)
print("Hessian Matrix:", hessi)
