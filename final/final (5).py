from __future__ import annotations
from typing import Union
import math, cmath
import re, matplotlib.pyplot as plt, numpy as np


class Complex:
    def __init__(self, real: Union[int, float] = 0, img: Union[int, float]= 0) -> None:
        self.real: Union[int, float] = real
        self.img: Union[int, float] = img

    def __str__(self):
        if self.img == 0:
            return str(self.real)
        else:
            return f"{self.real} {self.img}i"
        
    def __add__(self, other: Union[int, float, Complex]):
        if isinstance(other, Union[int, float]):
            self.real += other
        elif isinstance(other, Complex):
            self.real += other.real
            self.img += other.img
        return self

    def __radd__(self, other: Union[int, float, Complex]):
        return self.__add__(other)

    def __sub__(self, other: Union[int, float, Complex]):
        if isinstance(other, Union[int, float]):
            self.real -= other
        elif isinstance(other, Complex):
            self.real -= other.real
            self.img -= other.img
        return self

    def __rsub__(self, other: Union[int, float, Complex]):
        self.img *= -1
        self.real *= -1
        return self.__add__(other)

    def __mul__(self, other: Union[int, float, Complex]):
        if isinstance(other, Union[int, float]):
            self.real *= other
            self.img *= other
        elif isinstance(other, Complex):
            a = self.real
            b = self.img
            c = other.real
            d = other.img
            self.real = a*c - b*d
            self.img = a*d + b*c
        return self

    def __rmul__(self, other: Union[int, float, Complex]):
        return self.__mul__(other)
    
    def __truediv__(self, other: Union[int, float, Complex]):
        if isinstance(other, Union[int, float]):
            self.real /= other
            self.img /= other
        elif isinstance(other, Complex):
            a = other.real
            b = other.img
            other.img *= -1
            self.__mul__(other)
            self.__truediv__(a*a + b*b)
        return self
    
    def __rtruediv__(self, other: Union[int, float, Complex]):
        if isinstance(other, Union[int, float]):
            a = self.real
            b = self.img
            self.img = other
            self.real = 0
            self.__truediv__(Complex(a, b))
        elif isinstance(other, Complex):    
            a = self.real
            b = self.img
            c = other.real
            d = other.img
            self.img = c
            self.real = d
            self.__truediv__(Complex(a, b))
        return self

    def __pow__(self, other: Union[int, float, Complex]):
        if isinstance(other, Union[int, float]):
            if other == 0:
                return 1
            elif other > 0:
                a = self.real
                b = self.img
                for _ in range(other - 1):
                    self.__mul__(Complex(a, b))
                return self
            else:
                raise ValueError("Cannot be raised to a complex number")
        elif isinstance(other, Complex):
            raise ValueError("Cannot be raised to a complex number")
    
    def __rpow__(self, other: Union[int, float, Complex]):
        raise ValueError("Cannot be raised to a complex number")
    
