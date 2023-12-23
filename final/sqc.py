import cmath 
 
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
 
def main(): 
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
        print("Invalid number of coefficients. Please enter either 3 or 4 coefficients.") 
 
if __name__ == "__main__": 
    main()