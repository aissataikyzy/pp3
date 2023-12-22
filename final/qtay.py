import math

# Safe evaluation of user-input function
def safe_eval(expr, x):
    allowed_functions = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'exp': math.exp,
        'log': math.log,
        'sqrt': math.sqrt,
        'pow': pow
        # Add any other allowed functions here
    }

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
    
    for i in range(1, ord+1):
        der_x0 = diff(func, x0, i)
        coef.append(round((der_x0/math.factorial(i)), 2))
    
    str_res = f'{func(x0)} + '
    for i in range(1, ord+1):
        if coef[i-1] != 0:
            str_res += str(coef[i-1]) + (f' * (x-{x0})**{i}') + " + "
    
    str_res = str_res[:-3] if str_res else '0'  
    
    return coef, str_res

# User input
func_expr = input("Enter a function of x (e.g., 'x**3 + sin(x)'): ")
ord = int(input("Enter the order of the Taylor series: "))
x0 = float(input("Enter the point x0: "))

# Calculate and display the Taylor series
a, b = taylor_ser_coef(func_expr, ord, x0)
print(f'Coef: {a}')
print(b)