class Equation:
    def __init__(self, equation):
        self.equation = equation.replace(" ", "")
        print("equation class", equation)
        self.state = self.check()
        self.is_constant = True if re.search("^-?\d+$", self.equation) else False
        self.is_polynomial = False
        self.is_trigonometric = False
        self.dydx = False
        self.d2ydx2 = False
        self.F = None
        self.diff_table = {      # f -> f'
            'e^x': 'e^x',
            '-e^x': '-e^x',
            'sin(x)': 'cos(x)',
            'cos(x)': '-sin(x)',
            '-sin(x)': '-cos(x)',
            '-cos(x)': 'sin(x)',
            'ln(x)': '1/x',
            '-ln(x)': '-1/x'
        }
        self.integral_table = {  # f' -> f
            'e^x': 'e^x',
            '-e^x': '-e^x',
            'cos(x)': 'sin(x)',
            '-cos(x)': '-sin(x)',
            'sin(x)': '-cos(x)',
            '-sin(x)': 'cos(x)',
            '1/x': 'ln(x)',
            '-1/x': '-ln(x)'
        }
    
    def check(self):
        if len(re.findall("^-?\d+$", self.equation)) != 0:
            # print(self.equation)
            return True
        if len(re.findall("^([+-]?\d*\*x\^?\d*)", self.equation)) != 0:
            return True
        if len(re.findall("-?sin\(x\)|-?cos\(x\)|-?e\^x|-?ln\(x\)", self.equation)) != 0:
            return True
        return False

    def derivative_terms(self, term):
        coeff = pow = None
        if re.search("\*x", term):
            coeff = int(re.findall("([+-]?\d*)\*x", term)[-1])
            if re.search("\^", term):
                pow = int(re.findall("x\^(\d+)", term)[-1])
        if pow != None:
            return f"{coeff * pow:+}*x^{pow - 1}" if pow != 2 else f"{coeff * pow:+}*x"
        return f"{coeff:+}"

    def diff_polynomial(self):
        terms = re.findall("([+-]?\d*\*x\^?\d*)", self.equation)
        self.dydx = ""
        for term in terms:
            self.dydx += self.derivative_terms(term)
        return self.dydx.strip("+")
    def diff(self):
        if len(re.findall("^-?\d+$", self.equation)) != 0:
            return "0"
        elif len(re.findall("^([+-]?\d*\*x\^?\d*)", self.equation)) != 0: 
            self.is_polynomial = True
            return self.diff_polynomial()
        elif len(re.findall("-?sin\(x\)|-?cos\(x\)|-?e\^x|-?ln\(x\)", self.equation)) != 0:
            self.is_trigonometric = True
            print("diff", self.equation)
            return self.diff_table[self.equation]
        return
        
    def find_const(self, expression):
        const = re.findall("([+-]?\d*\*x\^?\d*)", expression) 
        for i in const:
            expression = expression.replace(i, "")
        const = expression
        return const

    def integral_terms(self, term):
        coeff = pow = None
        if re.search("\*x", term):
            coeff = int(re.findall("([+-]?\d*)\*x", term)[-1])
            if re.search("\^", term):
                pow = int(re.findall("x\^(\d+)", term)[-1])
        if pow != None:
            return f"{coeff / (pow + 1):+.3f}*x^{pow + 1}"
        return f"{coeff / 2:+.3f}*x^2"

    def integrate_polynomial(self):
        terms = re.findall("([+-]?\d*\*x\^?\d*)", self.equation)
        const = self.find_const(self.equation)
        self.F = ""
        for term in terms:
            self.F += self.integral_terms(term)
        self.F = self.F.strip("+")
        return self.F + "+C" if const == "" else self.F + const + "*x+C"

    def integrate(self):
        if len(re.findall("^([+-]?\d*\*x\^?\d*)", self.equation)) != 0:
            print(self.integrate_polynomial())
            return self.integrate_polynomial()
        if re.search("^-?\d+$", self.equation):
            return self.equation + "*x+C"
        if re.search("-?sin\(x\)|-?cos\(x\)|-?e\^x|-?1/x", self.equation):
            self.is_trigonometric = True
            return self.integral_table[self.equation]

    def definite_integral(self, function, a, b):
        print("definite integral", function)
        fa = self.convert_to_numeric(function, a)
        fb = self.convert_to_numeric(function, b)
        return eval(fb) - eval(fa)

    def is_quadratic_equation(self):
        if len(re.findall("^(\d+\*x\^2)([+-]?\d+\*x)?([+-]?\d+)?$", self.equation)):
            return True
        return False

    def solve_quadratic_equation(self, a = 0, b = 0, c = 0):
        terms = re.findall("([+-]?\d*)\*x\^?\d*", self.equation)
        if len(terms) == 1:
            a = int(terms[0].strip("+"))
        else:
            a, b = int(terms[0].strip("+")), int(terms[1].strip("+"))
        c = int(self.find_const(self.equation).strip("+"))
        print(a, b, c)
        D = lambda a, b, c: b*b - 4*a*c
        d = D(a, b, c)
        if d == 0:
            x1 = (-b) / (2*a)
            return [x1]
        elif d > 0:
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            return [x1, x2]
        return []        

    def convert_to_numeric(self, function, x = None):
        if x != None:
            function = re.sub("x", f"{x}", function)
        print("convert to numeric function", re.sub("\^", "**", function), x)
        return re.sub("\^", "**", function)

    def plot(self, function = None, first_deriv = False, second_deriv = False):
        x = np.linspace(-7.5, 7.5, 1000)
        print("is constant", self.is_constant)
        print("function state", self.state)
        # x = 1
        plt.xlabel("x - axis")
        plt.ylabel("y - axis")
        plt.axvline(x = 0, c = "black")
        plt.axhline(y = 0, c = "black")
        if self.is_constant:
            plt.axhline(y = self.equation, label = f"y={self.equation}")
        else:
            if self.is_trigonometric: 
                if self.equation[0] == "-":
                    f = self.equation.replace("-", "-np.")
                else:
                    f = "np." + self.equation
                print(f)
                f = self.convert_to_numeric(f)
                dydx = Equation(self.diff())
                print("show graph", dydx.equation)
                if dydx.equation != "":
                    if dydx.equation[0] == "-":
                        f_diff = dydx.equation.replace("-", "-np.")
                    else:
                        f_diff = "np." + dydx.equation
                    print(f_diff)
                    f_diff = self.convert_to_numeric(f_diff)
                    plt.plot(x, eval(f_diff), label = f"y'={dydx.equation}")

                plt.plot(x, eval(f), label = f"y={self.equation}")
            else:
                f = self.convert_to_numeric(self.equation) # y = f(x)
                print("f", f)
                # f = self.convert_to_numeric(self.dydx)
                # dydx = self.diff()                         # y' = f'(x)
                dydx = Equation(self.diff())
                print("dydx", dydx.equation)
                d2ydx2 = Equation(dydx.diff())      # y'' = f''(x)
                print("d2ydx2", d2ydx2.equation)
                plt.plot(x, eval(f), label = f"y={self.equation}")
                if dydx.equation != "":
                    if dydx.is_constant:
                        plt.axhline(y = dydx.equation, label = f"y'={dydx.equation}")
                    else:
                        dydx_f = self.convert_to_numeric(dydx.equation)
                        plt.plot(x, eval(dydx_f), label = f"y'={dydx.equation}")
        plt.legend()
        plt.show()

