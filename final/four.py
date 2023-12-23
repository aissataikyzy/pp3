import math 
 
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
    expression = input("Enter your function in terms of t: ") 
    try: 
        func = lambda t: eval(expression, {'math': math, 't': t}) 
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
 
# Parameters 
T = 1  # Period 
N = 10  # Number of Fourier series terms 
 
# Get user function 
user_func = get_user_function() 
 
if user_func: 
    # Get Fourier coefficients 
    a, b = fourier_series_coefficients(user_func, T, N) 
 
    # Get user-defined t value 
    user_t = get_user_t() 
 
    if user_t is not None: 
        # Reconstruct and print the function for the user-defined t value 
        print(f"At t={user_t},  Fourier ~ {fourier_series(a, b, T, user_t, N)}")