def example_of_complex_number():
    """Пример комплексных чисел"""
    a = Complex(1, 3)
    b = Complex(0, 3)
    print(a + b)

def example_of_critical_points():
    """Пример критических точек"""
    f = Equation("1*x^2")
    critical_points = f.solve_quadratic_equation()
    print(*critical_points)

def example_of_function_graph():
    """Пример построения графиков"""
    f = Equation("1*x^2")
    f.plot()




def integrate(func, start, end, num_points=1000):
    total_sum = 0
    step = (end - start) / num_points
    for i in range(num_points):
        total_sum += func(start + i * step)
    return total_sum * step

def cos_component(n, omega, t, func):
    return func(t) * math.cos(n * omega * t)

def sin_component(n, omega, t, func):
    return func(t) * math.sin(n * omega * t)

def fourier_series_coefficients(func, T, N):
    a0 = integrate(func, 0, T) / T
    a = [a0]
    b = [0]
    omega = 2 * math.pi / T

    for n in range(1, N + 1):
        an = 2 / T * integrate(lambda t: cos_component(n, omega, t, func), 0, T)
        bn = 2 / T * integrate(lambda t: sin_component(n, omega, t, func), 0, T)
        a.append(an)
        b.append(bn)

    return a, b

def fourier_series(a, b, T, t, N):
    omega = 2 * math.pi / T
    result = a[0] / 2
    for n in range(1, N + 1):
        result += a[n] * math.cos(n * omega * t) + b[n] * math.sin(n * omega * t)
    return result

def get_user_function():
    expression = input("Enter your function in terms of x: ")
    try:
        func = lambda x: eval(expression, {'math': math, 'x': x, 'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': math.log, 'pi': math.pi, 'sqrt': math.sqrt})
        return func
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def get_user_t():
    try:
        t = float(input("Enter the value of t: "))
        return t
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None

def solve_trigonometric_equation():
    equation = input("Enter the trigonometric equation in terms of x: ")
    lower_limit = float(input("Enter lower limit (a): "))
    upper_limit = float(input("Enter upper limit (b): "))

    solution = bisection_method(equation, lower_limit, upper_limit)

    if solution is not None:
        print(f"Approximate solution: x = {solution}")
    else:
        print("No solution found within the specified tolerance.")

def bisection_method(equation, a, b, tol=1e-6, max_iter=100):
    fa = parse_input(equation, a)
    fb = parse_input(equation, b)

    if fa * fb > 0:
        print("Error: Function values at endpoints must have opposite signs.")
        return None

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        fc = parse_input(equation, c)

        if fc == 0:
            return c  

        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iter_count += 1

    return (a + b) / 2

def parse_input(value, x=None):
    try:
        if x is not None:
            return eval(value, {'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'pi': math.pi, 'x': x})
        else:
            return eval(value, {'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'pi': math.pi})
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * h * (f(a) + f(b))
    for i in range(1, n):
        result += h * f(a + i * h)
    return result

def integ_steps(a, b, result, h):
    h = (b - a) / 20
    try:
        steps_result = f'({h}/2) * (f({a}) + 2 * f({a+h}) + 2*f({a+2*h}) + ... + f({b}) = {result}'
        print(steps_result)
    except Exception as e:
        print(f"Error in step-by-step calculation: {str(e)}")

def integral_calc():
    function_str = input("Enter the function: ")
    lower_limit_str = input("Enter lower limit (a): ")
    upper_limit_str = input("Enter upper limit (b): ")

    lower_limit = parse_input(lower_limit_str)
    upper_limit = parse_input(upper_limit_str)

    if not function_str or lower_limit is None or upper_limit is None:
        print("Invalid input. Please make sure to enter a valid function and numeric limits.")
        return

    num_subintervals = 20
    func = lambda x: eval(function_str, {'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': math.log, 'pi': math.pi, 'sqrt': math.sqrt, 'x': x})
    try:
        result1 = trapezoidal_rule(func, lower_limit, upper_limit, num_subintervals)
        result = f"{result1:.6f}"
        print(f"Integral Result: ∫({function_str})dx = {result} x∈[{lower_limit};{upper_limit}]")
        integ_steps(lower_limit, upper_limit, result, num_subintervals)
    except Exception as e:
        print(f"Error: {str(e)}")

def double_integral_calc():
    function_str = input("Enter the function: ")
    lower_limit_x_str = input("Enter lower limit for x: ")
    upper_limit_x_str = input("Enter upper limit for x: ")
    lower_limit_y_str = input("Enter lower limit for y: ")
    upper_limit_y_str = input("Enter upper limit for y: ")

    lower_limit_x = parse_input(lower_limit_x_str)
    upper_limit_x = parse_input(upper_limit_x_str)
    lower_limit_y = parse_input(lower_limit_y_str)
    upper_limit_y = parse_input(upper_limit_y_str)

    if not function_str or any(val is None for val in [lower_limit_x, upper_limit_x, lower_limit_y, upper_limit_y]):
        print("Invalid input. Please make sure to enter a valid function and numeric limits.")
        return

    num_subintervals_x = 20
    num_subintervals_y = 20

    func = lambda x, y: eval(function_str, {'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': math.log, 'pi': math.pi, 'sqrt': math.sqrt, 'x': x, 'y': y})

    try:
        result_x = trapezoidal_rule(lambda x: trapezoidal_rule(lambda y: func(x, y), lower_limit_y, upper_limit_y, num_subintervals_y), lower_limit_x, upper_limit_x, num_subintervals_x)
        result = f"{result_x:.6f}"
        print(f"Double Integral Result: ∬({function_str})dA = {result} x∈[{lower_limit_x};{upper_limit_x}], y∈[{lower_limit_y};{upper_limit_y}] ")
    except Exception as e:
        print(f"Error: {str(e)}")

def calculate_fourier_series():
    user_func = get_user_function()
    
    if user_func:
        T = 1 
        N = 10  

        a, b = fourier_series_coefficients(user_func, T, N)
        
        t_values = [float(val) for val in input("Enter values of t: ").split(',')]
        
        for t in t_values:
            print(f"t={t}, f(t)={user_func(t)}, Fourier ~ {fourier_series(a, b, T, t, N)}")

def gcd(x,y):
    if x==y:
        return x
    elif x>y:
        return gcd(x-y,y)
    else:
        return gcd(x,y-x)

def number_factorization_operations():
    print("Select operation:")
    print("1. GCD/LCM")
    print("2. Factors")
    print("3. Prime factor")

    choice = input("Enter choice: 1, 2, or 3: ")

    if choice == '1':
        a, b = input("Enter numbers: ").split(" ")
        a, b = int(a), int(b)
        print("GCD: " + str(gcd(a, b)))
        print("LCM: " + str(a * b // gcd(a, b)))

    elif choice == '2':
        number = int(input("Enter a number for factors: "))
        factors = []

        for i in range(1, int(math.sqrt(number)) + 1):
            if number % i == 0:
                factors.append(i)
                factor_pair = number // i
                if factor_pair != i:
                    factors.append(factor_pair)

        factors.sort()
        print(factors)

    elif choice == '3':
        number = int(input("Enter number for prime factor: "))
        factors = []
        while number % 2 == 0:
            factors.append(2)
            number //= 2
        divisor = 3
        while number != 1 and divisor <= number:
            if number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            else:
                divisor += 2
        print("The prime factors are: ")
        for i in range(len(factors)):
            print(factors[i], end=', ')
    else:
        print("Invalid input")


def calculate_limit():
    user_func = get_user_function()

    if user_func:
        limit_point = get_user_limit_point()
        approach_direction = get_user_approach_direction()

        if limit_point is not None and approach_direction is not None:
            try:
                limit_result = calculate_limit_value(user_func, limit_point, approach_direction)
                print(f"The limit is approximately: {limit_result}")
            except Exception as e:
                print(f"Unable to calculate the limit. Error: {str(e)}")

def calculate_limit_value(func, x, approach_direction):
    if approach_direction == 'both':
        limit_positive = func(x + 1e-10)
        limit_negative = func(x - 1e-10)
        return (limit_positive + limit_negative) / 2
    elif approach_direction == 'positive':
        return func(x + 1e-10)
    elif approach_direction == 'negative':
        return func(x - 1e-10)

def get_user_limit_point():
    try:
        x_str = input("Enter the limit point (x): ")
        x = eval(x_str, {'math': math, 'pi': math.pi})
        return x
    except Exception as e:
        print(f"Invalid input. {str(e)}")
        return None

def get_user_approach_direction():
    approach_direction = input("Enter the approach direction ('both', 'positive', or 'negative'): ")
    if approach_direction.lower() in ['both', 'positive', 'negative']:
        return approach_direction.lower()
    else:
        print("Invalid input. Please enter 'both', 'positive', or 'negative'.")
        return None

def get_user_function():
    expression = input("Enter your function in terms of x: ")
    try:
        func = lambda x: eval(expression, {'math': math, 'x': x, 'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': math.log, 'pi': math.pi, 'sqrt': math.sqrt})
        return func
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    elif discriminant == 0:
        root1 = root2 = -b / (2*a)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)

    # Check if roots are real and remove imaginary part if it's negligible
    if root1.imag == 0:
        root1 = root1.real
    if root2.imag == 0:
        root2 = root2.real

    return root1, root2

def solve_cubic(a, b, c, d):
    a, b, c, d = map(complex, (a, b, c, d))

    if a == 0:
        raise ValueError("The coefficient 'a' must not be 0 for a cubic equation.")

    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    roots = []
    for k in range(3):
        omega_k = cmath.exp(2j * cmath.pi * k / 3)
        term = ((-q/2) + cmath.sqrt((q/2)**2 + (p/3)**3))**(1/3)
        root = omega_k * term - p/(3*omega_k*term) - b/(3*a)
        roots.append(root)

    return roots

def polynomials_menu():
    print("Enter the coefficients of the equation (up to 4). For a quadratic equation, enter 3 coefficients.") 
    coeffs = list(map(float, input("Enter coefficients separated by space: ").split())) 

    if len(coeffs) == 3:
        roots = solve_quadratic(*coeffs)
        rounded_roots = [(round(root.real, 4) + round(root.imag, 4) * 1j) for root in roots]
        print("The roots of the quadratic equation are:", rounded_roots)
    elif len(coeffs) == 4:
        roots = solve_cubic(*coeffs)
        rounded_roots = [(round(root.real, 4) + round(root.imag, 4) * 1j) for root in roots]
        print("The roots of the cubic equation are:", rounded_roots)
    else:
        print("Invalid number of coefficients. Please enter exactly 3 or 4 coefficients.")


def safe_eval(expr, x):
    allowed_functions = {'sin': math.sin,'cos': math.cos,'tan': math.tan,'exp': math.exp,'log': math.log,'sqrt': math.sqrt,'pow': pow}

    # Replace the allowed function names in the expression with their corresponding function calls
    for func_name in allowed_functions:
        expr = expr.replace(func_name, f'allowed_functions["{func_name}"]')

    try:
        return eval(expr, {"__builtins__": {}}, {"x": x, "allowed_functions": allowed_functions})
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

def ord5(f, x):
    h = 0.00001
    df = -f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h)
    dy = 12*h
    return df/dy

def ord6(f, x):
    h = 0.004
    df = f(x+3*h) - 6*f(x+2*h) + 15*f(x+h) - 20*f(x) + 15*f(x-h) - 6*f(x-2*h) + f(x-3*h)
    dy = h**6
    return df/dy

def ord7(f, x):
    h = 0.1
    df = -f(x+3*h) + 9*f(x+2*h) - 45*f(x+h) + 45*f(x-h) - 9*f(x-2*h) + f(x-3*h)
    dy = 180*h
    return df/dy

def ord8(f, x):
    h = 0.01
    df = f(x+4*h) - 8*f(x+3*h) + 28*f(x+2*h) - 56*f(x+h) + 70*f(x) - 56*f(x-h) + 28*f(x-2*h) - 8*f(x-3*h) + f(x-4*h)
    dy = h**8
    return df/dy

def ord9(f, x):
    h = 0.1
    df = -f(x+4*h) + 12*f(x+3*h) - 90*f(x+2*h) + 560*f(x+h) - 560*f(x-h) + 90*f(x-2*h) - 12*f(x-3*h) + f(x-4*h)
    dy = 5040*h
    return df/dy

def ord10(f, x):
    h = 0.1
    df = f(x+5*h) - 10*f(x+4*h) + 45*f(x+3*h) - 120*f(x+2*h) + 210*f(x+h) - 210*f(x-h) + 120*f(x-2*h) - 45*f(x-3*h) + 10*f(x-4*h) - f(x-5*h)
    dy = 3628800*h
    return df/dy

def diff(f, x, order = 1): #max ord for derivatives is 10
    h = 1e-3
    
    if order == 1:
        df = f(x+h) - f(x-h)
        dy = 2*h
        res = df/dy
        
    elif order == 2:
        df = f(x+h) - 2*f(x) + f(x-h)
        dy = h**2
        res = df/dy
    
    elif order == 3:
        df = f(x+2*h) - 2*f(x+h) + 2*f(x-h) - f(x-2*h)
        dy = 2*h**3
        res = df/dy
    
    elif order == 4:
        df = f(x+2*h) - 4*f(x+h) + 6*f(x) - 4*f(x-h) + f(x-2*h)
        dy = h**4
        res = df/dy
    
    elif order == 5:
        res = ord5(f, x)
    
    elif order == 6:
        res = ord6(f, x)
    
    elif order == 7:
        res = ord7(f, x)
    
    elif order == 8:
        res = ord8(f, x)
    
    elif order == 9:
        res = ord9(f, x)

    elif order == 10:
        res = ord10(f, x)
        
    return res

# Taylor series coefficients
def taylor_ser_coef(func_expr, ord, x0):
    func = lambda x: safe_eval(func_expr, x)
    coef = []

    for i in range(1, ord + 1):
        der_x0 = diff(func, x0, i)
        coef.append(round((der_x0 / math.factorial(i)), 2))

    str_res = f'{func(x0)} + '
    for i in range(1, ord + 1):
        if coef[i - 1] != 0:
            str_res += str(coef[i - 1]) + (f' * (x-{x0})**{i}') + " + "

    str_res = str_res[:-3] if str_res else '0'

    return coef, str_res


def taylor_series_menu():
    print("\nTaylor Series Menu:")
    func_expr = input("Enter a function of x: ")
    ord = int(input("Enter the order of the Taylor series: "))
    x0 = float(input("Enter the point x0: "))
    a, b = taylor_ser_coef(func_expr, ord, x0)
    print(f'Coef: {a}')
    print(b)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Calculate Integral")
        print("2. Calculate Double Integral")
        print("3. Solve Trigonometric Equation")
        print("4. Calculate Fourier Series")
        print("5. Number Factorization Operations")
        print("6. Simple Limits")
        print("7. Quadratic and Cubic Polynomials")
        print("8. Taylor Series")
        print("9. Complex number")
        print("10. Critical points")
        print("11. Graph of the function")
        print("12. Exit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8, or 9): ")

        if choice == "1":
            integral_calc()
        elif choice == "2":
            double_integral_calc()
        elif choice == "3":
            solve_trigonometric_equation()
        elif choice == "4":
            calculate_fourier_series()
        elif choice == "5":
            number_factorization_operations()
        elif choice == "6":
            calculate_limit()
        elif choice == "7":
            polynomials_menu()
        elif choice == "8":
            taylor_series_menu()
        elif choice == "9":
            example_of_complex_number()
        elif choice == "10":
            example_of_critical_points()
        elif choice == "11":
            example_of_function_graph()
        elif choice == "12":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, 8, or 9.")


if __name__ == "__main__":
    main_menu()
